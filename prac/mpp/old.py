#
#in: x.2 = x.1^2\nx.1 = x.2^2\nX0
#   split \n
#   X0 v formate (x.1,x.2)
#
#   fun perenosa
#       find =
#       s[:]+"-"+s[:]+"=0"
#   =>F(X)=0  <-f1(x.1,x.2); f2(x.1,x.2)
#
#   fun dif_str_x.i
#     |  for j in range(1,2):
#           find("x."+str(j)) -> smotrim stepen1 (iz rascheta polinomial1n func) -> proizv rucami cherez "n"+s[:]+"^n-1"+s[:]
#     |  find +     find -
#           rucami proiz cherez "n"+s[:]+"^n-1"+s[:]
#     |  split - + = 
#           for elem in list:
#               elem = diff_str(elem,x.i)
#           for elem in list:
#               s = s+elem
#   => posledni1 variant best
#
#   diff_str(elem,x.i):
#      ii = x.i[2]
#      for j in range(1,2):
#           if j==ii:
#              find x.j
#              proizvodnuu berem
#           else:
#               if find x.j
#                   zamenyaem nulem
#               else: pass
#   => df1/ dx.1; df1/dx.2; i tak dalee 
#
#   isdetequalzero(df1/dx.1, ...)
#       ad-bc == 0 -> T | F
#   => F -> F(x) vsegda virozdena (det = 0 v luboi tochke) 
#
#   isdetequalzerodlyaX0(df1/dx.1, ...,x0)
#       ad-bc == 0 -> T | F
#   => F -> virozdena v tochke
#
# Теперь можно решать задачу Коши для 
#   dx/dm = -([dF/dx]^-1)*F(X0)
#       m время от 0 до n  x(m)  F(x(m))
#

from math import sin,cos
import re#split
from sympy import integrate, Symbol 

def perenos(s):
    a = s.find("=")
    if s[a+1]==0:
        return s
    return s[:a]+"-"+s[a+1:]+"=0"

def diff_str(e,xi):#элемент полинома как стр и по чему производим
    e = e.strip()
    try:
        e = int(e)
        return "0"
    except:
        pass
    if e[:3]=="sin": return "cos"+e[3:]
    if e[:3]=="cos": return "-sin"+e[3:]
    a = e.find(xi)
    if a==-1:   return "0"
    b = e.find("^")
    if b==-1:   return "1"
    try:
        be = int(e[b+1:])
    except:
        print("strashnaya stepen1")
        return "aaaa"
    #print(be)
    if e[0]=="-": return "-" + str(be) +"*"+ e[1:b] +"^"+str(be-1)
    else: return str(be) +"*"+ e[:b] +"^"+str(be-1)
    raise "heyya"

def concatforeval(list):
    s = ""
    for iii,elem in enumerate(list):
        if elem == "0":
            continue
        if iii==0:
            s = elem
        else:
            if elem[0]=="-": s=s+elem
            else:
                s = s+"+"+elem
    return s

def raisetominusone(list):
    for iii,elem in enumerate(list):
        if elem=="0":
            continue
        a = elem.find("^")
        b = elem.find("x")
        if a != -1:
            try:
                ba = int(elem[a+1:])
            except:
                print("panic in ^-1")
            if ba == 1:
                list[iii]=elem[:b]
                if list[iii][-1]=="*":
                    list[iii] = list[iii][:-1]
                continue
        list[iii] = "("+elem+")"+"^(-1)"
    return list

f1 = input().replace("= ","=")
f2 = input().replace("= ","=")
X0 = list(eval(input()))
print(f1,f2,X0)

f1 = perenos(f1).replace("-","~-").replace("+","`")
f2 = perenos(f2).replace("-","~-").replace("+","`")
print(f1,f2,X0)

f1list = re.split("`|~|=",f1)
f2list = re.split("`|~|=",f2)
print(f1list,f2list,X0)

#заношу производные по переменным в списки
f1listx1=[0 for _ in f1list]
f1listx2=[0 for _ in f1list]
f2listx1=[0 for _ in f2list]
f2listx2=[0 for _ in f2list]
for iii,elem in enumerate(f1list):
    f1listx1[iii] = diff_str(elem,"x1")
    f1listx2[iii] = diff_str(elem,"x2")
