from numpy import poly1d

class FuzzyMarkovMethod:    
    def __init__(self):
        self.nucl_codes = {'A': 0, 'T': 1, 'C': 2, 'G': 3}

    #probability matrix calculation for step 1
    def constructProbMatrix1(self, sequence: str) -> list:
        matrix_counts = [[0 for x in range(4)] for y in range(4)]
        for index in range(len(sequence)-1):
            if(sequence[index] in self.nucl_codes and sequence[index+1] in self.nucl_codes):
                matrix_counts[self.nucl_codes[sequence[index]]][self.nucl_codes[sequence[index+1]]] += 1
        matrix_probs = []
        for row in matrix_counts:
            new_row = []
            row_sum = sum(row)
            if(row_sum == 0):
                row_sum = 1
            for element in row:
                element = float(element/row_sum)
                new_row.append(element)
            matrix_probs.append(new_row)
        return matrix_probs

    # step K probability matrix calculation using matrixes for step K-1 and step 1
    def constructProbMatrixK(self, matrix_prev: list, matrix_1: list) -> list:
        matrix_K = [[0.0 for x in range(4)] for y in range(4)]
        for i in range(4):
            for j in range(4):
                for r in range(4):
                    matrix_K[i][j] += matrix_1[i][r]*matrix_prev[r][j]
        return matrix_K

    #4th degree polynomial solution
    def lambda_solver(self, y: list) -> float:
        coef4 = y[0]*y[1]*y[2]*y[3]
        coef3 = y[0]*y[1]*y[2] + y[0]*y[1]*y[3] + y[0]*y[2]*y[3] + y[1]*y[2]*y[3]
        coef2 = y[0]*y[1] + y[0]*y[2] + y[0]*y[3] + y[1]*y[2] + y[1]*y[3] + y[2]*y[3]
        coef1 = y[0] + y[1] + y[2] + y[3] - 1
        p = poly1d([coef4, coef3, coef2, coef1, 0])
        l = -1
        for r in p.roots:
            if(r.imag == 0 and r.real > l):
                l = r.real
        return l

    #similarity calculation using probability matrixes
    def FISim(self, matrix1: list, matrix2: list) -> float:
        J = []
        for i in range(4):
            h = []
            y = []
            for j in range(4):
                h.append(1 - abs(matrix1[i][j] - matrix2[i][j]))
                y.append(max(matrix1[i][j], matrix2[i][j]))
            h_sorted = sorted(h, reverse=True)
            y_sorted = []
            for h_value in h_sorted:
                y_sorted.append(y[h.index(h_value)])
            l = self.lambda_solver(y)
            A = []
            A.append(y_sorted[0])
            for j in range(1, 4, 1):
                prev = A[j-1]
                new = y_sorted[j]
                A.append(prev + new + l*prev*new)
            Ji = []
            for j in range(4):
                Ji.append(min(h_sorted[j], A[j]))
            J.append(max(Ji))
        return max(J)
    
    #call function
    def __call__(self, sequences_seq: list, sequences_id: list, writer):
                
        #probability matrix calculation
        matrixes_k8 = []
        for index in range(len(sequences_seq)):
            matrix1 = self.constructProbMatrix1(sequences_seq[index])
            matrixk = matrix1
            for _ in range(1):
                matrixk = self.constructProbMatrixK(matrixk, matrix1)
            matrixes_k8.append(matrixk)
            
        #distance calculation and writing to file
        #distance is calculated as 1 - similarity
        for index1 in range(len(sequences_seq)):
            for index2 in range(index1+1, len(sequences_seq)):
                d = round(1 - self.FISim(matrixes_k8[index1], matrixes_k8[index2]), 10)
                writer.writerow([sequences_id[index1], sequences_id[index2], d])