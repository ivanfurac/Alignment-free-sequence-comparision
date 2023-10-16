class LempelZivMethod:
    def __init__(self):
        pass
    
    #calculate Lempel-Ziv complexity of a sequence
    def lempelziv_complexity(self, seq: str) -> int:
        words = set()
        index = 0
        length = 1
        while(index + length <= len(seq)):
            if(seq[index:index+length] in words):
                length = length + 1
            else:
                words.add(seq[index:index+length])
                index = index + length
                length = 1
        return len(words)
    
    #calculate compression distance of two sequences
    def compression_distance(self, seq1: str, seq2: str) -> float:
        c1 = self.lempelziv_complexity(seq1)
        c2 = self.lempelziv_complexity(seq2)
        c12 = self.lempelziv_complexity(seq1 + seq2)
        return float((c12 - min(c1, c2))/(max(c1, c2)))
    
    #call function
    def __call__(self, sequences_seq: list, sequences_id: list, writer):
        for index1 in range(len(sequences_seq)):
            for index2 in range(index1+1, len(sequences_seq)):
                writer.writerow([sequences_id[index1], sequences_id[index2], round(self.compression_distance(sequences_seq[index1], sequences_seq[index2]),10)])