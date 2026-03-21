a,b=map(int,input().split())
c,d=map(int,input().split())
ta= a*60 +b
tc=c*60+d
dt=tc-ta

if dt<0:
    dt+=24*60
    
    print(dt//60,dt%60)
else:
    print(dt//60,dt%60)
