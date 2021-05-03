listn=[52,273,32,72,100]
try:
    num=int(input("input int"))
    print("{}번째 요소: {}".format(num,listn[num]))
except ValueError as Exception:
    print("int int int")
    print("exception:", exception)
except IndexError as exception:
    print("index index index")
    print("exception", exception)
