import unittest
import numpy as np
from gnuradio import gr, gr_unittest, blocks
import random

from differential_qam_encoder import differential_qam_encoder
from differential_qam_decoder import differential_qam_decoder, qam

random.seed(42)

class test_differential_qam_encoder_decoder(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def generate_test_data(self, order):
        n_symbols = 2**((order.value+1)*2)
        src_data = np.array([random.randint(0, n_symbols-1) for _ in range(1000)], dtype=np.uint8)
        return src_data

    def test_encoder_decoder_qam4(self):
        order = qam.QAM4
        src_data = self.generate_test_data(order)
        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, dec, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(src_data))


    def test_encoder_decoder_qam16(self):
        order = qam.QAM16
        src_data = self.generate_test_data(order)
        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, dec, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(src_data))


    def test_encoder_decoder_qam64(self):
        order = qam.QAM64
        src_data = self.generate_test_data(order)
        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, dec, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(src_data))

    def test_encoder_decoder_qam256(self):
        order = qam.QAM256
        src_data = self.generate_test_data(order)
        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order)
        dec = differential_qam_decoder(order)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, dec, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(src_data))


if __name__ == '__main__':
    gr_unittest.run(test_differential_qam_encoder_decoder)
