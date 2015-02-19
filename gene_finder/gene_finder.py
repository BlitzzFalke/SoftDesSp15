# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Marie-Caroline Finke

"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons, aa_table
import random
from load import load_seq

def shuffle_string(s):
    """ Shuffles the characters in the input string
        NOTE: this is a helper function, you do not have to modify this in any way """
    return ''.join(random.sample(s,len(s)))

### YOU WILL START YOUR IMPLEMENTATION FROM HERE DOWN ###


def get_complement(nucleotide):

    """ Returns the complementary nucleotide

        nucleotide: a nucleotide (A, C, G, or T) represented as a string
        returns: the complementary nucleotide
        >>> get_complement('A')
        'T'
        >>> get_complement('C')
        'G'"""

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'
    

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
        >>> get_reverse_complement("ATGCCCGCTTT")
        'AAAGCGGGCAT'
        >>> get_reverse_complement("CCGCGTTCA")
        'TGAACGCGG'
        """
    index = 0
    complement_string = ''
    while index < len(dna):
        nucleotide = dna[index]
        complement = get_complement(nucleotide)
        complement_string = complement_string + complement
        index = index + 1

   
    complement_list = list(complement_string)
    reverse_complement_list = complement_list.reverse()
    reverse_complement_string = ''.join(complement_list)
    return reverse_complement_string


def rest_of_ORF(dna):

    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
        >>> rest_of_ORF("ATGTGAA")
        'ATG'
        >>> rest_of_ORF("ATGAGATAGG")
        'ATGAGA'"""

    index = 0
    stop = ['TAG', 'TAA', 'TGA']
    while index < len(dna) - 2:
        if dna[index:index + 3] in stop:
            return dna[:index]
        else:
            index = index + 3
    return dna


def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_oneframe("ATGCATGAATGTAGATAGATGTGCCC")
    ['ATGCATGAATGTAGA', 'ATGTGCCC']
    """
    index = 0
    result = []
    while index < len(dna) - 2:
        if dna[index:index + 3] == 'ATG':
            start = index
            open_frame = rest_of_ORF(dna[index:])
            result.append(open_frame)
            length = len(open_frame)
            index = index + length
        else:
            index = index + 3
    return result


def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs

    >>> find_all_ORFs("ATGCATGAATGTAG")
    ['ATGCATGAATGTAG', 'ATGAATGTAG', 'ATG']
    """
    first_frame = find_all_ORFs_oneframe(dna[:])
    second_frame = find_all_ORFs_oneframe(dna[1:])
    third_frame = find_all_ORFs_oneframe(dna[2:])
    all_frames = first_frame + second_frame + third_frame
    return all_frames


def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    >>> find_all_ORFs_both_strands("ATGCGAATGTAGCATCAAA")
    ['ATGCGAATG', 'ATGCTACATTCGCAT']
    """
    revdna = get_reverse_complement(dna)
    return find_all_ORFs(dna) + find_all_ORFs(revdna)



def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string
    >>> longest_ORF("ATGCGAATGTAGCATCAAA")
    'ATGCTACATTCGCAT'
    """
    index = 0
    longest_length = 0
    all_ORFs = find_all_ORFs_both_strands(dna)
    while index < len(all_ORFs):
        length = len(all_ORFs[index])
        if length > longest_length:
            longest_length = length
            working_ORF = all_ORFs[index]
            index = index + 1
        else:
            index = index + 1
    return working_ORF



def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    
    index = 0
    all_shuffled_longest_length = 0
    while index < num_trials:
        shuffled_dna = shuffle_string(dna)
        shuffled_longest_length = len(longest_ORF(shuffled_dna))
        if shuffled_longest_length > all_shuffled_longest_length:
            all_shuffled_longest_length = shuffled_longest_length
            index = index + 1
        else:
            index = index + 1
    return all_shuffled_longest_length


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment

        >>> coding_strand_to_AA("ATGCGA")
        'MR'
        >>> coding_strand_to_AA("ATGCCCGCTTT")
        'MPA'
    """
    
    index = 0
    amino_acid_string = ''
    while index < len(dna) - 2:
        amino_acid = aa_table[dna[index:index+3]]
        amino_acid_string = amino_acid_string + amino_acid
        index = index + 3
    return amino_acid_string





def gene_finder(dna):
    """ Returns the amino acid sequences that are likely coded by the specified dna
        
        dna: a DNA sequence
        returns: a list of all amino acid sequences coded by the sequence dna.
    """
    threshold = longest_ORF_noncoding(dna,1500)
    all_ORFs_gene = find_all_ORFs_both_strands(dna)
    index = 0
    amino_acid_gene = []
    while index < len(all_ORFs_gene):
        if len(all_ORFs_gene[index]) > threshold:
            amino_acid_gene.append(coding_strand_to_AA(all_ORFs_gene[index]))
            index = index + 1
        else:
            index = index + 1
    return amino_acid_gene



if __name__ == "__main__":
    dna = load_seq("./data/X73525.fa")
    print gene_finder(dna)
    # threshold = longest_ORF_noncoding(dna,1500)
    # print threshold
    import doctest
    doctest.testmod()