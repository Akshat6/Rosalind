import utils
utils.crear_screen()
try:
    data2 = open("rna_codon_table.txt","r")
except FileNotFoundError:
    print("rna_codon_table.txt")
    print("ending execution.....")
    quit()
text2=data2.read()
text2=text2.split("\n")
data = open(utils.get_data_file_name(__file__),"r")
text=data.read()

codon_list=[]
protein_list=[]
for i in range(len(text2)):
    codon_list.append(text2[i].split(" ")[0])
    protein_list.append(text2[i].split(" ")[1])
rna_codon_dict=dict(zip(codon_list,protein_list))
#print (rna_codon_dict)
protein=""
for i in range(0,len(text)-3,3):
    sub=text[i:i+3]
    if(rna_codon_dict[sub].lower()=="stop"):
        break
    protein+=rna_codon_dict[sub]
    
print(protein)
