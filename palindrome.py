str=input()
left=0
palindrome=True
right=len(str)-1
while left<right:
  if str[left]==str[right]:
    left+=1
    right-=1
  else:
    palindrome=False
    break
if palindrome:
  print("palindrome")
else:
  print("Not a palindrome")
