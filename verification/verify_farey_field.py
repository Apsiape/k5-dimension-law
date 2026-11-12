"""Independent engine A. Predictions registered before first execution, 2026-11-11.
For sqrt(5): exact minimum e_N=(a_N-sqrt5)(sqrt5-b_N).
Node fourth powers, j=1..4: (6-2sqrt5)/5, 5/4,
(6+2sqrt5)/5, (9+4sqrt5)/20. Overall limsup phi**10/20.
D liminf 0.7434960689..., limsup 1.574750... .
Phi: liminf sqrt(phi/sqrt5)=0.850650808..., limsup times phi=1.3763819... .
Zero-deficit drift: d_N=e_N/[5(a_N+b_N-1)], best constant 0.364239... .
Controls: e_4=(17sqrt5-38)/4; e_17=(305sqrt5-682)/68;
d_17=(305sqrt5-682)/1185. Mutant (7/3,2) must lose.
Brute force: ALL reduced rational support values in [0,5], orders 1..12,
and ALL straddling pairs; support-size reduction: paper §8.3; the minimum
itself is Theorem B1 (§4.2a).
No numerical tolerance is used for algebra, minimization or feasibility.
"""
import os, sys
HERE=os.path.dirname(os.path.abspath(__file__))
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[key]='1'
from fractions import Fraction as F
from math import gcd
from decimal import Decimal as D, getcontext
import json
getcontext().prec=180
sys.stdout.reconfigure(encoding='utf-8')
class Q:
    def __init__(self,a=0,b=0): self.a,self.b=F(a),F(b)
    def __add__(self,o):
        o=o if isinstance(o,Q) else Q(o)
        return Q(self.a+o.a,self.b+o.b)
    __radd__=__add__
    def __neg__(self): return Q(-self.a,-self.b)
    def __sub__(self,o): return self+-asq(o)
    def __rsub__(self,o): return asq(o)+-self
    def __mul__(self,o):
        o=asq(o); return Q(self.a*o.a+5*self.b*o.b,self.a*o.b+self.b*o.a)
    __rmul__=__mul__
    def __truediv__(self,o):
        o=asq(o); norm=o.a*o.a-5*o.b*o.b
        return self*Q(o.a/norm,-o.b/norm)
    def sign(self):
        a,b=self.a,self.b
        if not b: return (a>0)-(a<0)
        if a>=0 and b>0: return 1
        if a<=0 and b<0: return -1
        x=a*a-5*b*b
        return ((x>0)-(x<0))*((a>0)-(a<0))
    def __lt__(self,o): return (self-asq(o)).sign()<0
    def __eq__(self,o):
        o=asq(o); return self.a==o.a and self.b==o.b
    def dec(self): return D(self.a.numerator)/D(self.a.denominator)+(D(self.b.numerator)/D(self.b.denominator))*D(5).sqrt()
    def enc(self): return [str(self.a),str(self.b)]
def asq(o): return o if isinstance(o,Q) else Q(o)
sqrt5=Q(0,1); phi=(1+sqrt5)/2

def deficit(a,b,alpha): return (a-alpha)*(alpha-b)
def root4(x): return x.sqrt().sqrt()
def nodes(alpha,cap):
    L,R=(2,1),(3,1) if alpha==sqrt5 else (2,1)
    if alpha==phi: L,R=(1,1),(2,1)
    out=[(1,F(*R),F(*L))]
    while True:
        p,q=L[0]+R[0],L[1]+R[1]
        if q>cap: return out
        if Q(F(p,q))<alpha: L=(p,q)
        else: R=(p,q)
        out.append((q,F(*R),F(*L)))

total=0; brute=[]
for N in range(1,13):
    vals=sorted({F(p,q) for q in range(1,N+1) for p in range(5*q+1) if gcd(p,q)==1})
    below=[v for v in vals if Q(v)<sqrt5]; above=[v for v in vals if sqrt5<Q(v)]
    best=None; bestdr=None; drpair=None; pair=None; count=0
    for b in below:
        for a in above:
            e=deficit(a,b,sqrt5); count+=1; dr=e/(5*(a+b-1))
            if best is None or e<best: best,pair=e,(a,b)
            if bestdr is None or dr<bestdr: bestdr,drpair=dr,(a,b)
    want=nodes(sqrt5,N)[-1]
    assert pair==(want[1],want[2]) and drpair==pair
    # Verify the supporting-line remainder at EVERY possible rational block mean.
    assert all(not ((v-pair[0])*(v-pair[1])<0) for v in vals)
    total+=count
    row={'N':N,'support_values':len(vals),'pairs':count,'a':str(pair[0]),'b':str(pair[1]),'e':best.enc()}
    brute.append(row)
    print('BRUTE',row)
