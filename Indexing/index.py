import os
import json
import pyterrier as pt
import pandas as pd
import numpy as np

# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the directory path relative to the script location
data_dir = os.path.abspath("./chocolate_crawler/Crawled/")

# List of JSON files
json_files = ['laderach.json', 'spruengli.json', 'maxchocolatier.json']

# Initialize an empty list to store data from all JSON files
all_data = []

# Load data from each JSON file
for json_file in json_files:
    json_path = os.path.join(data_dir, json_file)

    print(f"Loading data from {json_path}")

    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
            all_data.extend(data)
    except FileNotFoundError:
        print(f"File not found: {json_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {json_path}: {e}")

# print("Loaded data:")
# print(all_data)

# Extract relevant information
# texts = [
#     (item.get('description', '') if item.get('description', '') else '') + ' ' + 
#     (item.get('ingredients', '') if item.get('ingredients', '') else '') + ' ' + 
#     (item.get('allergens', '') if item.get('allergens', '') else '') + ' ' +
#     (item.get('price', '') if item.get('price', '') else '')
#     for item in all_data
# ]

# Extract relevant information
# texts = [
#     ' '.join(filter(None, [
#         item.get('description', ''),
#         item.get('ingredients', ''),
#         item.get('allergens', ''),
#         item.get('price', '')
#     ]))
#     for item in all_data
# ]

# Extract relevant information
texts = [
    ' '.join(filter(None, [
        item.get('description', ''),
        item.get('ingredients', ''),
        item.get('allergens', ''),
        item.get('price', '')
    ]))
    for item in all_data
]

# Create an index
idx = ['d' + str(i + 1) for i in range(len(texts))]

# Create a DataFrame
docs_df = pd.DataFrame(np.column_stack((idx, texts)), columns=['docno', 'text'])
# print(docs_df)

# Specify the index path relative to the script location
index_path = os.path.abspath("./index")
print(index_path)

# indexer = pt.DFIndexer(index_path, overwrite=True)
# index_ref = indexer.index(docs_df["text"], docs_df["docno"])
# index_ref.toString()

# Create a DataFrame
# docs_df = pd.DataFrame(np.column_stack((range(1, len(texts) + 1), texts)), columns=['docno', 'text'])

# Save DataFrame to a TREC-style file
# saves the indexing in the file
trec_file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./index/chocolate_index.csv")
docs_df.to_csv(trec_file_path, sep='\t', header=False, index=False)
# print(trec_file_path)


# Create a PyTerrier DFIndexer 
indexer = pt.DFIndexer(index_path, overwrite=True)
# indexer = pt.TRECCollectionIndexer(trec_file_path, verbose=True, blocks=False)
# indexer = pt.FilesIndexer("./index", verbose=True, blocks=False)

# Index the DataFrame
# index_ref = indexer.index(docs_df["text"], docs_df["docno"])

# Display the index reference
# print(index_ref.toString())

# Initialize PyTerrier
pt.init()

# Retrieve the index
index = pt.IndexFactory.of(index_ref)

# Perform a sample query
# query = "your query here"
result = pt.BatchRetrieve(index, wmodel="BM25")
result.search("chocolate")

# Print the result
print(result)
