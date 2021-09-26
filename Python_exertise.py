#---------------------Python excercise1 ------------------------------------------#


1. Css Selector 수정
#Css Selector는 웹 페이지에서 특정 요소를 선택하기 위해 해당 요소까지 찾아갈 수 있도록 해주는 주소와 같은 것이다.
# 대부분의 웹브라우져에서 는 해당 요소에 대한 css selector 값을 쉽게 얻어올 수 있다
selector = "#today_main_news > div.hdline_news > ul > li:nth-child(1)"

selector_list = selector.split(">")
selector_list[-1] = selector_list[-1].split(":")[0]

" > ".join(selector_list)

2. list comprehension으로 만드는 구구단
#리스트 컴프리헨션은 쉽게 말해 ‘리스트를 쉽게, 짧게 한 줄로 만들 수 있는 파이썬의 문법’이다. 
def gugu_com(x=2):
    [print(f"{x} x {i} = {x*i}") for i in range(1, 10)]

gugu_com(2)

3. 두 주사위의 곱
die = [i for i in range(1,7)]

[[j*i for i in die] for j in die]

4. 두 주사위의 합
dice_sum = [[2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8],
            [4, 5, 6, 7, 8, 9], 
            [5, 6, 7, 8, 9, 10],
            [6, 7, 8, 9, 10, 11],
            [7, 8, 9, 10, 11, 12]]

print(dice_sum[1][5])
print(dice_sum[5][1])

die = [i for i in range(1,7)]  # 반복문을 이용한 풀이

dice_sum = [[j+i for i in die] for j in die]

print(dice_sum[1][5])
print(dice_sum[5][1])

*도전문제(표절 검사 프로그램)
from collections import defaultdict, Counter

text = """Python is a very simple programming language so even if you are new to programming, you can learn python without facing any issues."""
text2 = """C is a very difficult programming language so even if you are good at programming, you can learn c with facing any issues."""
text3 = """R Programming is good at statistical analysis. you can learn easily"""

def word_counter(text):
    word_count = defaultdict(lambda: 0)
    for word in text.lower().split(): #각 단어를 소문자로 바꾸고 단어별로 나누는 과정
        word_count[word] += 1 #디폴트 값 0으로 설정해둔 곳에, 한번 이상 단어가 반복되면 count 한다.
        
    return word_count

    word_counter(text)

(text와 text2의 유사도와 text와 text3의 유사도 측정)
def text_similarity(text_count_1, text_count_2):
    text1_count = Counter(text_count_1)
    text2_count = Counter(text_count_2)
    
    word_total = sum(text1_count.values())
    word_diff = sum((text1_count - text2_count).values())
    
    return (1 - word_diff / word_total) * 100

text_similarity(word_counter(text), word_counter(text2))
text_similarity(word_counter(text), word_counter(text3))


#--------------------- Python excercise2 ------------------------------------------#
1. 람다함수
#람다(lambda) 함수는 함수의 이름 없이, 함수처럼 사용할 수 있는 익명의 함수를 말한다. 

1.1. 기존 함수
def f(x,y): #f라는 함수에 매개변수 2개를 받는다.
    return x + y #x와 y의 합을 반환한다.

print(f(1,4))

1.2. lambda 함수 할당
f=lambda x,y: x + y #f라는 변수가 함수의 이름처럼 사용된다.

#람다함수의 공식
##lamda 인수1, 인수2 : 수식
#인수1과 인수2는 인수를 나타낸다. (기존함수에서 def() 괄호안에 해당하는 값)

print(f(1,4))

1.3. 익명의 lambda 함수
print((lambda x, y:x + y)(1, 4))

2. 맵리듀스
2.1. map 함수 #연속 데이터를 저장하는 시퀀스 자료형에서 요소마다 같은 기능을 적용할 때 사용한다.

