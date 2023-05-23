from Bio.Seq import Seq

dna = Seq("ATCG")
rna = dna.transcribe()
protein = dna.translate()

print(dna)
print(rna)
print(protein)