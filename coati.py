def fasta_downloader(n,n):
    """
    Descarga en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopython 
    """
    from Bio import Entrez  
        with Entrez.efetch(db="nucleotide", rettype="fasta", retmode="text", id="KP691608.1") as handle:
        seq_record = SeqIO.read(handle, "fasta")
        print("%s with %i features" % (seq_record.id, len(seq_record.features)))
        seq_record.seq
    return(fast)

def alignment(): 
    
"""    
para que el algoritmo extraiga solamente las secuencias de la variable coati y realice un alineamiento usando clustalW. El resultado debe ser coati.aln y coati.dnd que deben guardarse en su carpeta de trabajo.
"""