## 삽입 정렬 ##
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(data)):
  for j in range(i, 0, -1): # i부터 1까지 1씩 감소
    if data[j] < data[j - 1]:
      data[j], data[j - 1] = data[j - 1], data[j]
    else:
      break

print(data)