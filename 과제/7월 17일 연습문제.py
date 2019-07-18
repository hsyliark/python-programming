### 조건문


## Q1
# 연도를 입력으로 받아 윤년인지 아닌지를 출력하는 프로그램을 작성하시오.
# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.
# (예를들어, 2012년은 4의 배수라서 윤년이지만, 1900년은 4의 배수이지만, 100의 배수이기 때문에 윤년이 아니다.
# 하지만, 2000년은 400의 배수이기 때문에 윤년이다.)

def year_judge(year):
    if year % 400 == 0:
        print('윤년')
    elif year % 4 == 0 and year % 100 != 0:
        print('윤년')
    else:
        print('윤년이 아님')
        
year_judge(2012)
year_judge(1900)
year_judge(2000)



## Q2
# 상근이는 매일 아침 알람을 듣고 일어난다.
# 알람을 듣고 바로 일어나면 다행이겠지만, 항상 조금만 더 자려는 마음 때문에 매일 학교를 지각하고 있다.
# 상근이는 모든 방법을 동원해보았지만, 조금만 더 자려는 마음은 그 어떤 것도 없앨 수가 없었다.
# 이런 상근이를 불쌍하게 보던 창영이는 자신이 사용하는 방법을 추천해 주었다.
# 바로 "45분 일찍 알람 맞추기"이다.
# 이 방법은 단순하다. 원래 맞춰져 있는 알람을 45분 앞서는 시간으로 바꾸는 것이다.
# 어차피 알람 소리를 들으면, 알람을 끄고 조금 더 잘 것이기 때문이다.
# 이 방법을 사용하면, 매일 아침 더 잤다는 기분을 느낄 수 있고, 학교도 지각하지 않게 된다.
# 현재 상근이가 맞춰놓은 알람 시각을 입력으로 받아(시와 분) 창영이의 방법을 사용한다면,
# 이를 언제로 고쳐야 하는지 구하는 프로그램을 작성하시오.

hour, minute = map(int,input().split())
def wakeup(hour,minute):
    if minute >= 45:
        print(hour,':',minute-45)
    else:
        print(hour-1,':',minute+15)

wakeup(hour,minute)



## Q3
# 세 정수 a, b, c를 입력으로 받아 두 번째로 큰 정수를 출력하는 프로그램을 작성하시오.

aList = list(map(int,input().split()))

def bubble_sort(aList):
    for i in range(0, len(aList) - 1):
        for k in range(i + 1, len(aList)):
            if aList[i] > aList[k]: # 부등호 바뀌면 내림차순
                aList[i], aList[k] = aList[k], aList[i]
    print(aList[1])



## Q4
# 세 자연수 a, b, c 가 피타고라스 정리 a**2 + b**2 = c**2 를 만족하면 피타고라스 수라고 부른다.
# (여기서 a < b < c 이고 a + b > c)
# 예를 들면, 3**2 + 4**2 = 9 + 16 = 25 = 5**2 이므로 3, 4, 5는 피타고라스 수입니다.
# a + b + c = 1000 인 피타고라스 수를 구하시오. (답은 한가지 뿐이다.)

import random as rd

while True:
    a = rd.randint(1, 1000)
    b = rd.randint(1, 1000)
    c = 1000 - a - b
    if a < b < c and a + b > c and a**2 + b**2 == c**2 :
        print(a,b,c)
        break    # answer : 200, 375, 425
        
        

### 반복문


## Q1
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# 입력: 첫째 줄에 테스트 케이스의 개수 T를 입력받는다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다.(0 < A, B < 10)
# 출력: 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력한다.
# x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B이다.

import random as rd

n = 30
for i in range(n):
    A = rd.randint(1, 9)
    B = rd.randint(1, 9)
    C = A + B
    print('Case #',i+1,':',' ',A,'+',B,'=',C)



## Q2
# 5이상 9이하의 홀수를 입력받아 다이아몬드 형태의 별을 출력하는 프로그램을 작성하시오.
# 예) N=7
#              *
# 			  ***
# 			 *****
# 			*******
#            *****
# 			  ***
#              *

