![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Alignment-free Sequence Comparison
This project was one of my bioinformatics projects I did as a student at the Faculty of Electrical Engineering and Computing in Zagreb. The project was inspired by a paper published in 2017 (Zielezinski et al., Alignment-free sequence comparison: benefits, applications, and tools), where alignment-free sequence analysis methods are discussed.

## Project Overview
The goal of biological sequence analysis (protein sequences or nucleotide sequences) is to determine the similarity of two sequences, which is then used to estimate their evolutionary relationship and predict their structure or functionality. Alignment-based sequence analysis algorithms first produce the alignment of two sequences, and then, based on the number of matches and gaps, calculate their distance. These methods are very accurate, but they suffer from many disadvantages, mostly dealing with large space and time complexities. Recently, more focus has been put on alignment-free methods, which do not produce alignments but use knowledge from probability, statistics and information theory to calculate sequence similarity.

The goal of this project was to implement several alignment-free methods and use them to calculate distances between biological sequences coming from different datasets. The datasets were taken from AFproject, a free service for alignment-free method benchmarking, which was also used to check the performance of those methods (Zielezinski et al. Benchmarking of alignment-free sequence comparison methods. Genome Biology, 2019, 20, p144. doi: 10.1186/s13059-019-1755-7). The website can be accessed [here](https://afproject.org/app/).

Four different alignment-free methods were implemented and compared for the purpose of this project (the code for those methods can be found in the repository):
* **k-mer count**: First, two vectors are created that represent the number of different k-mers that can be found in each sequence. Then the distance (e.g., euclidean) is calculated between two vectors.
* **compression distance**: Lempel-Ziv complexities of both sequences are determined, as well as the complexity of a new sequence created by concatenating the two sequences. Normalized compression distance is then calculated using the following formula:
  ![image](https://github.com/ivanfurac/Alignment-free-sequence-comparision/assets/73389887/9c28baf1-6934-4f85-8be6-3bfaeba7206c)

* **relative entropy**: For each symbol *i*, the frequencies of that symbol (nucleotide) appearing in both sequences are calculated (*p* and *q*). A measure called Kullback-Leibler divergence is then calculated, which basically represents the dissimilarity between two probability distributions, using the formula below:
  
  ![image](https://github.com/ivanfurac/Alignment-free-sequence-comparision/assets/73389887/80017da4-51de-4b9f-9570-492487908f37)

* **fuzzy integral similarity**: The sequences are viewed as Markov chains where nucleotides represent states. Transition probabilities are calculated, and then the Sugeno fuzzy integral is used to calculate the dissimilarity between two sequences.

## Repository and Usage
