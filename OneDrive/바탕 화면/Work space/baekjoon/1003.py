def fibo(N):
    if N in memo:
        count[0] += memo[N][0]
        count[1] += memo[N][1]
    else:
        fibo(N-1) 
        fibo(N-2)
    memo[N] = (count[0],count[1])
cnt = int(input())
for i in range(cnt):
    count = [0,0]#0은 0의개수 1 은 1의 개수
    memo = {0 : (1,0), 1: (0,1)}
    #딕셔너리로 0이라는 키에 (1,0)이라는 튜플을 집어 넣은 것
    N = int(input())
    fibo(N)
    print(count[0],count[1])
    #피보나치 같은 것들은 N값이 커질수록 계산량이 많아지므로
    #메모제이션 기법을 이용하여 미리 값들을 기억함.
