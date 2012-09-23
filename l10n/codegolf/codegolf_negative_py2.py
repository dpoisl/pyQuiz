def f(n,t=".",c=","):a=str(abs(n)).split(".");l=len(a[0]);return"-"*(n<0)+"".join(t[(i-l)%3:i]+a[0][i]for i in range(l))+(c+a[1]if a[1:]else"")

