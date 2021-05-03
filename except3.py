list_number = [52,273,32,72,100]
try:
    num=int(input("input int>"))
    print("{}번쨰 요소: {}".format(num,list_number[num]))
except ValueError:
    print("정수를 입력해주시요!")
except IndexError:
    print("리스트 인덱스를 벗어났어요")
