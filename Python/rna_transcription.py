def to_rna(dna_strand):
    dna = {
        "G": "C",
        "C": "G",
        "A": "U",
        "T": "A",
    }
    return "".join(dna[c] for c in dna_strand)
