from dwave.system import DWaveSampler, EmbeddingComposite
sampler = EmbeddingComposite(DWaveSampler())
h={}
J={('s1', 's2'): -0.5}
sampleset = sampler.sample_ising(h,J, num_reads=1000)
print(sampleset)
