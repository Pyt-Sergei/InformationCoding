A = 'abcd'
P = [2,5,5,4]
r = 4

def coding(s):
    beg = 0
    end = 1
    prob = 1
    k = 0
    k1=0
    ans= ''

    for x in s:
        pos = A.find(x)
        end = beg*(2**r) + prob*sum(P[0:pos+1])
        beg = beg*(2**r) + prob*sum(P[0:pos])
        prob=prob*P[pos]
        k += r
        print(beg,end,k,sep='--')
        k1 += r

        while True:
            if end < 2**(k-1):
                k-= 1
                ans+= '0'
            elif beg >= 2**(k-1):
                beg-= 2**(k-1)
                end-= 2**(k-1) 
                k-= 1
                ans+= '1'
            elif beg%2 == 0 and end%2 == 0:
                beg/= 2
                end/= 2
                prob/= 2
                k-= 1
            elif k > 30:
                beg//= 2
                end//= 2
                prob = end - beg
                k-= 1
            else:
                break
        print(beg,end,k,sep='--')
    return ans
