import unittest
import numpy as np
from gnuradio import gr, gr_unittest, blocks

from differential_qam_encoder import differential_qam_encoder, qam


class test_differential_qam_encoder(gr_unittest.TestCase):

    def setUp(self):
        self.tb = gr.top_block()

    def tearDown(self):
        self.tb = None

    def generate_qam_test_data(self, order):
        quadrant_diff = np.array(range(4), dtype=np.uint8).repeat(2**(order.value*2))
        quadrant = quadrant_diff.cumsum() % 4
        symbol_part_in_quadrant = np.array(list(range(2**(order.value*2))) * 4, dtype=np.uint8)
        expected = quadrant << order.value*2 | symbol_part_in_quadrant
        src_data = quadrant_diff << order.value*2 | symbol_part_in_quadrant
        return (src_data, expected,)

    def test_qam4(self):
        (src_data, expected) = self.generate_qam_test_data(qam.QAM4)

        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order=qam.QAM4)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(expected))

    def test_qam16(self):
        (src_data, expected) = self.generate_qam_test_data(qam.QAM16)

        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order=qam.QAM16)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(expected))

    def test_qam64(self):
        (src_data, expected) = self.generate_qam_test_data(qam.QAM64)

        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order=qam.QAM64)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(expected))

    def test_qam256(self):
        (src_data, expected) = self.generate_qam_test_data(qam.QAM256)

        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order=qam.QAM256)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, sink)
        self.tb.run()

        result = sink.data()
        self.assertEqual(list(result), list(expected))


    def test_state_reset(self):
        src_data = np.array([1, 1], dtype=np.uint8)

        src = blocks.vector_source_b(src_data.tolist(), False)
        enc = differential_qam_encoder(order=qam.QAM4)
        sink = blocks.vector_sink_b()

        self.tb.connect(src, enc, sink)
        self.tb.run()

        # If the block is recreated, prev_symbol must reset
        self.assertEqual(list(sink.data()), [1, 2])


if __name__ == '__main__':
    gr_unittest.run(test_differential_qam_encoder)
