import numpy as np
from gnuradio import gr, gr_unittest, blocks, digital

from differential_qam_encoder import differential_qam_encoder
from differential_qam_decoder import differential_qam_decoder, qam


class test_constellation(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def test_qam16_without_phase_shift(self):
        order = qam.QAM16
        src_data = range(16)
        test_constellation = digital.constellation_calcdist([-3+3j, -1+3j, 1+3j, 3+3j, -3+1j, -1+1j, 1+1j, 3+1j, -3-1j, -1-1j, 1-1j, 3-1j, -3-3j, -1-3j, 1-3j, 3-3j], [11, 9, 14, 15, 10, 8, 12, 13, 1, 0, 4, 6, 3, 2, 5, 7],
        4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        test_constellation.set_npwr(1)

        src = blocks.vector_source_b(src_data, False)
        enc = differential_qam_encoder(order)
        digital_constellation_encoder = digital.constellation_encoder_bc(test_constellation)
        digital_constellation_decoder = digital.constellation_decoder_cb(test_constellation)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, digital_constellation_encoder, digital_constellation_decoder, dec, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(src_data))

    def test_qam16_with_90deg_phase_shift(self):
        order = qam.QAM16
        src_data = range(16)
        test_constellation = digital.constellation_calcdist(
            [3+3j, 1+3j, 1+1j, 3+1j, -3+3j, -3+1j, -1+1j, -1+3j, -3-3j, -1-3j, -1-1j, -3-1j, 3-3j, 3-1j, 1-1j, 1-3j],
            range(16),
            4, 1, digital.constellation.AMPLITUDE_NORMALIZATION).base()
        test_constellation.set_npwr(1)

        src = blocks.vector_source_b(src_data, False)
        enc = differential_qam_encoder(order)
        digital_constellation_encoder = digital.constellation_encoder_bc(test_constellation)
        phase_shift = blocks.phase_shift(90, False)
        digital_constellation_decoder = digital.constellation_decoder_cb(test_constellation)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        # after_diff_encoder_sink = blocks.vector_sink_b()
        # self.tb.connect(enc, after_diff_encoder_sink)

        # enc_sink = blocks.vector_sink_c()
        # self.tb.connect(digital_constellation_encoder, enc_sink)

        # phase_sink = blocks.vector_sink_c()
        # self.tb.connect(phase_shift, phase_sink)

        # const_dec_sink = blocks.vector_sink_b()
        # self.tb.connect(digital_constellation_decoder, const_dec_sink)

        self.tb.connect(src, enc, digital_constellation_encoder, phase_shift, digital_constellation_decoder, dec, sink)
        self.tb.run()

        # print("After diff encoder:", after_diff_encoder_sink.data())
        # print("After encoder:", enc_sink.data())
        # print("After phase shifter:", phase_sink.data())
        # print("Symbols after constellation decoder:", const_dec_sink.data())

        result = sink.data()
        self.assertEqual(list(result)[1:], list(src_data)[1:])

if __name__ == '__main__':
    gr_unittest.run(test_constellation)
