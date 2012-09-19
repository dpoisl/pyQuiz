def f(n,t=".",c=","):a,*b=n.split(".");return t.join(a[x-1:x-4:-1]for x in range(0,-len(a),-3))[::-1]+(c+b[0]if b else"")
