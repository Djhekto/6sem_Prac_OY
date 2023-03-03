from math import sin,cos
from sympy import integrate, Symbol, diff, expand
import numpy as np
from matplotlib import pyplot as plt
#from numpy.linalg import matrix_power
#from numpy import array as nparray

def perenosubravnol1(s):
    a = s.find("=")
    if s[a+1]==0:
        return s
    return s[:a]+"-"+s[a+1:]#+"=0"

def enc(str1):
    return "(" + str1 + ")"

def main():
    f1 = input().replace("= ","=")
    f2 = input().replace("= ","=")
    X0 = list(eval(input()))
    f1 = perenosubravnol1(f1).replace(" ","").replace("^","**")
    f2 = perenosubravnol1(f2).replace(" ","").replace("^","**")
    print(f1,f2,X0)

    dx1 = Symbol("x1")
    dx2 = Symbol("x2")

    df1x1 = str(diff(f1,dx1))
    df1x2 = str(diff(f1,dx2))
    df2x1 = str(diff(f2,dx1))
    df2x2 = str(diff(f2,dx2))
    print(df1x1,df1x2,df2x1,df2x2)

    matrix1 = np.array([[df1x1,df1x2],[df2x1,df2x2]])
    print(matrix1)
#    print(np.linalg.matrix_power(matrix1,-1))

    # [[a b] [c d]] -1  =  1/(ab-cd) [d -b] [-c a]
    #? ad != bc
    #
    const_koef = "(-1) /" +enc(enc(df1x1)+"*"+ enc(df2x2)+"-"+enc(df1x2)+"*"+enc(df2x1))
    print(const_koef,expand(const_koef),sep = "  =>  ")
    const_koef = str(expand(const_koef))
    
    f1x1 = enc(const_koef)+"*"+df1x1
    f1x2 = enc(const_koef)+"*"+df1x2
    f2x1 = enc(const_koef)+"*"+df2x1
    f2x2 = enc(const_koef)+"*"+df2x2
    print(f1x1,f1x2,f2x1,f2x2)
    
    constx1 = str(expand( enc(f1x1) +"+"+enc(f1x2) ))
    constx2 = str(expand( enc(f2x1) +"+"+enc(f2x2) ))
    print(constx1,"        ",constx2)
    
    constf1 = f1#.replace("x2","b").replace("x1","a")
    constf2 = f2#.replace("x2","b").replace("x1","a")
    print(constf1,constf2)
    
    fx1 = str(expand(enc(constx1)+"*"+enc(constf1)))
    fx2 = str(expand(enc(constx2)+"*"+enc(constf2)))    
    print(fx1,fx2)
    
    x1_ = X0[0]
    x2_ = X0[1]
    print(x1_,x2_)
    
    test = fx1.replace("x1",str(x1_)).replace("x2",str(x2_))
    test1= fx2.replace("x1",str(x1_)).replace("x2",str(x2_))
    print(test,eval(test),eval(test1))
    x1_list = []
    x2_list = []
    vremya = [t/100 for t in range(1000) ]
    for m in vremya:
        if x2_ > 100 or x1_ > 100: break
        try: 
            x1_c = x1_
            x1_+=eval(fx1.replace("x1",str(x1_)).replace("x2",str(x2_)))*0.01
            x2_+=eval(fx2.replace("x1",str(x1_c)).replace("x2",str(x2_)))*0.01
            x1_list.append(x1_)
            x2_list.append(x2_)
            print("(  ",x1_,"  ;  ",x2_,"  )")
        except:
            break

    plt.plot(x1_list,x2_list)
    plt.show()




"""
    df1x1 = expand(df1x1**(-1))
    df1x2 = expand(df1x2**(-1))
    df2x1 = expand(df2x1**(-1))
    df2x2 = expand(df2x2**(-1))
    print(df1x1,df1x2,df2x1,df2x2)

    df1x1 = integrate(df1x1,dx1)
    df1x2 = integrate(df1x2,dx2)
    df2x1 = integrate(df2x1,dx1)
    df2x2 = integrate(df2x2,dx2)
    print(df1x1,df1x2,df2x1,df2x2)
"""

main()