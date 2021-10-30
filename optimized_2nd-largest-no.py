import math
array = [6,1,2,8,3,4,7,10,5]
max = -math.inf
max_2 = -math.inf
index=0
while index < len(array):
  if array[index] > max :
    max_2 = max
    max = array[index]
  if array[index] > max_2 and array[index] < max: max_2 = array[index]
  index+=1
print(max_2)
