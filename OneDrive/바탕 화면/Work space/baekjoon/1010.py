count = int(input())


# mCn,m!/(m-n)!n! 각각 m!과 n! (m-n)!을 구하고 나누자
facto_N = 1
facto_M = 1
facto_MN = 1
for i in range(count):
    N,M = map(int,input().split())
    for i in range(1,N+1,1):
        facto_N *= i
    for i in range(1,M+1,1):
        facto_M *= i
    for i in range(1,(M-N)+1,1):
        facto_MN *= i
    result = facto_M//(facto_N*facto_MN)
    print(result)
    facto_N = 1
    facto_M = 1
    facto_MN = 1
    N = 0
    M = 0


