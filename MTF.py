def MTFcoding(string):
    s = string
    A = sorted( list(set(s)))
    l = A
    code= ''
    for c in s:
        code+= str(l.index(c))
        l.remove(c)
        l.insert(0,c)

    return code

def MTFdecoding(A,code):

    h = sorted(A)
    word= ''
    for x in code:
        word += h[int(x)]
        h.insert(0, h.pop(int(x)))
    return word
    
