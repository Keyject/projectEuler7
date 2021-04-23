# euler 7
# KeyJect
import math
def isPrime(num):
  for i in range(2 , int(math.sqrt(num)+1)):
    if num%i==0:
      return False
  return True

i=1
count = 0
goal = 10001
while True:
  i+=1
  if isPrime(i):
    count+=1
  if count==goal:
    print(i)
    break