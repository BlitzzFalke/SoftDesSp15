def rest_of_ORF(dna):
    index = 0
    stop = ['TAG', 'TAA', 'TGA']
    while index < len(dna) - 2:
        if dna[index:index + 3] in stop:
            return dna[:index]
        else:
            index = index + 3
    return dna
print rest_of_ORF('ATGCATGAATGTAG')