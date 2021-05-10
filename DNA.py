# https://docs.python.org/3/library/typing.html

from pprint import pprint
from typing import (
    Optional,
    Dict,
)
from collections import (
    Counter, 
    defaultdict,
)


# Bases Nitrogenadas que participan del ADN
BASES_NITROGENADAS = {
    "A": "Adenina",
    "T": "Timina",
    "C": "Citosina",
    "G": "Guanina"
}

# Base nitrogrenadas complementarias en la cadena de ADN
# A <-> T , G <-> C
COMPLEMENT = {
    "A": "T", 
    "T": "A",
    "C": "G",
    "G": "C"
}

# --- Info ---
def about_me():
    "Informacion acerca del ADN"
    pass
    
class DNA: 

    def __init__(self, sequence: Optional[str] = None): 
        if sequence is not None:
            assert set(sequence) == set(BASES_NITROGENADAS), "All nucleotides must be in {'A','T','G','C'}"
        self.sequence = sequence 

    def complement(self, sequence: Optional[str] = None): 
        "Compementary ADN sequence"
        sequence = sequence if sequence is not None else self.sequence
        return "".join(COMPLEMENT.get(nucleotide) for nucleotide in sequence)
    
    def to_ARN(self,):
        pass
    
    def from_ARN(self, sequence: str): 
        #
        pass

    # magic methods
    def __repr__(self,): 
        summary = []
        
        # Frequency of Nucleotides
        count = self.nucleotide_representativity(self.sequence)
        count_str = ["{!r}: {}".format(n,c) for n,c in count]
        summary.append("; ".join(count_str))
        
        # len of sequence
        summary.append("'length': {}".format(len(self.sequence)))
        
        # head of sequence
        head_sequence = self.sequence[:20] + "..." if len(self.sequence) > 20 else self.sequence
        summary.append("DNA('"+ head_sequence +"')")

        return "\n".join(summary)

    @staticmethod
    def nucleotide_representativity(sequence: str, sort: bool = True):
        "Representativity of each nucleotide in a DNA sequence"
        # Count nucleotides in the sequence
        count_nucleotides = dict(Counter(sequence))

        # Sort nucleotides by frequency
        count_nucleotides = sorted(count_nucleotides.items(), key = lambda item: item[1], reverse=True)
        
        return count_nucleotides