ex = [1,2,3,4,5]
f = lambda x:x**2
print(list(map(f, ex))

2.2. reduce 함수
#map() 함수와 다르지만 형제처럼 사용하는 함수로 리스트와 같은 시쿼스 자료형에 차례대로 함수를 적용하여 모든 값을 통합하는 함수이다.

from functools import reduce
print(reduce(lambda x,y:x+y, [1,2,3,4,5]))

3. 별표의 활용

3.1. 가변 인수로 활용
 - 가변인수
def asterisk_test(a, *args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5,6)

 - 키워드 가변 인수
def asterisk_test(a,**kargs):
    print(a,kargs)
    print(type(kargs))
asterisk_test(1,b=2,c=3,d=4,e=5,f=6)

3.2. 별표의 언패킹 기능
 -함수에서의 사용
 def asterisk_test(a,args):
    print(a,*args)
    print(type(args))
asterisk_test(1,(2,3,4,5,6))

def asterisk_test(a,args):
    print(a,args)
    print(type(args))
asterisk_test(1,(2,3,4,5,6))

- 일반 자료형에서의 사용
a,b,c=([1,2], [3,4], [5,6])
print(a,b,c)
data=([1,2], [3,4], [5,6])
print(*data)

- zip 함수와의 응용
for data in zip(*[[1,2],[3,4],[5,6]]):
    print(data)
    print(type(data))

- 키워드 가변 인수 응용
def asterisk_test(a,b,c,d):
    print(a,b,c,d)
data={"b":1, "c":2, "d":3}
asterisk_test(10, **data)

4. 선형대수학

4.1. 파이썬 스타일 코드로 표현한 벡터
vector_a=[1,2,10]  # 리스트로 표현한 경우
vector_b=(1,2,10)   # 튜플로 표현한 경우
vector_c={'x':1, 'y':2, 'z':10}  # 딕셔너리로 표현한 경우

#리스트는 대괄호 [ ]를, 튜플은 소괄호 ( )를, 딕셔너리는 중괄호 { }를 사용해서 나타낸다.
#리스트와 튜플은 표면상으로는 매우 유사한데 한 가지 중요한 차이가 있다.
#튜플의 경우 요소를 변경하거나 삭제할 수 없으나 리스트에서는 가능하다.
# 리스트와 튜플이 어떤 값만을 담을 수 있었다면, 딕셔너리는 키(key)라는 것과 그 키에 해당하는 값(value)을 담을 수 있다.

u=[2,2]
v=[2,3]
z=[3,5]
result=[] #result라는 공백의 리스트를 만들어 놓고 시작

for i in range(len(u)):
    result.append(u[i]+v[i]+z[i]) #result에 값을 추가하는 방식
print(result)

u=[2,2]
v=[2,3]
z=[3,5]
result=[sum(t) for t in zip(u,v,z)] #반복문의 형태
print(result)

- 별표를 사용한 함수화
def vector_addition(*args):
    return [sum(t) for t in zip(*args)]   # unpacking 통해 zip(u,v,z) 효과를 낼 수 있음.

vector_addition(u,v,z)

- 간단한 두벡터의 합
a = [1, 1]
b = [2, 2]

[x + y for x, y in zip(a, b)]

- 벡터의 연산: 스칼라곱
u=[1,2,3]
v=[4,4,4]

alpha=2

result=[alpha*sum(t) for t in zip(u,v)]
result

4.2. 파이썬 스타일코드로 표현한 행렬
- 딕셔너리로 표현하는 경우 좌표정보나 이름정보를 넣을 수 있으나 복잡함
matrix_a=[[3,6], [4,5]] #리스트로 표현한 경우
matrix_b=[(3,6), (4,5)] #튜플로 표현한 경우
matrix_c={(0,0):3, (0,1):6, (1,0):4, (1,1):5}  #디셔너리로 표현한경우

- 행렬의 연산: 행렬의 elemnet-wise 합
matrix_a=[[3,6], [4,5]]
matrix_b=[[5,8], [6,7]]

result=[[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]
print(result)

*일반문제(주민등록번호로 성별 찾기 with map)
pins = ["891120-1234567", "931120-2335567", "911120-1234234", "951120-1234567"]

list(map(lambda x: x.split("-")[1][0], pins))

*도전문제
a = [1, 2]
b = [3, 4]

dot = lambda a,b : sum([x*y for x, y in zip(a, b)])

dot(a,b)