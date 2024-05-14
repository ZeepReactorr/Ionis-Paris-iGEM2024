import os, sys
import re
from Bio import SeqIO, Blast
from dataclasses import dataclass

#change into the desired directory to store the results of the sorting
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

@dataclass
class LHrna:
    mother_seq:str
    frame:int
    mother_seqid:str
    siARNs : list

@dataclass
class SIrna:
    sequence:str
    ID : str
    mother_id : str

def load_seq(file:__file__, description="Load the file's sequences in a list"):
    return [seq for seq in SeqIO.parse(file, "fasta")]

def sep_seq(seq_list):
    liste_rna = [LHrna(mother_seq=read.seq, frame=21, mother_seqid=read.id,
                    siARNs=[SIrna(sequence=read.seq[index:index+21],
                                  ID=f"{read.id}_{index}", mother_id=read.id) 
                                  for index in range(0, len(read.seq)) if len(read.seq[index:index+21]) > 20])
                for read in seq_list]

    file_list = []
    for LH in liste_rna:
        all_rna = ''.join([f">{rna.ID}\n{rna.sequence}\n" for rna in LH.siARNs])
        file_list.append(f"siRNA_from_{LH.mother_seqid}.fasta")
        with open(f"siRNA_from_{LH.mother_seqid}.fasta", 'w') as file:
            file.write(f">{LH.mother_seqid}\n{LH.mother_seq}\n{all_rna}")
            
    return file_list



