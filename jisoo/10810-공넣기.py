N, M = map(int, input().split()) 
b_list = [0 for _ in range(N)]

for _ in range(M) : #M번 입력값 받음
    i, j ,k = map(int, input().split())
    for n in range(i,j+1):
        b_list[n-1] = k

for n in range(N) : 
    print(b_list[n],end=' ')