for iii,elem in enumerate(f2list):
    f2listx1[iii] = diff_str(elem,"x1")
    f2listx2[iii] = diff_str(elem,"x2") 
print(f1listx1,f1listx2,f2listx1,f2listx2)
#print(diff_str(" 6*x1^6 ","x1"))

def isdetequalzero(f1x1,f1x2,f2x1,f2x2):#детерминант равен нулю без начальных условий (вроде не надо)
    #сравнить f1x1 f2x1 и f1x2 f2x2   -или-   f1x1 f2x2 и f1x2 f2x1
    if f1x1 == f2x1 and f1x2 == f2x2: return     True
    if f1x1 == f2x2 and f1x2 == f2x1: return     True
    return False

f1x1nonpowerone = concatforeval(f1listx1)
f1x2nonpowerone = concatforeval(f1listx2)
f2x1nonpowerone = concatforeval(f2listx1)
f2x2nonpowerone = concatforeval(f2listx2)
print(f1x1nonpowerone,f1x2nonpowerone,f2x1nonpowerone,f2x2nonpowerone)
if isdetequalzero(f1x1nonpowerone,f1x2nonpowerone,f2x1nonpowerone,f2x2nonpowerone): print("syst virozdena")

f1x1 = concatforeval(raisetominusone(f1listx1))
f1x2 = concatforeval(raisetominusone(f1listx2))
f2x1 = concatforeval(raisetominusone(f2listx1))
f2x2 = concatforeval(raisetominusone(f2listx2))
print(f1x1,f1x2,f2x1,f2x2)

print(X0)
X0[0] = "("+str(X0[0])+")"
X0[1] = "("+str(X0[1])+")"
f1x1_0 = f1x1.strip().replace("^","**")
f1x2_0 = f1x2.strip().replace("^","**")
f2x1_0 = f2x1.strip().replace("^","**")
f2x2_0 = f2x2.strip().replace("^","**")
f1_00 = f1.replace("~","").replace("`","+").replace(" ","").strip().replace("^","**")[:-2]
f2_00 = f2.replace("~","").replace("`","+").replace(" ","").strip().replace("^","**")[:-2]
print(f1x1_0,f1x2_0,f2x1_0,f2x2_0,f1_00,f2_00)

f1_0 = eval(f1_00.replace("x1",X0[0]).replace("x2",X0[1]))
f2_0 = eval(f2_00.replace("x1",X0[0]).replace("x2",X0[1]))
try:
    f1x1_0 = eval(f1x1_0)
    f1x2_0 = eval(f1x2_0)
    f2x1_0 = eval(f2x1_0)
    f2x2_0 = eval(f2x2_0)
except:
    print("ne yprostilos1")
    pass
print(f1x1_0,f1x2_0,f2x1_0,f2x2_0,f1_0,f2_0)

def isdetequalzeroX0(f1x1,f1x2,f2x1,f2x2,X0):#virozden li determ v to4ke
    pass

#from sympy import integrate
#>>> from sympy import Symbol   
#>>> x = Symbol('x')
#>>> integrate(x**2+x+1,x) 
#x**3/3 + x**2/2 + x
#>>> integrate(((-3*x**2)**(-1)),x) 
#1/(3*x)

x1 = Symbol('x1')
x2 = Symbol('x2')
#print(integrate(f1x1_0,x1),str(integrate(f1x1_0,x1)))
f1x1_0 = str(integrate(f1x1_0,x1))
f1x2_0 = str(integrate(f1x2_0,x2))
f2x1_0 = str(integrate(f2x1_0,x1))
f2x2_0 = str(integrate(f2x2_0,x2))
print("f1/x1 f1/x2  f2/x1  f2/x2  //b-a^2 a-b^2")
print(f1x1_0,f1x2_0,f2x1_0,f2x2_0,f1_0,f2_0)

#f1_0 f2_0 <- m
#f1x1_0,f1x2_0,f2x1_0,f2x2_0 = const
x1_ot_m = "-1 *("+str(f1_0)+")*(("+str(f1x1_0)+")+("+str(f1x2_0)+"))"
x2_ot_m = "-1 *("+str(f2_0)+")*(("+str(f2x1_0)+")+("+str(f2x2_0)+"))"
print("x1 = ",x1_ot_m)
print("x2 = ",x2_ot_m)
