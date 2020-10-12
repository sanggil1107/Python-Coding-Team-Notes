## Python Sort ##
data = [7, 5, 1, 9, 4]
data.sort()

for x in data:
  print(x)


## Python Sort(Key) ##
data = [(30, 'Yang'), (20, 'Dim'), (23, 'Aeo'), (28, 'Park'), (20, 'Choi')]
data.sort(key=lambda x: x[0])

for x in data:
  print(x)


## Python Sort(not Key) ##
data = [(30, 'Yang'), (20, 'Dim'), (23, 'Aeo'), (28, 'Park'), (20, 'Choi')]
data.sort()

for x in data:
  print(x)

