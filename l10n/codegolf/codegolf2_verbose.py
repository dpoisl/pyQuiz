def f(n,t=".",c=","):                     # f("12345.32")
    a=str(n).split(".")                   # ("12345", "32")
    result = ""
    segments = []
    for x in range(0,-len(a[0]),-3):      # x= 0, -3, ...
        segments.append(a[0][x-1:x-4:-1]) # a[0][-1:-4], a[0][-4:-7], ...
    from_segments = t.join(segments)      # reversed string with separators
    result += from_segments[::-1]         # reversed again
    result += (c+a[-1])*len(a[1:])        # a[1:] is either [] or ["32"]
