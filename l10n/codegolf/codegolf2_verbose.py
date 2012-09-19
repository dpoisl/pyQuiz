def f(n,t=".",c=","):
    a=str(n).split(".")
    result = ""
    segments = []
    for x in range(0,-len(a[0]),-3):
        segments.append(a[0][x-1:x-4:-1])
    from_segments = t.join(segments)
    result += from_segments[::-1]
    result += (c+a[-1])*len(a[1:])
