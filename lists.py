# # List -> Collection of non homogenous elements
# # List is mutable
# # List is ordered
# # List is indexed -> has both positive and negative index
# # List is iterable
# li = [1, "hello", 3.14, True, [11,22]]
# print(li)
# # Indexing
# li = [1,2,3,4,5,6,7,8,9,10]
# print(li[0])
# print(li[-1])
# print(li[-3])
# print(li[2])
# # Mutable
# print(li)
# li[3] = li[3]*100
# print(li)
# # Insertion
# li.append(100)
# print(li)
# li.insert(5,125)
# print(li)
# # Deletion
# li.pop()
# print(li)
# li.pop(5)
# print(li)
# li.remove(400)
# print(li)

# # Slicing -> Range Alike
# # Slice[start:end:step]
# print(li)
# print(li[3:]) # slice[start:]
# print(li[3:7]) # slice[start:end]
# print(li[:5]) # slice[:end]
# print(li[::2]) # slice[start:end:step]
# print(li[::-1]) # reverse

# # Iteration
# for i in li:
#     # i = i*10
#     print(i,end= " ")
# print()
# print(li)

# for i in range(len(li)):
#     li[i] = li[i]*10
#     print(li[i],end = " ")
# print()
# print(li)

# li = [1,2,3]
# li2 = li+li
# print(li2)
# li3 = li*3
# print(li3)

# # Shallow Copy 
# li = [1,2,3,4]
# li2 = li
# print(li)
# print(li2)
# li2[0] = 100
# print(li)
# # Deep Copy
# li2 = li.copy()
# li2[0] = 999
# print(li)
# print(li2)
li=['sasi','priya']
print(li)
li2=li.copy()
li2.append('sasi')
print(li)
li3=li
li3.append('1')
print(li)
