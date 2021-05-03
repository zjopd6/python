#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("pi")


# In[2]:


user_input_a=input("정수로 입력")


if user_input_a.isdigit():
    number_input_a= int(user_input_a)
    
    
    print("원의 반지름:", number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14*number_input_a*number_input_a)
else:
    print("정수를 입력하지 않았습니다.")


# In[3]:


try:
    number_input_b= int(input("정수입력>"))
    print("원의 반지름:", number_input_b)
    print("원의 둘레: ", 2*3.14*number_input_b)
    print("원의 넓이:", 3.14*number_input_b*number_input_b)
except:
    print("무언가 잘못되었습니다..")


# In[5]:


list_input_a=["52","273","32","spy","103"]

list_number=[]

for item in list_input_a:
    
        try:
            float(item)
            list_number.append(item)
        except:
            pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))


# In[7]:


try:
    number_input_a = int(input("정수입력>"))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지름:", number_input_a)
    print("원의 둘레: ", 2*3.14*number_input_a)
    print("원의 넓이:", 3.14*number_input_a*number_input_a)


# In[11]:


try:
    num=int(input("정수입력>"))
    print("반지름:", num)
    print("둘레",2*3.14*num)
    print("넓이",3.14*num*num)
except:
    print(" ! 정 수 입 력 ! ")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("프로그램을 종료합니다.")


# In[13]:


def test():
    print("test()함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("함수의 마지막줄입니다.")
    
test()


# In[14]:


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


# In[18]:


try:
    num=int(input("int input"))
    print("circle half", num)
    print("circle dulae", num*2*3.14)
    print("circle mola", num*3.14*num)
except Exception as exception:
    print("type(exception)",type(exception))
    print("exception",exception)


# In[19]:


list_number = [52,273,32,72,100]
try:
    num=int(input("input int>"))
    print("{}번쨰 요소: {}".format(num,list_number[num]))
except ValueError:
    print("정수를 입력해주시요!")
except IndexError:
    print("리스트 인덱스를 벗어났어요")


# In[21]:


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


# In[23]:


listn=[52,273,32,72,100]
try:
    numi= int(input("정수입력: "))
    print("{}번째 요소:{}".format(numi,listn[numi]))
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해주세요!")
    print(type(exception),exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print(type(exception),exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception),exception)


# In[25]:


number =int("정수입력>")
number =int(number)

if number >0 :
    raise NotImplementedError
else:
    raise NotImplementedError
    


# In[ ]:




