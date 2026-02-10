import numpy as np
from gnuradio import gr
from enum import Enum

class qam(Enum):
    QAM4 = 0
    QAM16 = 1
    QAM64 = 2
    QAM256 = 3

class differential_qam_encoder(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """"""

    def __init__(self, order=qam.QAM4):
        gr.sync_block.__init__(
            self,
            name='Differential QAM Encoder',   # will show up in GRC
            in_sig=[np.uint8],
            out_sig=[np.uint8]
        )
        self.order = order
        self.mask = np.uint8(3 << (2 * self.order.value))
        self.modulo = 2**((self.order.value+1)*2)
        self.prev_symbol = np.uint8(0)

    def work(self, input_items, output_items):
        for i in range(len(input_items[0])):
            with np.errstate(over='ignore'): # Overflow might happen (suppress warning since it's intentional)
                output_items[0][i] = ((self.prev_symbol & self.mask) + input_items[0][i]) % self.modulo
            self.prev_symbol = output_items[0][i]
        return len(output_items[0])
