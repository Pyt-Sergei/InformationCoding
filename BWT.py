def BWTcoding(word):

    l = list(word)
    h = []

    for i in l:
        l = l[1:] + l[0:1]
        h.append(l)
    h= sorted(h)
    
    code = ''
    for x in h:
        code += x[len(h)-1]

    return code


def BWTdecoding(code):
    
    w = sorted(list(code))

    m = [(x,i) for i,x in enumerate(w) ]
    n = []
    for i in range(0,len(code)):
        n.append((code[i], w.index(code[i]) ))
        w[w.index(code[i])] = 0

    ans =''
    pos =0

    for i in range(len(code)):
        pos = n.index(m[pos])
        ans += m[pos][0]

    return ans