print('BRUTE TOTAL:',total,'straddling pair cases; 12 orders')
e4=deficit(F(9,4),F(2),sqrt5); e17=deficit(F(9,4),F(38,17),sqrt5)
assert e4==Q(F(-38,4),F(17,4)) and e17==Q(F(-682,68),F(305,68))
d17=e17/(5*(F(9,4)+F(38,17)-1))
assert d17==Q(F(-682,1185),F(305,1185))
assert e4<deficit(F(7,3),F(2),sqrt5)
print('POSITIVE CONTROLS e4,e17,d17:',str(e4.dec()),str(e17.dec()),str(d17.dec()))
print('NEGATIVE CONTROL: non-neighbour pair loses, PASS')
# Actual non-scalar carrier fixture: in M2, S=diag(2,3), mean 5/2,
# and in M1 S=2; cyclic relabelled copies equalize each marginal.
mu=2*(sqrt5-2)
variance=mu*Q(F(1,4))+mu*(Q(F(5,2))-sqrt5)*(Q(F(5,2))-sqrt5)+(1-mu)*(2-sqrt5)*(2-sqrt5)
assert variance-deficit(F(5,2),F(2),sqrt5)==mu/4
assert Q(0)<mu/4
print('NONSCALAR FIXTURE: exact excess above Farey bound = mu/4 > 0, PASS')
# Exact drift lower bound and its attaining weights at every node through cap.
allnodes={}
for name,alpha in [('sqrt5',sqrt5),('phi',phi)]:
    ns=nodes(alpha,300000)
    allnodes[name]=[{'N':n,'a':str(a),'b':str(b),'e':deficit(a,b,alpha).enc()} for n,a,b in ns]
    print(name,'STERN-BROCOT NODES:',len(ns), 'MAX_ORDER=300000')
    for n,a,b in ns:
        e=deficit(a,b,alpha); c=a+b-1; delta=e/(5*c); m=alpha-5*delta
        assert Q(b)<m and m<Q(a)
        assert m*c-a*b-alpha*alpha+alpha==Q(0)
        assert delta==e/(5*c)
    print(name,'DRIFT ZERO ROOTS:',len(ns),'PASS')

sd=D(5).sqrt(); pd=(1+sd)/2; rho=2+sd; r=sd-2
predL=[(6-2*sd)/5,D(5)/4,(6+2*sd)/5,(9+4*sd)/20]
predU=[(D(j+1)+r)**4*(rho-j)/(20*(D(j)+r)) for j in range(1,5)]
print('PREDICTED L_j:',*[str(x)[:34] for x in predL])
print('PREDICTED U_j:',*[str(x)[:34] for x in predU])
print('CONSTANTS sqrt5:',root4(predL[0]),root4(pd**10/20))
print('CONSTANTS phi:',(pd/sd).sqrt(),pd*(pd/sd).sqrt())
print('CONSTANTS drift:',root4(predL[0]/(5*(2*sd-1))),root4(pd**10/(100*(2*sd-1))))
hprev,kprev,h,k=1,0,2,1
conv=[]
for n in range(25):
    for j in range(1,5):
        pp,qq=hprev+j*h,kprev+j*k
        aa,bb=sorted([F(h,k),F(pp,qq)],reverse=True)
        e=deficit(aa,bb,sqrt5); dn=e/(5*(aa+bb-1))
        nextq=kprev+(j+1)*k
        low=D(qq)**4*e.dec(); high=D(nextq)**4*e.dec()
        # D(eps) upper endpoint is a supremum; use eps=(1-1/q^2)e_previous.
        eta=F(1,qq*qq+1); near=(1-eta)*e
        qnext=nextq
        if n>=2:
            mednext=F(hprev+(j+1)*h,nextq)
            fixed=F(hprev+4*h,kprev+4*k) if j==4 else F(h,k)
            na,nb=sorted([fixed,mednext],reverse=True)
            assert deficit(na,nb,sqrt5)<near and near<e
        ratio=D(qnext)*root4(near.dec())
        row={'n':n,'j':j,'N':qq,'a':str(aa),'b':str(bb),'e':e.enc(),'next_N':nextq,'low4':str(low),'sup4':str(high),'D_near':str(ratio),'drift_ratio':str(D(qq)*root4(dn.dec()))}
        conv.append(row)
        if n in (2,3,5,10,20,24):
            print('ASYMPTOTIC',n,j,qq,'N4e=',str(low)[:28],'D4e_sup=',str(high)[:28],'drift=',row['drift_ratio'][:23],'D_near=',row['D_near'][:23])
        if n==24:
            assert abs(low-predL[j-1])<D('1e-28')
            assert abs(high-predU[j-1])<D('1e-28')
    hprev,kprev,h,k=h,k,4*h+hprev,4*k+kprev

phinodes=nodes(phi,10**25)
for idx in [8,20,40,80,100]:
    if idx+1<len(phinodes):
        n,a,b=phinodes[idx]; nn=phinodes[idx+1][0]; e=deficit(a,b,phi).dec()
        print('PHI ASYMPTOTIC',idx,n,'N4e=',str(D(n)**4*e)[:28],'D4e_sup=',str(D(nn)**4*e)[:28])
last=phinodes[-2]; nxt=phinodes[-1][0]; pe=deficit(last[1],last[2],phi).dec()
assert abs(D(last[0])**4*pe-pd**2/5)<D('1e-28')
assert abs(D(nxt)**4*pe-pd**6/5)<D('1e-28')
with open(os.path.join(HERE,'engine_a.json'),'w',encoding='utf-8') as f:
    json.dump({'brute':brute,'pair_count':total,'nodes':allnodes,'asymptotics':conv},f,indent=2)
print('ALL ENGINE A CHECKS PASS')


