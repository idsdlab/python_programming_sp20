try:
    out_fp = open("C:/Temp/data1_write.txt", "w", encoding='utf-8')
    print('file is opened')
except:
    print('file is not opened')

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        out_fp.writelines(outStr + "\n")
    else:
        break

out_fp.close()
print('--- 정상적으로 파일에 씀 ---')