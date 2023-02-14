from Bio import Entrez 
from Bio import SeqIO 
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
import os

def faster_downloader():
    id_coati=[]
    rep= []
    coati=[]
    """
    Sirve para cargar id_coati.txt en id_coatiy descargar en formato genbank la información correspondiente a los identificadores de accesión usando el ENTREZ de Biopythony se guardar en coati y en coati.gb
    """
    coati = open('C:/Users/ander/Documents/Prueba pi/2022II_GBI6_exam2/data/coati.txt' , 'r')
    # Leemos el archivo
    data = coati.read()

    # Creamos una lista donde cada objeto se añade después de un salto \n
    coati_list = data.split("\n")
    coati.close()

    #Descargamos los datos de NCBI con ENTREZ. 
    id_list = coati_list
    Entrez.email = "anders.pujo@gmail.com" 
    coati = []
    with Entrez.efetch( db="nucleotide", rettype="gb", retmode="text", id= id_list
                      ) as handle: 
        for seq_record in SeqIO.parse(handle, "gb"): 
            coati.append(seq_record)
            SeqIO.write(coati, "data/coati.gb", "genbank")
  
    return print (coati)

from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
from Bio.Align.Applications import ClustalwCommandline
import os

def alignment():
    """
    Sirve para que el algoritmo extraiga solamente las secuencias de la variable coati y realice un alineamiento usando clustalW. El resultado debe ser coati.aln y coati.dnd que deben guardarse en su carpeta de trabajo.
    """
    seqpa = SeqIO.parse("data/coati.gb", "genbank")
    seqwr = SeqIO.write(seqpa, "data/coati.fasta", "fasta")
    
    clustalw_exe = r"C:\Program Files (x86)\ClustalW2\clustalw2.exe"
    clustalw_cline = ClustalwCommandline(clustalw_exe, infile = "data/coati.fasta")
    assert os.path.isfile(clustalw_exe), "Clustal_W executable is missing or not found"
    stdout, stderr = clustalw_cline()
     
    with open("data/coati.aln", "r") as Cotin:    
        ClustalAlign = AlignIO.read(cotin, "clustal")

    return["Aligned"]
def tree():
    """
    Sirve para que realice el cálculo de las distancias utilizando coati.aln y finalmente que imprima en la pantalla el árbol filogenético y guarde en su carpeta de trabajo el arbol como coati_phylotree.pdf
    """
    from Bio import AlignIO
    from Bio import Phylo 
    from Bio.Phylo.TreeConstruction import DistanceCalculator 
    
    calculator = DistanceCalculator('identity')
    
    from Bio.Phylo.TreeConstruction import DistanceTreeConstructor
    
    constructor = DistanceTreeConstructor(calculator)
    with open("data/coati.aln", "r") as alin: 
        alignment = AlignIO.read(alin, "clustal")
    
    distance_matrix = calculator.get_distance(alignment)
    
    arbolito = constructor.build_tree(alignment)
    arbolito.rooted = True
    
    Phylo.write(arbolito, "data/coati_phylotree.pdf", "phyloxml")
    Phylo.read(file="data/coati_phylotree.pdf", format="phyloxml")
    
    Phylo.draw(arbolito)
    
    return tree


