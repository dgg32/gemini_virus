import requests
import re
import os

detail = ""

if not os.path.isfile("brite/brite_ko.txt"):
    kegg_page = "https://rest.kegg.jp/get/br:ko03200"

    detail = requests.get(kegg_page).text

    with open("brite/brite_ko.txt", "w") as output:
        output.write(detail)
else:
    with open("brite/brite_ko.txt", "r") as input:
        detail = input.read()

rx_entry = re.compile(r'\w\s+(K\d+)')
rx_prefix = re.compile(r'GENES\s+(\w+):')
rx_gene_id = re.compile(r'(\S+)\(\S+\)')
rx_tax = re.compile(r'TAX:(\d+)')

kegg_url_prefix = "https://rest.kegg.jp/get/"

kegg_gene_prefix = "https://rest.kegg.jp/get/"

cache = {}

with open("brite/kegg_protein_cache.csv", "r") as input:
    lines = input.readlines()
    for line in lines:
        fields = line.strip().split(",")
        cache[fields[0]] = fields[1]

# content = "taxid,ko\n"
# with open("brite/kegg_protein.csv", "w") as output:
#     output.write(content)

output_file = "import/taxon_kegg.csv"

if not os.path.isfile(output_file):
   
    with open(output_file, "w") as output:
        output.write(f"taxid,ko\n")

kegg_done = set()

with open("brite/kegg_done.csv", "r") as input:
    lines = input.readlines()
    for line in lines:
        kegg_done.add(line.strip())
    
is_gene = False

for line in detail.split("\n"):

        
    search_entry = rx_entry.search(line)
    #print (line)
    if search_entry:
        #print (ko)
        ko = search_entry.group(1)

        if ko not in kegg_done:

            kegg_url = kegg_url_prefix + ko
            #print (kegg_url)
            kegg_page = requests.get(kegg_url).text
            

            for line in kegg_page.split("\n"):
                if line.startswith("GENES"):

                    is_gene = True

                if is_gene:
                    search_prefix = rx_prefix.search(line)
                    prefix = ""
                    if search_prefix:
                        prefix = search_prefix.group(1).lower()

                    #print (line)
                    fields = re.findall(rx_gene_id, line)
                    #print (fields)
                    for f in fields:
                        
                        if f not in cache:
                            kegg_gene_url = kegg_gene_prefix + prefix + ":" +  f
                            #print (kegg_gene_url)
                            kegg_gene_page = requests.get(kegg_gene_url).text
                            
                            #print (kegg_gene_page)
                            for gene_line in kegg_gene_page.split("\n"):
                                
                                #print (gene_line)
                                if gene_line.startswith("TAXONOMY"):
                                    #print (gene_line)
                                    search_tax = rx_tax.search(gene_line)

                                    if search_tax:
                                        taxid = search_tax.group(1)

                                        cache[f] = taxid

                                        with open("brite/kegg_protein_cache.csv", "a") as output:
                                            temp = f"{f},{taxid}\n"
                                            output.write(temp)
                        
                        if f in cache:
                            taxid = cache[f]

                            with open(output_file, "a") as output:
                                output.write(f"{taxid},{ko}\n")
                            #print (f"{taxid},{ko}")
            kegg_done.add(ko)

            with open("brite/kegg_done.csv", "w") as output:
                output.write("\n".join(list(kegg_done)))

