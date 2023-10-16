from typing import Any
import numpy as np
from scipy import entropy

class RelativeEntropyMethod:
    def __init__(self):
        pass
    
    #calculates Kullback-Leibler divergency
    def entropy_distance(seq1: str, seq2: str) -> float:
        dict1 = {}
        dict2 = {}
        for element in seq1:
            if(element in dict1):
                dict1[element] = dict1[element] + 1
            else:
                dict1[element] = 1
                dict2[element] = 0
        for element in seq2:
            if(element in dict2):
                dict2[element] = dict2[element] + 1
            else:
                dict2[element] = 1
                if(element not in dict1):
                    dict1[element] = 0
        pk1 = []
        pk2 = []
        for element in dict1:
            if(dict1[element] == 0.):
                dict1[element] = 1
            if(dict2[element] == 0.):
                dict2[element] = 1
            pk1.append(dict1[element])
            pk2.append(dict2[element])
        pk1 = np.array(pk1)
        pk2 = np.array(pk2)
        return entropy(pk=pk1, qk=pk2)
    
    #call function
    def __call__(self, sequences_seq: list, sequences_id: list, writer):
        for index1 in range(len(sequences_seq)):
            for index2 in range(index1+1, len(sequences_seq)):
                writer.writerow([sequences_id[index1], sequences_id[index2], round(self.entropy_distance(sequences_seq[index1], sequences_seq[index2]),10)])