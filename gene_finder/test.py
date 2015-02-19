def find_all_ORFs(dna):
	first_frame = find_all_ORFs_oneframe(dna[:])
	second_frame = find_all_ORFs_oneframe(dna[1:])
	third_frame = find_all_ORFs_oneframe(dna[2:])
	all_frames = first_frame + second_frame + third_frame
	return all_frames

def find_all_ORFs_oneframe(dna):
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

def rest_of_ORF(dna):
    index = 0
    stop = ['TAG', 'TAA', 'TGA']
    while index < len(dna) - 2:
        if dna[index:index + 3] in stop:
            return dna[:index]
        else:
            index = index + 3
    return dna

def find_all_ORFs_both_strands(dna):

    revdna = get_reverse_complement(dna)
    return find_all_ORFs(dna) + find_all_ORFs(revdna)

def get_complement(nucleotide):

    if nucleotide == 'A':
        return 'T'
    if nucleotide == 'T':
        return 'A'
    if nucleotide == 'C':
        return 'G'
    if nucleotide == 'G':
        return 'C'   

def get_reverse_complement(dna):

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
            length = length
            index = index + 1
    return working_ORF

print longest_ORF("ATGCGAATGTAGCATCAAA")
