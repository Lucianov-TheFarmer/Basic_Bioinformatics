from Bio import SeqIO

orfs = []

def find_orfs(seq):
    """Find all open reading frames in a sequence."""
    for nuc in [seq, seq.reverse_complement()]:
        for frame in range(3):
            pro = nuc[frame:len(nuc)].translate()
            for aa in pro.split("*")[:-1]:
                if "M" in aa:
                    pos=[pos for pos, char in enumerate(aa) if char == "M"]
                    for p in pos:
                        orfs.append(str(aa[p:]))
                
    return orfs

def main():
    """Main program."""
    for record in SeqIO.parse("input.fasta", "fasta"):
        find_orfs(record.seq)

    for i in set(orfs):
        print(i)

if __name__ == "__main__":
    main()

