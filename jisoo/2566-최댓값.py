for i in range(9):
    tem = list(map(int, input().split()))

    if i == 0:
        max_value = max(tem)
        row = i + 1
        col = tem.index(max_value) + 1

    else:
        if max_value < max(tem):
            max_value = max(tem)
            row = i + 1
            col = tem.index(max_value) + 1

print(max_value)
print(row, col)