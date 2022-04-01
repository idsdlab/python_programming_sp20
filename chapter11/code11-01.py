try:
    in_fp = open("C:/Temp/data1.txt", "r", encoding='utf-8')
    print('file is opened')
except:
    print('file is not opened')

in_str = in_fp.readline()
in_list = [in_str]
print(type(in_str), in_str, in_list)

