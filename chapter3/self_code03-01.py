import sys

# getsizeof : returns the size of an object in bytes

print(sys.getsizeof(int()))
a = 1
print(sys.getsizeof(a))
a = 100
print(sys.getsizeof(a))
a = 18446744073709551615
print(sys.getsizeof(a))
a = 18446744073709551615000000000
print(sys.getsizeof(a))

#
# sys.exit(0)
# a = 18446744073709551615
# b = a+1
# c = b+1
# print(a)
# print(b)
# print(c)
#
#
