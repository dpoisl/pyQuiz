def f(n,t=".",c=","):a=n.split(".");return t.join(a[0][x-1:x-4:-1]for x in range(0,-len(a[0]),-3))[::-1]+(c+a[-1])*len(a[1:])
