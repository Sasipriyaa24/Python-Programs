password=input()
if len(password)>=8 and password.isdigit and password.isupper and password.islower and password.isidentifier and password.isspace:
  print("Valid")
else:
  print("Invalid")