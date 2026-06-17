li=input().split(" ")
l_sum=0
r_sum=0
re=[]
# print(li)
for i in range(0,len(li)):
  l_sum=0
  r_sum=0
  for j in range(i):
    l_sum+=int(li[j])
  for j in range(i+1,len(li)):
    r_sum+=int(li[j])
  diff=abs(r_sum-l_sum)
  re.append(diff)
print(re)