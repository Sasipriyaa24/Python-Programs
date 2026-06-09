def fibo(n):
  temp1=0
  temp2=1
  for i in range(n-2):
    temp3=temp1+temp2
    temp1=temp2
    temp2=temp3
  return temp3
print(fibo(5))