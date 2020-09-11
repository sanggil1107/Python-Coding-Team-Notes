
data = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(data)):
  min_index = i
  for j in range(i + 1, len(data)):
    if data[min_index] > data[j]:
      min_index = j
  data[i], data[min_index] = data[min_index], data[i]

print(data)