def dna_to_rna(dna):
    """
    dna: string varaible
    """
    listdna = list(dna)
    print(listdna)
    listrna = []
    for c in listdna:
        if c == 'T': 
            listrna.append('U')
        # elif c == 'X': # else if
        else:
            listrna.append(c)
    #
    rna = ''.join(listrna)
    return rna 


dna = 'GCAT'  # -> 'GCAU'

listdna = list(dna)
print(listdna)
listrna = []
for c in listdna:
    if c == 'T':
        listrna.append('U')
    else:
        listrna.append(c)
#
rna = ''.join(listrna)
print(listrna, rna)


# =


print( ''.join(['I', 'do']))

print( '---'.join(['I', 'do', 'python']))

print( ' '.join(['I', 'do', 'python']))

print( 'I do python hahaha'.split() )

# April 21 : Midterm exam day. Time: 10:30am.

# MacOSX: pip3