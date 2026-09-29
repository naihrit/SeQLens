dna = ""
#________________________________________________________________________________________
#FUNCTIONS_____________________________________________________________________________
rna = []
protein= []
def transcription(dna):
    while len(dna) > 0:
        codon = dna[0:3]
        codon=codon.replace("A","U")
        codon=codon.replace("T","A")
        codon=codon.replace("G","X")
        codon=codon.replace("C","G")
        codon=codon.replace("X","C")
        rna.append(codon)
        dna = dna[3:len(dna)]
    return rna

AminoAcid = {
    'UUU':'Phe','UUC':'Phe','UUA':'Leu','UUG':'Leu',
    'CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
    'AUU':'Ile','AUC':'Ile','AUA':'Ile','AUG':'Met',
    'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
    'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser',
    'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
    'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
    'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
    'UAU':'Tyr','UAC':'Tyr','UAA':'Stop','UAG':'Stop',
    'CAU':'His','CAC':'His','CAA':'Gln','CAG':'Gln',
    'AAU':'Asn','AAC':'Asn','AAA':'Lys','AAG':'Lys',
    'GAU':'Asp','GAC':'Asp','GAA':'Glu','GAG':'Glu',
    'UGU':'Cys','UGC':'Cys','UGA':'Stop','UGG':'Trp',
    'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg',
    'AGU':'Ser','AGC':'Ser','AGA':'Arg','AGG':'Arg',
    'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly',
}

def translation(rna):
    protein = []
    for codon in rna:
        if codon in AminoAcid:
            amino = AminoAcid.get(codon, '?')
            protein.append(f"{codon} = {amino}") 
    return protein


mutation = {
    # Hemoglobinopathies (HBB gene)
    "GUG": "Sickle Cell Anemia (HBB: p.Glu6Val / HbS)",
    "AAG": "Hemoglobin C Disease (HBB: p.Glu6Lys / HbC)",
    "UAG": ("Beta-Thalassemia major (HBB: p.Lys18Ter - premature stop)",
            "Beta-Thalassemia (HBB: p.Gln40Ter - nonsense mutation)",
            "Cystic Fibrosis (CFTR: p.Tyr122Ter - premature termination)",
            "Familial Hypercholesterolemia (LDLR nonsense mutation)"), 

    # Oncology & Kinase Signaling
    "GAG": "BRAF V600E (Common in Melanoma, Colorectal, Thyroid cancers)",
    "CGU": "TP53 hotspot (p.Cys176Arg - loss of tumor suppressor function)",
    "UGG": ("TP53 hotspot (p.Arg248Trp - dominant-negative cancer driver)",
            "Phenylketonuria (PAH: p.Arg408Trp - classic PKU variant)"),
    "CAG": "TP53 hotspot (p.Arg248Gln - impaired DNA binding)",
    "CAU": "TP53 hotspot (p.Arg273His - structural oncogenic variant)",
    "UGU": ("TP53 hotspot (p.Arg273Cys - structural oncogenic variant)",
            "KRAS G12C (Targetable NSCLC mutation)",
            "Familial Hypercholesterolemia (LDLR: p.Arg416Cys)"),
    "GAU": ("KRAS G12D (Common driver in Pancreatic & Colorectal adenocarcinoma)",
            "Hereditary Hemochromatosis (HFE: p.His63Asp / H63D)",),
    "GUU": "KRAS G12V (Colorectal and Non-small cell lung cancer)",
    "CGG": "EGFR L858R (Exon 21 activating mutation in Lung Adenocarcinoma)",
    "AUG": "EGFR T790M (Gatekeeper resistance mutation to 1st/2nd gen TKIs)",

    # Cystic Fibrosis (CFTR gene)
    "AGA": ("Cystic Fibrosis (CFTR: p.Gly551Asp / G551D gating mutation)",
            "Osteogenesis Imperfecta (COL1A1 glycine substitution)"),
    "UGA": ("Cystic Fibrosis (CFTR: p.Arg553Ter - severe nonsense mutation)",
            "Phenylketonuria (PAH: p.Arg408Ter - classic severe PKU)"),
    

    # Neurological & Neuromuscular
    "UUA": "Amyotrophic Lateral Sclerosis (SOD1 variant)",
    "UGC": "Huntington's-like or spinocerebellar ataxia modifiers",
    "AAA": "Friedreich's Ataxia (FXN loss-of-function missense)",

    # Cardiovascular & Metabolic
    "AAU": "Tay-Sachs Disease (HEXA: p.Asp170Asn)",
    "ACU": "Hereditary Hemochromatosis (HFE: p.Ala28Val)",
    "UAC": "Hereditary Hemochromatosis (HFE: p.Cys282Tyr / C282Y)",
    # Endocrine & Connective Tissue
    "AGG": "Achondroplasia (FGFR3: p.Gly380Arg - dwarfism hotspot)",
    "CGC": "Marfan Syndrome (FBN1: cysteine-disrupting substitution)"
}


def disease_search(rna, protein):
    for codon in rna:
            if codon in mutation:
                amino = mutation.get(codon, '?')
                protein.append(f"\n{codon} = {amino}") 
    return protein

def call(dna, rna, protein):
     transcription(dna)
     translation(rna)
     disease_search(rna,protein)
     return protein

def reset():
    rna.clear()
    protein.clear()

#___________________________________________________________________________________________ 

##GETTING JS DATA____________________________________________________________________________________
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/translate', methods=['POST'])
def translate_dna():
    data = request.get_json()
    seq = data.get('seq', '')
    #______________________________________________________________________________
    rna = transcription(seq)
    protein=translation(rna)
    protein=disease_search(rna,protein)
    #______________________________________________________________________________
    protein_text = "\n".join(protein)
    if protein_text == "":
        protein_text= "\n Could not find the given sequence please provide another valid dna strand..."
    result = f"Python received sequence: {seq}\n{protein_text}"
    reset()
    return jsonify({"output": result})
if __name__ == '__main__':
    app.run(port=5000, debug=True)


