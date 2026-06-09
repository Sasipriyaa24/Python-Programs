li=[1,34,55,23,34,86,55,12,28,86]
dupli=set()
for i in li:
    if i in dupli:
        dupli.add(i)
      
    else:
        print(i) 
