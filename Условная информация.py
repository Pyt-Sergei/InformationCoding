import pandas as pd
import math


def H(L,denom):
    return -sum(map(lambda x: x/denom * math.log2(x/denom), filter(lambda x: x!=0, L)))


def task1():

    tbl = pd.read_csv('StudentsPerformance.csv')
    grp = tbl.groupby(['gender', 'race/ethnicity']).agg({'lunch': 'count'})
    ptbl = grp.pivot_table('lunch', 'gender', 'race/ethnicity')
    fmtb = grp.pivot_table('lunch','race/ethnicity', 'gender')

    I_AB = 0
    for name in fmtb:
        sm = sum(fmtb[name])
        I_AB += H(fmtb[name], sm)*sm/1000

    I_A = H([sum(ptbl[name]) for name in ptbl ], 1000)

    print('Энтропия A', I_A )
    print('Мера зависимости', (I_A - I_AB)/I_A)


def task2():
    
    tbl = pd.read_csv('StudentsPerformance.csv')
    grp = tbl.groupby(['gender', 'lunch']).agg({'race/ethnicity': 'count'})
    ptbl = grp.pivot_table('race/ethnicity', 'gender', 'lunch')
    fmtb = grp.pivot_table('race/ethnicity', 'lunch', 'gender')

    I_AB = 0
    for name in ptbl:
        sm = sum(ptbl[name])
        I_AB += H(ptbl[name],sm) * sm/1000

    I_A = H([sum(fmtb[name]) for name in fmtb ], 1000)

    print('Энтропия A', I_A )
    print('Мера зависимости', (I_A - I_AB)/I_A )


def task2b():

    tbl = pd.read_csv('StudentsPerformance.csv')
    grp = tbl.groupby(['race/ethnicity', 'lunch']).agg({'gender': 'count'})                                                        
    ptbl = grp.pivot_table('gender', 'race/ethnicity', 'lunch')
    fmtb = grp.pivot_table('gender', 'lunch', 'race/ethnicity')

    I_AB = 0
    for name in ptbl:
        sm = sum(ptbl[name])
        I_AB += H(ptbl[name],sm) * sm/1000

    I_A = H([sum(fmtb[name]) for name in fmtb ], 1000)

    print('Энтропия A', I_A )
    print('Мера зависимости', (I_A - I_AB)/I_A )


tbl = pd.read_csv('StudentsPerformance.csv')
def task45(oldname, newname):
    
    global tbl
    mth = list(tbl[oldname])
    mth =  sorted(mth)

    p1,p2,p3,p4 = mth[200],mth[400],mth[600],mth[800]
    mathgrp = []
    
    for x in list(tbl[oldname]):

        if x < p1:
            mathgrp.append(1)
        elif x >= p1 and x < p2:
            mathgrp.append(2)
        elif x >= p2 and x < p3:
            mathgrp.append(3)
        elif x >= p3 and x < p4:
            mathgrp.append(4)
        else:
            mathgrp.append(5)

    tbl[newname] = mathgrp

    grp = tbl.groupby(['gender', newname]).agg({oldname: 'count'})                                                        
    ptbl = grp.pivot_table(oldname, newname, 'gender')
    fmtb = grp.pivot_table(oldname, 'gender', newname)

    I_AB = 0
    for name in ptbl:
        sm = sum(ptbl[name])
        I_AB += H(ptbl[name],sm) * sm/1000

    I_A = H([sum(fmtb[name]) for name in fmtb ], 1000)

    print('Энтропия A', I_A )
    print('Мера зависимости', (I_A - I_AB)/I_A )
            
        
