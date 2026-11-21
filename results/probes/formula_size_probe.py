# Exact minimum de Morgan formula size (leaf count; AND/OR, negations free on leaves)
# over all Boolean functions of n variables, via dynamic programming over truth tables.
import sys
n=int(sys.argv[1]); N=1<<n; FULL=(1<<N)-1
def var(i):
    t=0
    for x in range(N):
        if (x>>i)&1: t|=1<<x
    return t
cost={}
for i in range(n):
    v=var(i); cost[v]=1; cost[FULL^v]=1
by={1:set(cost)}
c=1
while len(cost)<(1<<N):
    c+=1; new=set()
    for a in range(1,c):
        b=c-a
        if a>b: break
        for f in by.get(a,()):
            for g in by.get(b,()):
                for h in (f&g,f|g):
                    if h not in cost: cost[h]=c; new.add(h)
    by[c]=new
    print("size",c,"new functions",len(new),"total",len(cost),flush=True)
    if not new and c>60: break
# constants cost 0 conceptually; report parity
par=0
for x in range(N):
    if bin(x).count("1")%2: par|=1<<x
print("n=",n,"max size",max(cost.values()),"parity size",cost.get(par))
