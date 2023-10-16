import os
import sys
import inspect
import argparse
from Bio import SeqIO
import csv

# read arguments from command line

available_methods = [method.strip('.py') for method in os.listdir(os.getcwd() + '/methods')]

parser = argparse.ArgumentParser(description='Alignment-free sequence comparision')

parser.add_argument('--src', type=str, default = os.getcwd() + '/data', help='Full path to directory that contains datasets of sequences (each dataset inside its own folder). By default, "./data" directory will be used.')
parser.add_argument('--dest', type=str, default = os.getcwd() + '/scores', help='Full path to directory where files containing calculated similarities will be stored. One file will be created for every dataset available and every method selected. By default, "./scores" directory will be used.')
parser.add_argument('--m', nargs='*', default=available_methods, help='Alignment-free methods (one or more) that will be used to calculate similarities. By default, similarities will be calculated using all available methods.')

args = parser.parse_args()
    
# run all methods, for every dataset found

sys.path.insert(0, os.getcwd() + '/methods')

for method_name in args.m:
    # check if given method exists
    if(method_name not in available_methods):
        print(f'ERROR: Invalid method name: {method_name}. Available methods are:')
        print('/n'.join(available_methods))
        continue
    
    #read method code from file
    #class name can be arbitrary
    method = ''
    method_module = __import__(method_name)
    for name_local in dir(method_module):
        if(inspect.isclass(getattr(method_module, name_local))):
            method = getattr(method_module, name_local)()            
    if(method == ''):
        continue
            
    #run method code and calculate distances, for every dataset found
    #one file will be created for every dataset and every method
    for dataset in os.listdir(args.src):
        #define source and destination paths
        src_path = args.src + '/' + dataset
        dest_path = args.dest + '/' + dataset + '_' + method_name + '.tsv'
        
        #load all sequences
        sequences_seq = []
        sequences_id = []
        for filename in os.listdir(src_path):
            sequences_list = SeqIO.parse(open(src_path + '\\' + filename, 'r'), 'fasta')
            for sequence in sequences_list:
                sequences_seq.append(str(sequence.seq))
                sequences_id.append(sequence.id)
              
        #initialize tsv writer  
        file = open(dest_path, 'w', newline='')
        writer = csv.writer(file, delimiter='\t')
        
        #calculate distances and write them to file
        method(sequences_seq, sequences_id, writer)  
        
        #close file
        file.close()  