try:
    in_fp = open("C:/Temp/data1.txt", "r", encoding='utf-8')
    print('file is opened')
except:
    print('file is not opened')

in_list = in_fp.readlines()
# print(in_list)

for in_str in in_list:
    # print(in_str)
    in_str = in_str.splitlines()[0]
    print(in_str)


in_fp.close()

