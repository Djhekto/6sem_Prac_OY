import sys
from math import sin,cos
from sympy import Symbol, diff, expand
from pyray import *
import raylib

def enc(str1):
    if type(str1)!=type("a"):        str1 = str(str1)
    return "(" + str1 + ")"

def str_mul(str1,str2):
    return str1 + "*" + enc(str2)

def reverse_2D_strfun_Matrix(df1x1,df1x2,df2x1,df2x2):
    # [[a b] [c d]] -1  =  1/(ad-bc) [d -b] [-c a]
    #// ad != bc |x1=.. x2=..
    #https://math.stackexchange.com/questions/3835371/does-it-make-sense-to-define-the-inverse-of-a-matrix-of-functions
    str_k = "(-1) /" +enc(enc(df1x1)+"*"+ enc(df2x2)+"-"+enc(df1x2)+"*"+enc(df2x1)) 
    return str_mul(str_k,df2x2),str_mul(str_k,"-"+df1x2),str_mul(str_k,"-"+df2x1),str_mul(str_k,df2x2)

def pravayachast1(s):
    a = s.find("=")
    if a==-1:        return s
    return s[a+1:]

def trytogetridofquestions(symbols,symbols_with_clear_ab,yslovia,strfunlist,a,b):
    print(symbols,symbols_with_clear_ab,yslovia,strfunlist,a,b)
    yslovia1 = yslovia
    ind_knownsymb = [a for a,b in symbols_with_clear_ab]
    ind_badsymb = [a for a,b in symbols if [a,b] not in symbols_with_clear_ab]
    print(ind_knownsymb,ind_badsymb, sep = "  ;; ; ; ;; ;  ")
    
    print(yslovia1,strfunlist)
    for ii in ind_badsymb:
        yslovia1[ii][0] = strfunlist[ii].replace("t",enc(a))
        yslovia1[ii][1] = strfunlist[ii].replace("t",enc(b))
        for kk in ind_knownsymb:
            yslovia1[ii][0] = yslovia1[ii][0].replace(symbols[kk][1],enc(yslovia[kk][0]))
            yslovia1[ii][1] = yslovia1[ii][1].replace(symbols[kk][1],enc(yslovia[kk][1]))

    return yslovia1

def trytoevalyslovia(yslovia):
    for i,list1 in enumerate(yslovia):
        for ii,elem in enumerate(list1):
            yslovia[i][ii] = eval(elem)
    return yslovia

def euler4D_twodirections(symbols,yslovia,strfunlist,a,b,tz,ppp,shag=0.1):
    list4d_tocki_vlevo = []
    list4d_tocki_vpravo = []
    list4d_tocki_vlevo.append(ppp)
    list4d_tocki_vpravo.append(ppp)
    
    print(symbols,yslovia,strfunlist,a,b,tz,ppp,shag)
    
    i=0
    tz_vlevo = eval(tz)
    while tz_vlevo>a:
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vlevo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vlevo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vlevo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vlevo.append(list_append_me)
        tz_vlevo -= shag
        i+=1
        for chislo in list4d_tocki_vlevo[i]:
            if abs(chislo)>=100000:
                tz_vlevo = a

    #print("\n",list4d_tocki_vlevo)
        
    i=0
    tz_vpravo = eval(tz)
    while tz_vpravo<b:
        list_append_me = []
        for ii in range(4):
            new_dot = strfunlist[ii].replace("t",enc(tz_vpravo))
            for ind,symb in symbols:
                new_dot = new_dot.replace(symb,enc(list4d_tocki_vpravo[i][ind]))
            list_append_me.append(eval(enc(list4d_tocki_vpravo[i][ii])+"+"+str_mul(new_dot,shag)))
        list4d_tocki_vpravo.append(list_append_me)
        tz_vpravo += shag
        i+=1
        for chislo in list4d_tocki_vpravo[i]:
            if abs(chislo)>=100000:
                tz_vpravo = b
    #print("\n",list4d_tocki_vpravo)

#>>> a = [4,3,2,1] 
#>>> b = [4,5,6,7] 
#>>> c = reversed(a)  
#>>> list(c)[:-1]+b  
#[1, 2, 3, 4, 5, 6, 7]
    list4d_tocki = list(reversed(list4d_tocki_vlevo))[:-1]+list4d_tocki_vpravo
    return list4d_tocki

def main():
    fullinput = sys.stdin.readlines()
    for ii,elem in enumerate(fullinput):
        fullinput[ii] = pravayachast1(elem.replace(" =","=").replace("= ","=").replace("\n","").replace("^","**"))
    print(fullinput)
    strfunlist = fullinput[0:3+1]
    print("syst\n",strfunlist,sep="  ,  ")
    yslovia = [fullinput[4:6],fullinput[6:8],fullinput[8:10],fullinput[10:12]]
    print(yslovia)
    a,b = eval(fullinput[12])
    print("time\n",a,b)
    tz = fullinput[13]
    print("t*=",tz)
    ppp = eval(fullinput[14])
    print("guess",ppp)
    symbols = []
    for ii,elem in enumerate(fullinput[15].split(",")):
        symbols.append([ii,elem])
    print("symbols",symbols)
    symbols_with_clear_ab = []
    for iii,list1 in enumerate(yslovia):
        if list1[0]!="?" and list1[1]!="?": symbols_with_clear_ab.append(symbols[iii])
    print("s ab",symbols_with_clear_ab)
    yslovia = trytogetridofquestions(symbols,symbols_with_clear_ab,yslovia,strfunlist,a,b)
    print(yslovia)
    yslovia = trytoevalyslovia(yslovia)
    print(yslovia, "  v  ",a,b)
    print(ppp," v ",tz)
    list4d_tocki = euler4D_twodirections(symbols,yslovia,strfunlist,a,b,tz,ppp)
    print(list4d_tocki)
    return

main()