"""Independent engine B, registered before first execution, 2026-11-11.
No field class and no Decimal: integer square-root brackets and rational intervals.
Predictions: ALL pair minima orders 1..12 agree with the Farey law; 34 sqrt5
nodes and 26 phi nodes through 300000. Node L: .305572809,1.25,2.094427191,
.8972135955; maximum U=6.149593..., D limits .743496...,1.574750... .
Phi fourth powers phi**2/5 and phi**6/5. Drift best .364239... .
Positive controls e4=(17sqrt5-38)/4, e17=(305sqrt5-682)/68,
d17=(305sqrt5-682)/1185. A deliberately non-neighbour pair must lose.
"""
import os,sys
HERE=os.path.dirname(os.path.abspath(__file__))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from fractions import Fraction
from math import isqrt,gcd
import json
sys.stdout.reconfigure(encoding='utf-8')
SCALE=10**180
z=isqrt(5*SCALE*SCALE)
slo,shi=Fraction(z,SCALE),Fraction(z+1,SCALE)
assert slo*slo<5<shi*shi
flo,fhi=(1+slo)/2,(1+shi)/2

def e_interval(a,b,lo,hi):
    assert a>hi>lo>b
    return (a-hi)*(lo-b),(a-lo)*(hi-b)
def enc(v): return [v.numerator,v.denominator]
def approx(v): return format(float(v),'.15g')
def disjoint_better(candidate,current):
    assert candidate[1]<current[0] or current[1]<candidate[0], 'Unresolved rational interval comparison'
    return candidate[1]<current[0]

with open(os.path.join(HERE,'engine_a.json'),encoding='utf-8') as f: other=json.load(f)
case_total=0; drift_total=0
for N in range(1,13):
    values=[]
    for denominator in range(1,N+1):
        for numerator in range(0,5*denominator+1):
            if gcd(numerator,denominator)==1: values.append(Fraction(numerator,denominator))
    lows=[v for v in values if v<slo]; highs=[v for v in values if v>shi]
    best=None; bestdr=None; winner=None; dwinner=None; count=0
    for low in lows:
        for high in highs:
            e=e_interval(high,low,slo,shi); count+=1
            dr=(e[0]/(5*(high+low-1)),e[1]/(5*(high+low-1)))
            if best is None or disjoint_better(e,best): best,winner=e,(high,low)
            if bestdr is None or disjoint_better(dr,bestdr): bestdr,dwinner=dr,(high,low)
    expected=other['brute'][N-1]
    assert count==expected['pairs'] and len(values)==expected['support_values']
    assert (str(winner[0]),str(winner[1]))==(expected['a'],expected['b'])
    assert dwinner==winner
    # Independent interval evaluation of engine A's exact coefficients.
    aa,bb=map(Fraction,expected['e'])
    ext=(aa+bb*slo,aa+bb*shi) if bb>=0 else (aa+bb*shi,aa+bb*slo)
    assert max(best[0],ext[0])<=min(best[1],ext[1])
    case_total+=count; drift_total+=count
    print('BRUTE B',N,'values',len(values),'pairs',count,'epsilon winner',winner,'drift winner',dwinner)
assert case_total==other['pair_count']
print('PAIR COUNT:',case_total,'epsilon +',drift_total,'drift; all independent rational interval minima agree')

def scan(name,cap):
    L=R=None; changes=[]
    for q in range(1,cap+1):
        m=isqrt(5*q*q)
        if name=='phi': m=(m+q)//2
        changed=False
        if L is None or m*L[1]>L[0]*q: L=(m,q); changed=True
        if R is None or (m+1)*R[1]<R[0]*q: R=(m+1,q); changed=True
        if changed: changes.append((q,Fraction(*R),Fraction(*L)))
    return changes
nodes={}
for name,lo,hi in [('sqrt5',slo,shi),('phi',flo,fhi)]:
    ns=scan(name,300000); nodes[name]=ns
    expect=other['nodes'][name]
    assert len(ns)==len(expect)
    for (n,a,b),row in zip(ns,expect):
        assert (n,str(a),str(b))==(row['N'],row['a'],row['b'])
        e=e_interval(a,b,lo,hi)
        assert e[0]>0
    print('SCAN B',name,300000,'denominator cases;',len(ns),'change nodes; ALL agree')
    print('NODES:',','.join(str(x[0]) for x in ns))

ns={n:(a,b) for n,a,b in nodes['sqrt5']}
def overlap(x,y): return max(x[0],y[0])<min(x[1],y[1])
def linear_interval(a,b):
    return (a+b*slo,a+b*shi) if b>=0 else (a+b*shi,a+b*slo)
e4=e_interval(*ns[4],slo,shi); e17=e_interval(*ns[17],slo,shi)
assert overlap(e4,linear_interval(Fraction(-38,4),Fraction(17,4)))
assert overlap(e17,linear_interval(Fraction(-682,68),Fraction(305,68)))
c=5*(sum(ns[17])-1); d17=(e17[0]/c,e17[1]/c)
assert overlap(d17,linear_interval(Fraction(-682,1185),Fraction(305,1185)))
assert e4[1]<e_interval(Fraction(7,3),Fraction(2),slo,shi)[0]
print('POSITIVE CONTROLS e4,e17,d17:',*[approx(x[0]) for x in (e4,e17,d17)],'PASS')
print('NEGATIVE CONTROL non-neighbour pair loses PASS')
# Independently generate all large nodes by unit mediants, rather than A's
# convergent recursion. This recertifies the rational inputs as well as values.
left,right=(2,1),(3,1)
large_pairs={(1,Fraction(*right),Fraction(*left))}
while left[1]+right[1]<=10**17:
    p,q=left[0]+right[0],left[1]+right[1]
    if p*p<5*q*q: left=(p,q)
    else: right=(p,q)
    large_pairs.add((q,Fraction(*right),Fraction(*left)))
for row in other['asymptotics']:
    assert (row['N'],Fraction(row['a']),Fraction(row['b'])) in large_pairs
print('INDEPENDENT LARGE MEDIANT GENERATION: all 100 asymptotic inputs agree')
# 100 node records through n=24, generated independently of A's recurrence:
# read only the rational pair to certify the numeric values with intervals;
# a separate denominator scan above independently checks path generation.
for row in other['asymptotics']:
    a,b=Fraction(row['a']),Fraction(row['b']); n=row['N']; nxt=row['next_N']
    e=e_interval(a,b,slo,shi)
    low=(n**4*e[0],n**4*e[1]); upper=(nxt**4*e[0],nxt**4*e[1])
    # A's decimal values were rounded to 180 significant digits. Allow its
    # documented rounding, far smaller than the independent sqrt bracket width.
    al,au=Fraction(row['low4']),Fraction(row['sup4'])
    tolerance=Fraction(1,10**100)
    assert low[0]-tolerance<al<low[1]+tolerance
    assert upper[0]-tolerance<au<upper[1]+tolerance
    if row['n']==24:
        print('ASYMPTOTIC B j',row['j'],'N4e',approx(low[0]),'D4e_sup',approx(upper[0]))
print('INTERVAL ASYMPTOTIC CHECKS: 100 node records PASS')
with open(os.path.join(HERE,'engine_b.json'),'w',encoding='utf-8') as f:
    json.dump({'denominator_cases':600000,'epsilon_pair_cases':case_total,'drift_pair_cases':drift_total,'sqrt_interval':[str(slo),str(shi)],'nodes':{name:[[n,str(a),str(b)] for n,a,b in ns] for name,ns in nodes.items()}},f,indent=2)
print('ALL ENGINE B CHECKS PASS')

