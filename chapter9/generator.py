def genFunc(num):
    for i in range(0, num):
        yield i
        print('Generator ing...')


for data in genFunc(5):
    print(data)