H, M = map(int,input().split())

if M >= 45 :
    if H == 0:
        M -= 45
        print(H,M)
    else :
        M = M-45
        print(H,M)
else :
    if H ==0:
        H = 23
        M = M+15
        print(H,M)
    else:
        H = H-1
        M = M+15
        print(H,M)