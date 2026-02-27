import numpy as np
import threading
from gnuradio import gr


class byte_to_short(gr.sync_block):
    def __init__(self, n_bits = 8):
        gr.sync_block.__init__(
            self,
            name='Byte To Short',
            in_sig=[np.uint8],
            out_sig=[np.int16]
        )
        self._lock = threading.Lock()
        if (n_bits < 1 or n_bits > 8):
            raise ValueError(f"n_bits must be in range 1..8 (was {n_bits})")
        self.n_bits = int(n_bits)

    def set_n_bits(self, n_bits):
        n_bits = int(n_bits)
        if (n_bits < 1 or n_bits > 8):
            raise ValueError(f"n_bits must be in range 1..8 (was {n_bits})")
        with self._lock:
            self.n_bits = n_bits

    def work(self, input_items, output_items):
        with self._lock:
            n_bits = self.n_bits
        shift = 16 - n_bits
        # Inverse of offset-binary quantization used in short_to_byte.
        output_items[0][:] = ((input_items[0].astype(np.int32) << shift) - 2**15).astype(np.int16)
        return len(output_items[0])
