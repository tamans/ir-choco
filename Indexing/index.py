import pyterrier as pt
import json  
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
data_path = os.path.join(current_directory, "../chocolate_crawler/chocolates.json")
index_path = os.path.join(current_directory, "Indexing")

# Load the crawled data from the JSON file
with open(data_path, 'r', encoding='utf-8') as json_file:
    crawled_data = json.load(json_file)

# Initialize the index
indexer = pt.Indexer(index_path)

# Iterate over your crawled data and add documents to the index
for chocolate_info in crawled_data:
    # Assuming 'title' and 'description' are keys in chocolate_info
    doc = {'docno': chocolate_info.get('docno', ''),
           'title': chocolate_info.get('title', ''),
           'description': chocolate_info.get('description', '')}
    
    indexer.index(doc)

# Close the index
indexer.close()
