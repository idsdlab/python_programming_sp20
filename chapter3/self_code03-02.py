# self_code03-02.py

a = 11
b = 0o11
c = 0x11

bin_a = bin(a)
bin_b = bin(b)
bin_c = bin(c)

print(a, b, c)
print(bin_a, bin_b, bin_c)

dec_a = int(bin_a, 2)
dec_b = int(bin_b, 2)
dec_c = int(bin_c, 2)

print(dec_a, dec_b, dec_c)





