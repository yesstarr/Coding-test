#15828
#host -> router...-> 목적지
#라우터 내부(버퍼)에서 패킷이 들어온 순서대로 처리
#속도가 감당 안되면 터짐. 모든 패킷 버려짐
#첫째줄에는 버퍼의 크기, 0은 패킷 처리, -1은 입력끝
#FIFO구조
from queue import Queue

queue_size = int(input())
queue = Queue()
while 1:
    user_input = input()
    if user_input == "-1":
        if queue.empty():
            print("empty")
        for i in range(queue.qsize()):
            print(queue.queue[i],end = " ")
        break
    elif user_input == "0":
        if not queue.empty():
            queue.get() 
    elif queue_size <= queue.qsize():
        while queue.qsize() == "1":
            queue.get() 
    else:
        queue.put(user_input)        
#-----------------------------------
#시간 복잡도 문제로 deque 사용
from collections import deque

queue_size = int(input())
queue = deque()
while 1:
    if user_input == "-1":
        if not queue:
            print("empty")
        else:
            print(" ".join(map(str,queue)))
        break
    elif user_input == "0":
        if queue:
            queue.popleft()
    else:
        packet = int(user_input)
        if len(queue) < queue_size:
            queue.append(packet)        
