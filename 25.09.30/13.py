dna = 'cgatcgatcgataagctcgatcgctagctcgactcgt'
codon = {}
for i in range(0,len(dna),3):
    codon[dna[i:i+3]]=dna.count(dna[i:i+3])
print(codon)