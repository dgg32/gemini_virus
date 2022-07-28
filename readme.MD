

# Introduction

  

This repository contains code and data for my article "[I Built the Same Virus Knowledge Graph on Gemini Cloud, AuraDB and Neo4j Desktop](https://dgg32.medium.com/i-built-the-same-virus-knowledge-graph-on-gemini-cloud-auradb-and-neo4j-desktop-e2efa95f566c)".

1. The import folder contains all the data needed for the knowledge graph.

2. The brite folder contains raw data that mainly come from the source websites.

3. The parsed_file folder contains intermediate files.


4. The py and ipynb are scripts that generate the final data from the raw data.

  


# Prerequisite

Python with the pyphy package (pip install pyphy)

Neo4j

AuraDB

Gemini Data account

# Data preparation

Execute the following script one after another

1. download_various_kegg.py

2. parse_disease.py

3. virus_disease_drug.ipynb

4. download_kegg_virus.ipynb

5. parse_virusdb.ipynb

6. add_strand_type.ipynb

7. download_protein_kegg.py

8. parse_kegg.ipynb

9. download_drug.ipynb



# Data import
The medium article contains instructions for the data import.


# Authors

*  **Sixing Huang** - *Concept and Coding*

  

## License

  

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details




