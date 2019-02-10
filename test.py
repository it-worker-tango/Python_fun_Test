for i in range(100,100000):
    s =  i * i
    b = 1
    k = i
    s_len = len(str(s))
    while k >0:
        b = b *10
        k = k // 10


    c = s % b
    #print(i,c,b)
    if i == 376:
        print(c, s, b, k)
    if i == c:
        print(i)