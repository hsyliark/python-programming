### Unit 30~32

def print_numbers(a, b, c):
    print(a)
    print(b)
    print(c)
print_numbers(10, 20, 30)

# unpacking
x = [10, 20, 30]
print_numbers(*x)
print_numbers(*[10, 20, 30])
print_numbers(*[10, 20]) # error

# 가변 인수 함수
def print_numbers(*args):
    for arg in args:
        print(arg)
print_numbers(10,20,30,40)
x = [10,20,30,40]
print_numbers(*x)

def print_numbers(a, *args):
    print(a)
    print(args)
print_numbers(1)
print_numbers(1,10,20)
print_numbers(*[10,20,30])

# 키워드 인수
def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')

# dictionary unpacking
x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)

def personal_info(**kwargs):
    for kw, arg in kwargs.items():
        print(kw, ': ', arg, sep='')
personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
x = {'name':'홍길동', 'age':30, 'address':'서울시 용산구 이촌동'}
personal_info(**x)

def personal_info(**kwargs):
    if 'name' in kwargs:
        print('이름: ', kwargs['name'])
    if 'age' in kwargs:
        print('나이: ', kwargs['age'])
    if 'address' in kwargs:
        print('주소: ', kwargs['address'])

# 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
def personal_info(name, **kwargs):
    print(name)
    print(kwargs)
personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})

# 위치 인수와 키워드 인수를 함께 사용하기
def custom_print(*args, **kwargs):
    print(*args, **kwargs)
custom_print(1, 2, 3, sep=':', end='')

def personal_info(name, age, address='비공개'): # 초깃값 설정 변수는 뒤쪽에 몰아주기
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)
personal_info('홍길동', 30)
personal_info('홍길동', 30, '서울시 용산구 이촌동')


## 재귀호출(recursive call)

def hello():
    print('Hello, world!')
    hello()
hello() # Recursion error

def hello(count):
    if count == 0:
        return
    print('Hello, world!',count)
    count -= 1
    hello(count)
hello(5)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

def is_palindrome(word):
    if len(word) < 2:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome(word[1:-1])
print(is_palindrome('hello'))
print(is_palindrome('level'))


## 익명함수 (lambda expression)

def plus_ten(x):
    return x + 10
plus_ten(1)
lambda x: x + 10

plus_ten = lambda x: x + 10
plus_ten(2)

(lambda x: x + 10)(1)
(lambda x: y = 10; x + y)(1) # error
y = 10
(lambda x: x + y)(1)

def plus_ten(x):
    return x + 10
list(map(plus_ten, [1,2,3]))
list(map(lambda x: x + 10, [1,2,3]))

# map, filter, reduce
a = list(range(1,11))
list(map(lambda x: str(x) if x % 3 == 0 else x, a)) # 반드시 else 구문 추가
list(map(lambda x: str(x) if x % 3 == 0, a)) # error
list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
def f(x):
    if x == 1:
        return str(x)
    elif x == 2:
        return float(x)
    else:
        return x + 10
list(map(f, a))

a = [1,2,3,4,5]
b = [2,4,6,8,10]
list(map(lambda x, y: x * y, a, b))

def f(x):
    return x > 5 and x < 10
a = [8,3,2,10,15,7,1,9,0,11]
list(filter(f, a))
a = [8,3,2,10,15,7,1,9,0,11]
list(filter(lambda x: x > 5 and x < 10, a))
a = [8,3,2,10,15,7,1,9,0,11]
[i for i in a if i > 5 and i < 10]

def f(x, y):
    return x + y
a = [1,2,3,4,5]
from functools import reduce
a = [1,2,3,4,5]
reduce(f, a)
a = [1,2,3,4,5]
reduce(lambda x, y: x + y, a)
a = [1,2,3,4,5]
x = a[0]
for i in range(len(a) - 1):
    x = x + a[i + 1]
x




