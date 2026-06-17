class A:
    a_val = 10
    def a_method(self):
        print("I am method of Class A")
# Single Inheritance
class B(A):
    b_val = 20
    def b_method(self):
        print("I am method of Class B")
# Multi-level Inheritance
class C(B):
    c_val = 30
    def c_method(self):
        print("I am method of Class C")
class D:
    d_val = 40
    def d_method(self):
        print("I am method of Class D")
# Muliple inheritance
class E(A,D):
    e_val = 50
    def e_method(self):
        print("I am method of Class E")
# Hierarchial Inheritance
class F(A):
    f_val = 60
    def f_method(self):
        print("I am method of Class F")
# Hybrid Inheritance
class G(E,C):
    g_val = 70
    def g_method(self):
        print("I am method of Class G")



a_obj = A()
print("Accessing A Class Props with A Obj")
print(a_obj.a_val)
a_obj.a_method()

print("Single Inheritance")
b_obj = B()
print("Accessing B Class Props with B Obj")
print(b_obj.b_val)
b_obj.b_method()
print("Accessing the A calss Props woth B Obj")
b_obj.a_method()
print(b_obj.a_val)

print("Multilevel inheritance")
c_obj = C()
print("Accessing C Class Props with C Obj")
print(c_obj.c_val)
c_obj.c_method()
print("Acessing The A,B class With C OBJ")
c_obj.b_method()
print(c_obj.b_val)
c_obj.a_method()
print(c_obj.a_val)

print("Multiple Inheritance")
e_obj = E()
e_obj.a_method()
e_obj.d_method()

print("Hierarchial Inheritance")
f_obj = F()
f_obj.a_method()

print("Hybrid Inheritance")
g_obj = G()
g_obj.a_method()
g_obj.b_method()
g_obj.c_method()
g_obj.d_method()
g_obj.e_method()
