n_symbols = 16 * 10;
n_bit_per_symbol = 4;
n_samples_per_symbol = 8;

f = fopen('vector_source', 'rb');
symbols = fread(f, n_symbols, 'uint8')
fclose(f);

f = fopen('packed', 'rb');
packed_symbols = fread(f, 8/n_bit_per_symbol * n_symbols, 'uint8');
dec2bin(packed_symbols)
fclose(f);

f = fopen('16qam', 'rb');
qam_samples_interleaved = fread(f, 2*n_symbols * n_samples_per_symbol, 'float');
qam_samples = qam_samples_interleaved(1:2:end) + i*qam_samples_interleaved(2:2:end)
fclose(f);

plot(real(qam_samples))
