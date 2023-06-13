import sys


def pravayachast1(s):
    a = s.find("=")
    if a==-1:        return s
    return s[a+1:]

def getsymbol(s):
    a = s.find("=")
    if a==-1:        return s
    return s[:a]    

def main():
    fullinput = sys.stdin.readlines()
    for ii,elem in enumerate(fullinput):
        fullinput[ii] = pravayachast1(elem.replace(" =","=").replace("= ","=").replace("\n","").replace("^","**"))
    print(fullinput)
    strf1 = fullinput[0]
    strf2 = fullinput[1]
    strf3 = fullinput[2]
    strf4 = fullinput[3]
    print("syst\n",strf1,strf2,strf3,strf4,sep="  ,  ")
    x1ysl = [fullinput[4],fullinput[5]]
    x2ysl = [fullinput[6],fullinput[7]]
    x3ysl = [fullinput[8],fullinput[9]]
    x4ysl = [fullinput[10],fullinput[11]]
    print("ysl",x1ysl,x2ysl,x3ysl,x4ysl,sep="\n")
    a,b = eval(fullinput[12])
    print("time\n",a,b)
    tz = fullinput[13]
    print("t*=",tz)
    x1p,x2p,x3p,x4p = eval(fullinput[14])
    print("guess",x1p,x2p,x3p,x4p)
    symbols = []
    for elem in fullinput[15].split(","):
        symbols.append(elem)
    print("symbols",symbols)
    return



main()