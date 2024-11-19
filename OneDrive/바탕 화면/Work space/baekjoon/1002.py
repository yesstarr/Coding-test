#조-류, 백-류, 조-백 과의 거리를 통해 판단.
#만약 조-류 + 백-류 가 조-백의거리랑 같다면 1 조-백 거리보다
#작다면 0 조-백 거리보다 크다면 2 즉, 두 점 사이의 공식 3번
import math
test = int(input())
result = 0
for i in range(test):
    x_1,y_1,r_1,x_2,y_2,r_2 = map(int,input().split())
    a_1 = pow(x_2-x_1,2) #A-B의 x제곱
    b_1 = pow(y_2-y_1,2) #A-B의 y제곱
    atob = math.sqrt(a_1 + b_1) # 조-백,r_1은 조-류,백-류는 r_2
    if atob == r_1+r_2 or(atob != 0 and atob == abs(r_1 - r_2)): #내접
        result = 1
        print(result)
    elif atob > r_1 + r_2 or atob < abs(r_1-r_2):
        result = 0
        print(result)
    elif atob == 0 and r_1 == 0:
        result = 1
        print(result)
    elif atob == 0 and r_1 == r_2:
        result = -1
        print(result)
    else:
        result = 2
        print(result) 