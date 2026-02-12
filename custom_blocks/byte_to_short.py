import numpy as np
from gnuradio import gr


class byte_to_short(gr.sync_block):
    def __init__(self, n_bits = 8):
        gr.sync_block.__init__(
            self,
            name='Byte To Short',
            in_sig=[np.uint8],
            out_sig=[np.int16]
        )
        if (n_bits < 1 or n_bits > 8):
            raise ValueError(f"n_bits must be in range 1..8 (was {n_bits})")
        self.n_bits = n_bits

    def work(self, input_items, output_items):
        output_items[0][:] = (input_items[0].astype(np.uint16) << (16 - self.n_bits)).astype(np.int16)
        return len(output_items[0])

