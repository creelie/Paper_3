"""Exact geometric-edge checks; finite supplements to the all-length written proof.

Unlike the paper's prefix-weight parity formula, intersection is computed by
encoding actual directed grid edges and intersecting their bitsets.
"""
from math import comb
import json

def geometry(m):
    ids={(x,y,d):i for i,(x,y,d) in enumerate(
        (x,l-x,d) for l in range(m) for x in range(l+1) for d in [0,1])}
    edges=[];vertices=[]
    for w in range(1<<m):
        x=y=0;e=0;v={(0,0)}
        for p in range(m):
            d=(w>>p)&1;e|=1<<ids[x,y,d]
            x+=1-d;y+=d;v.add((x,y))
        edges.append(e);vertices.append(v)
    return ids,edges,vertices

def parity_rows(edges):
    return [sum(1<<j for j,f in enumerate(edges) if (e&f).bit_count()%2)
            for e in edges]

def star_checks(maximum=9):
    out=[]
    for k in range(1,maximum+1):
        ids,edges,vertices=geometry(k);N=1<<k;rows=parity_rows(edges)
        masks=[sum(1<<w for w in range(N) if w.bit_count()==t) for t in range(k+1)]
        found=set()
        for a in range(N):
            wa=a.bit_count()
            if not wa:continue
            allowed=masks[wa]|masks[wa-1]
            for b in range(N):
                if b.bit_count()+1==wa and (rows[a]>>b)&1==(k+1)%2 and \
                   not ((rows[a]^rows[b])&~allowed):found.add((a,b))
        last=1<<(k-1);expected={(u|last,u) for u in range(last)}
        if k>=3 and k%2:
            a=1+sum(1<<i for i in range(1,k,2));b=sum(1<<i for i in range(2,k,2))
            expected.add((a,b))
        assert found==expected,(k,found^expected)
        for u in range(last):
            for c in range(N):
                actual=((rows[u|last]^rows[u])>>c)&1
                assert actual==((c&(last-1)).bit_count()==u.bit_count())
        cells=0
        for p,e in enumerate(edges):
            for level in range(k-1):
                for x in range(level+1):
                    y=level-x
                    boundary=sum(1<<ids[a,b,d] for a,b,d in
                        [(x,y,0),(x,y,1),(x,y+1,0),(x+1,y,1)])
                    assert (e&boundary).bit_count()==int((x,y) in vertices[p])+int((x+1,y+1) in vertices[p])
                    cells+=1
        out.append({'k':k,'star_pairs':len(found),'canonical_pairs':last,
                    'exceptional_pairs':int(k>=3 and k%2==1),'cell_checks':cells})
    return out

def skeletons(m):
    result=[]
    def rec(i,height,stack,arcs):
        if i==m:
            result.append((tuple(arcs),tuple(stack)));return
        rec(i+1,height+1,stack+[i],arcs)
        if height:rec(i+1,height-1,stack[:-1],arcs+[(stack[-1],i)])
    rec(0,0,[],[])
    return result

def system(m,arcs,free):
    classes=[]
    for a in range(1<<len(free)):
        words=[]
        for orient in range(1<<len(arcs)):
            w=sum(((a>>i)&1)<<p for i,p in enumerate(free))
            w+=sum(1<<(p if (orient>>i)&1 else q) for i,(p,q) in enumerate(arcs))
            words.append(w)
        classes.append(frozenset(words))
    return tuple(classes)

def skeleton_checks(maximum=8):
    out=[]
    for m in range(maximum+1):
        skels=skeletons(m);assert len(skels)==comb(m,m//2)
        _,edges,_=geometry(m);systems=set();pairs_checked=0
        for arcs,free in skels:
            k=len(free);_,small,_=geometry(k)
            classes=system(m,arcs,free);systems.add(frozenset(classes))
            assert sum(len(c)**2 for c in classes)==1<<m
            for a,C in enumerate(classes):
                for x in C:
                    assert x.bit_count()==len(arcs)+a.bit_count()
                    for b,D in enumerate(classes):
                        expected=(small[a]&small[b]).bit_count()%2
                        for y in D:
                            assert (edges[x]&edges[y]).bit_count()%2==expected
                            pairs_checked+=1
        assert len(systems)==len(skels)
        out.append({'m':m,'skeletons':len(skels),'distinct_systems':len(systems),'identity_pairs':pairs_checked})
    return out

def path_classification(maximum=4):
    result=[]
    for n in range(1,maximum+1):
        _,edges,_=geometry(2*n);words=[w for w in range(1<<(2*n)) if w.bit_count()==n]
        adj=[sum(1<<j for j,v in enumerate(words) if v!=w and (edges[w]&edges[v]).bit_count()%2==0) for w in words]
        def cliques(target):
            found=set()
            def rec(P,C):
                if len(C)==target:found.add(frozenset(C));return
                while len(C)+P.bit_count()>=target:
                    bit=P&-P
                    if not bit:return
                    i=bit.bit_length()-1;P^=bit;rec(P&adj[i],C+[words[i]])
            rec((1<<len(words))-1,[]);return found
        actual=cliques(1<<n)
        expected={system(2*n,arcs,free)[0] for arcs,free in skeletons(2*n) if not free}
        assert actual==expected
        assert len(actual)==comb(2*n,n)//(n+1)
        assert not cliques((1<<n)+1)
        result.append({'n':n,'paths':len(words),'extremal_families':len(actual),'larger_family_exists':False})
    return result

if __name__=='__main__':
    print(json.dumps({'method':'exact geometric edge intersections; no SAT solver or floating point',
        'star_and_cell':star_checks(),'skeletons':skeleton_checks(),
        'path_classification':path_classification(),'status':'PASS'},indent=2))
