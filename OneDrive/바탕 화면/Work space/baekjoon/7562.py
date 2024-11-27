#7562
class TreeNode:
    def __init__(self, x, y, level):
        self.x = x
        self.y = y
        self.level = level
        self.children = []

def create_knight_tree(chess_size, start, target):#start_x,start_y , target_x,target_y 반환
    directions = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    root = TreeNode(start[0], start[1], 0)  # 스타트 지점으로 루트 생성
    visited = [[False] * chess_size for _ in range(chess_size)]#방문 배열 생성 후 모든 칸 FALSE 로 설정
    visited[start[0]][start[1]] = True

    queue = [root]  # BFS 탐색 큐, 어펜드나 팝같은 문법 사용할려고 리스트로 설정
    while queue:#큐가 빌때까지 반복문 진행
        current_node = queue.pop(0)#pop한 값
        
        # 목표 위치에 도달하면 층 반환
        if (current_node.x, current_node.y) == target:
            return current_node.level

        # 현재 칸 기준으로 갈 수 있는 모든 방향인 8방향으로 확장
        for dx, dy in directions:
            nx, ny = current_node.x + dx, current_node.y + dy
            #방문하지 않았으면서 체스판 내에 있는 경우
            if 0 <= nx < chess_size and 0 <= ny < chess_size and not visited[nx][ny]:
                child = TreeNode(nx, ny, current_node.level + 1)
                current_node.children.append(child)  # 자식노드로 추가
                queue.append(child)  # 큐에 추가
                visited[nx][ny] = True#방문한걸로 바꿈
    
    return -1  # 목표에 도달할 수 없는 경우

# 입력 처리
test_case = int(input())
for _ in range(test_case):
    chess_size = int(input())
    start_x, start_y = map(int, input().split())
    target_x, target_y = map(int, input().split())
    
    # 트리 생성 및 탐색
    result = create_knight_tree(chess_size, (start_x, start_y), (target_x, target_y))
    print(result)