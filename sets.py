s1 = set()
s2 = set((1,2,3))
s3 = {"1",2,3}
print(type(s1))
print(s2,type(s2))
print(s3,type(s3))
s = {"naga","sai",123,32.45,"hello"}
print(s)
s.add(99)
print(s)
s.remove(99)
print(s)
s.discard(567890)
print(s)
s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)