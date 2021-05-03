print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막줄입니다.")
print("프로그램 종료")

#----------------------------------------------------


try:
    num=int(input("int input"))
    print("circle half", num)
    print("circle dulae", num*2*3.14)
    print("circle mola", num*3.14*num)
except Exception as exception:
    print("type(exception)",type(exception))
    print("exception",exception)
