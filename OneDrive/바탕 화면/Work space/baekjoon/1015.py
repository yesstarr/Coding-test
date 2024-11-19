# #0,0칸이 흰색이냐 검적생이냐
# #0,0칸이 흰색이면 합이 짝수인 것은 모두 다 흰색이여야함. 
# #10칸이면 3번 11칸이면4번 즉 a-7,b-7해서 몇번할지 반복문 돌림
# #각 반복문끼리 몇개 그건지 구해서 최소값 찾아야함.


y, x = map(int, input().split())  
board = []

for _ in range(y):  # 전체 보드판 입력
    row = input().strip()  
    board.append(list(row[:x]))  

rows = len(board)
cols = len(board[0])
chess_size = 8
rep_x = cols - chess_size + 1
rep_y = rows - chess_size + 1

minimum = 64  

# 체스판 리스트 내포를 통한 형성
for start_y in range(rep_y):
    for start_x in range(rep_x):
        cnt1 = 0  # 'W'로 시작하는 경우의 색칠 수
        cnt2 = 0  # 'B'로 시작하는 경우의 색칠 수
        
        for y in range(chess_size):
            for x in range(chess_size):
                current_color = board[start_y + y][start_x + x]
                if (x + y) % 2 == 0:  # 짝수 칸
                    if current_color != 'W':
                        cnt1 += 1
                    if current_color != 'B':
                        cnt2 += 1
                else:  # 홀수 칸
                    if current_color != 'B':
                        cnt1 += 1
                    if current_color != 'W':
                        cnt2 += 1
        
        minimum = min(minimum, cnt1, cnt2)

print(minimum)