import math

# input 5
n = 5
for i in range(1, math.ceil(n / 2) + 1):
    for k in range(4 - i):
        print(' ', end='')
    for m in range(2 * i - 1):
        print('*', end='')
    for p in range(4 - i):
        print(' ', end='')
    print()
for i in range(0, math.ceil(n / 2) - 1):
    for s in range(i + 2):
        print(' ', end='')
    for t in range(n - 2 - 2 * i):
        print('*', end='')
    for u in range(i):
        print(' ', end='')
    print()

# input 7
n = 7
for i in range(1, math.ceil(n / 2) + 1):
    for k in range(4 - i):
        print(' ', end='')
    for m in range(2 * i - 1):
        print('*', end='')
    for p in range(4 - i):
        print(' ', end='')
    print()
for i in range(0, math.ceil(n / 2) - 1):
    for s in range(i + 1):
        print(' ', end='')
    for t in range(n - 2 - 2 * i):
        print('*', end='')
    for u in range(i):
        print(' ', end='')
    print()

# input 9
n = 9
for i in range(1, math.ceil(n / 2) + 1):
    for k in range(5 - i):
        print(' ', end='')
    for m in range(2 * i - 1):
        print('*', end='')
    for p in range(4 - i):
        print(' ', end='')
    print()
for i in range(0, math.ceil(n / 2) - 1):
    for s in range(i + 1):
        print(' ', end='')
    for t in range(n - 2 - 2 * i):
        print('*', end='')
    for u in range(i):
        print(' ', end='')
    print()



## Q3
# 디지털 시계에 하루동안(00:00~23:59) 3이 표시되는 시간을 초로 환산하면 총 몇 초(second)일까요?
# - 디지털 시계는 하루동안 다음과 같이 시:분(00:00~23:59)으로 표시됨.
# 00:00 (60초간 표시)
# 00:01
# …
# 23:59

sum_second = 0
for i in range(0,24):
    for k in range(0,60):
        clock = str(i) + str(k)
        if '3' in clock:
            sum_second += 60
print(sum_second)



## Q4
# 1~1000에서 각 숫자의 개수를 구하시오.
# - 예로 10 ~ 15 까지의 각 숫자의 개수를 구해보자.
# 10 = 1, 0
# 11 = 1, 1
# 12 = 1, 2
# 13 = 1, 3
# 14 = 1, 4
# 15 = 1, 5
# 그러므로 이 경우의 답은 0:1개, 1:7개, 2:1개, 3:1개, 4:1개, 5:1개

dict_num = dict(zip(map(str,range(0,10)),[0]*10))
for i in range(1,1001):
    str_i = str(i)
    for k in dict_num:
        if str(k) in str_i:
            dict_num[k] += str_i.count(str(k))
print(dict_num)



## Q5
# 자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
# 예를 들면, 6과 28은 완전수이다.
# 6=1+2+3         # 1,2,3은 각각 6의 약수
# 28=1+2+4+7+14   # 1,2,4,7,14는 각각 28의 약수.
# 입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 작성하시오.

N = int(input())
for i in range(1,N+1):
    sum1 = 0
    for k in range(1,i):
        if i % k == 0:
            sum1 += k
    if sum1 == i:
        print(i)



## Q6
# 1부터 10까지 자연수를 각각 제곱해 더하면 다음과 같다 (제곱의 합).
# 1**2 + 2**2 + ... + 10**2 = 385
# 1부터 10을 먼저 더한 다음에 그 결과를 제곱하면 다음과 같습니다 (합의 제곱).
# (1 + 2 + ... + 10)**2 = 552 = 3025
# 따라서 1부터 10까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 3025 - 385 = 2640 이 된다.
# 입력으로 자연수 N을 받아, 1부터 N까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마인가?

def difference(n):
    sum1 = 0
    sum2_1 = 0
    for i in range(1,n+1):
        sum1 += i**2
        sum2_1 += i
    sum2 = sum2_1**2
    print(abs(sum2-sum1))
difference(10)
difference(20)
    
        



        

