![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

# Alignment-free Sequence Comparison
This project was one of my bioinformatics projects I did as a student at the Faculty of Electrical Engineering and Computing in Zagreb. The project was inspired by a paper published in 2017 (Zielezinski et al., Alignment-free sequence comparison: benefits, applications, and tools), where alignment-free sequence analysis methods are discussed.

## Project Overview
The goal of biological sequence analysis (protein sequences or nucleotide sequences) is to determine the similarity of two sequences, which is then used to estimate their evolutionary relationship and predict their structure or functionality. Alignment-based sequence analysis algorithms first produce the alignment of two sequences, and then, based on the number of matches and gaps, calculate their distance. These methods are very accurate, but they suffer from many disadvantages, mostly dealing with large space and time complexities. Recently, more focus has been put on alignment-free methods, which do not produce alignments but use knowledge from probability, statistics and information theory to calculate sequence similarity.

The goal of this project was to develop a framework for implementing new alignment-free methods and using them to calculate distances between biological sequences. To check the performance of those methods, one can use the AFproject website, a free service for alignment-free method benchmarking on different datasets (Zielezinski et al. Benchmarking of alignment-free sequence comparison methods. Genome Biology, 2019, 20, p144. doi: 10.1186/s13059-019-1755-7). The website can be accessed [here]
