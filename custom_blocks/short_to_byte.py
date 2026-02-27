import numpy as np
import threading
from gnuradio import gr


class short_to_byte(gr.sync_block):
    def __init__(self, n_bits = 8):
        gr.sync_block.__init__(
            self,
            name='Short To Byte',
            in_sig=[np.int16],
            out_sig=[np.uint8]
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
            shift = 16 - self.n_bits
            max_code = (1 << self.n_bits) - 1

        # Offset-binary quantization: map int16 domain to 0..(2^n_bits-1).
        samples = input_items[0].astype(np.int32)
        codes = (samples + 2**15 + (1 << (shift - 1))) >> shift
        output_items[0][:] = np.clip(codes, 0, max_code).astype(np.uint8)
        return len(output_items[0])
