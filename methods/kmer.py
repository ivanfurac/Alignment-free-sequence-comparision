import math

class KmerCountMethod:
    def __init__(self, k: int=4):
        self.k = k
    
    #counts k-mers in both sequences
    def kmer_count(self, seq1: str, seq2: str) -> tuple:
        seq1_dict = {}
        seq2_dict = {}

        for index in range(len(seq1) - self.k + 1):
            kmer = seq1[index: index+self.k]
            if(kmer in seq1_dict):
                seq1_dict[kmer] = seq1_dict[kmer]+1
            else:
                seq1_dict[kmer] = 1

        for index in range(len(seq2) - self.k + 1):
            kmer = seq2[index: index+self.k]
            if(kmer in seq2_dict):
                seq2_dict[kmer] = seq2_dict[kmer]+1
            else:
                seq2_dict[kmer] = 1

        return (seq1_dict, seq2_dict)
    
    #calculates euclidean distance between two "vectors" of k-mers
    def distance(self, seq1_dict: dict, seq2_dict: dict) -> float:
        max1 = max(list(seq1_dict.values()))
        max2 = max(list(seq2_dict.values()))
        distance = 0
        for key in seq1_dict:
            if(key in seq2_dict):
                distance = distance + (seq1_dict[key]/max1 - seq2_dict[key]/max2)**2
            else:
                distance = distance + (seq1_dict[key]/max1)**2
        for key in seq2_dict:
            if(key not in seq1_dict):
                distance = distance + (seq2_dict[key]/max2)**2

        return math.sqrt(distance)
    
    #call function
    def __call__(self, sequences_seq: list, sequences_id: list, writer):
        for index1 in range(len(sequences_seq)):
            for index2 in range(index1+1, len(sequences_seq)):
                (seq1_dict, seq2_dict) = self.kmer_count(sequences_seq[index1], sequences_seq[index2])
                distance = self.distance(seq1_dict, seq2_dict)
                writer.writerow([sequences_id[index1], sequences_id[index2], round(distance,10)])