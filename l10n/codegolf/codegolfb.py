def f(n,t=".",c=","):a,*b=str(abs(n)).split(".");l=len(a);return"-"*(n<0)+"".join(t[(i-l)%3:i]+a[i]for i in range(l))+(c+b[0]if b else"")
