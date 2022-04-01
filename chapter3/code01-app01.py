import sys

intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None] * 8

if __name__ == '__main__':
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

    print(sys.getsizeof(intVar))
    print(sys.getsizeof(floatVar))
    print(sys.getsizeof(boolVar))
    print(sys.getsizeof(strVar))
    print(sys.getsizeof(listVar))
    print(sys.getsizeof(tupleVar))
    print(sys.getsizeof(dictVar))
    print(sys.getsizeof(setVar))