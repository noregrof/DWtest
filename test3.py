import networkx as nx
from collections import defaultdict
from dwave.system import DWaveSampler, EmbeddingComposite

E = { 'e1':(2,3,1),'e2':(2,3,1), 'e3':(2,2,3),'e4':(2,2,3), 'e5':(1,4,2),'e6':(1,4,2), 'e7':(1,1,4),'e8':(1,1,4) }
EE = [ (2,3,1),(2,3,1),(2,2,3),(2,2,3),(1,4,2),(1,4,2),(1,1,4),(1,1,4) ]
P = { 'p1':(5,0), 'p2':(5,0), 'p3':(0,5), 'p4':(0,5) }

for e in E:
    print(e)
    print(E[e])

Q = defaultdict(int)

lagrange = 8
for e in E:
    (c1,h1,i1) = E[e]
    for f in E:
        (c2,h2,i2) = E[f]
        if ((c1==c2) & (h1==h2) & (i1==i2)):
            Q[(e,f)] += (2*lagrange-2)
        else:
            Q[(e,f)] += 2*lagrange 
    Q[(e,e)] = (-7*lagrange+2)

print(Q)

sampler = EmbeddingComposite(DWaveSampler())
sampleset = sampler.sample_qubo(Q, num_reads=10, chain_strength=20)

print(sampleset)

