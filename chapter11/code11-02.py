try:
    in_fp = open("C:/Temp/data1.txt", "r", encoding='utf-8')
    print('file is opened')
except:
    print('file is not opened')

# in_str = in_fp.readline()
# in_list = [in_str]
# print(type(in_str), in_str, in_list)

while True:
    in_str = in_fp.readline()
    if in_str == "":
        break
    in_str = in_str.rstrip('\n')
    # print(in_str, end="")
    print(in_str)

in_fp.close()

