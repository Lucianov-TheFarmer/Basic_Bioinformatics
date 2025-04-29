# Python
from Bio import SeqIO

def find_shared_motifs(filename):
    sequences = [str(record.seq) for record in SeqIO.parse(filename, "fasta")]
    shortest_seq = min(sequences, key=len)
    for length in range(len(shortest_seq), 0, -1):
        for start in range(len(shortest_seq) - length + 1):
            motif = shortest_seq[start:start+length]
            if all(motif in seq for seq in sequences):
                return motif
    return ""

print(find_shared_motifs("input.fasta"))