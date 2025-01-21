#1004
import math
test_case = int(input())
for _ in range(test_case):
    cnt = 0
    
    start_x,start_y,dest_x,dest_y = map(int,input().split())
    cir_cnt = int(input())
    for i in range(cir_cnt):
        cir_x,cir_y,cir_r = map(int,input().split())
        cir_rr= cir_r*cir_r
        start_point = ((start_x-cir_x)*(start_x-cir_x) + (start_y-cir_y)* (start_y-cir_y))
        dest_point = ((dest_x-cir_x)*(dest_x-cir_x) + (cir_y-dest_y *cir_y-dest_y))
        #원과 원 사이의 관계
        #1.원과 원이 맞닿아 있는 경우 r1+r2 = 중점 사이 거리  -
        #2.원과 원이 겹쳐있는 경우 r1+r2 > 중점 사이 거리
        #3.원과 원이 닿지 않는 경우 r1+r2 < 중점 사이 거리

        #경우의 수 1.출발지와 목적지가 어느 원에도 속해 있지 않은 경우 2.출발지와 목적지가 특정 원에 속해 있는경우
        #조금 더 확실하게 원 안에 있는지 체크할려면 원의 방정식을 생각해야해 
        #ㅋㅋ... 원의 방정식도 제대로 모르누,,,,
        #범위 설정
        # 1. cnt = 0
        # 1-1 하나의 원 안에 출발지와 도착지 둘 다 있는 경우
        if start_point < cir_rr and dest_point < cir_rr :
            continue
        # 1-2 둘 다 원 안에 들어가있지 않은 경우
        if start_point > cir_rr and dest_point > cir_rr :
            continue
        
        #2. cnt +=1
        #하나의 원 안에 출발점과 목적지 둘 다 있는 경우를 생각해야함. 서로 같은 원 안에 있으면 continue, 그렇지 않다면 +=1
        if start_point < cir_r*cir_r and dest_point > cir_r*cir_r :
            cnt +=1
        if start_point > cir_r*cir_r and dest_point < cir_r*cir_r:
            cnt += 1

    print(cnt)
    