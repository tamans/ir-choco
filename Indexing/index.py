import pyterrier as pt
import os
import json
import pandas as pd
import numpy as np

def initialize_terrier():
    if not pt.started():
        pt.init()
    
    # Revert SSL configuration to default
    import ssl
    ssl._create_default_https_context = ssl.create_default_context

def load_data_from_json(data_dir, json_files):
    all_data = []
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
    
    return all_data


index_path = os.path.abspath('./Indexing/index')
save_path = os.path.abspath('./Indexing/index/choco.csv')

# def create_index_and_search(data_dir, json_files, query):
#     initialize_terrier()

#     all_data = load_data_from_json(data_dir, json_files)

#     # Create an index
#     idx = ['d' + str(i + 1) for i in range(len(all_data))]

#     # Extract relevant information
#     titles = [item.get('title', '') for item in all_data]
#     descriptions = [item.get('description', '') for item in all_data]
#     ingredients = [item.get('ingredients', '') for item in all_data]
#     allergens = [item.get('allergens', '') for item in all_data]
#     prices = [item.get('price', '') for item in all_data]

#     # Create a DataFrame
#     docs_df = pd.DataFrame(np.column_stack((idx, titles, descriptions, ingredients, allergens, prices)),
#                            columns=['docno', 'title', 'description', 'ingredients', 'allergens', 'price'])

#     docs_df.to_csv(save_path, index=False)

#     indexer = pt.DFIndexer(index_path, overwrite=True)
#     index_ref = indexer.index(docs_df["description"], docs_df["docno"])

#     index = pt.IndexFactory.of(index_ref)

#     print(index.getCollectionStatistics().toString())

#     br = pt.BatchRetrieve(index, wmodel="BM25")  # Alternative Models: "TF_IDF", "BM25"
#     results = br.search(query)
    
#     return results

# # Example usage
# data_dir = os.path.abspath("././chocolate_crawler/Crawled/")
# json_files = ['laderach.json', 'spruengli.json', 'maxchocolatier.json']
# query = "white chocolate CHF 20"

# search_results = create_index_and_search(data_dir, json_files, query)
# print(search_results)


def create_index_and_search(query):
    data_dir = os.path.abspath("./../chocolate_crawler/Crawled/")
    json_files = ['laderach.json', 'spruengli.json', 'maxchocolatier.json']
    
    initialize_terrier()

    all_data = load_data_from_json(data_dir, json_files)

    # Create an index
    idx = ['d' + str(i + 1) for i in range(len(all_data))]

    # Extract relevant information
    titles = [item.get('title', '') for item in all_data]
    descriptions = [item.get('description', '') for item in all_data]
    ingredients = [item.get('ingredients', '') for item in all_data]
    allergens = [item.get('allergens', '') for item in all_data]
    prices = [item.get('price', '') for item in all_data]

    # Create a DataFrame
    docs_df = pd.DataFrame(np.column_stack((idx, titles, descriptions, ingredients, allergens, prices)),
                           columns=['docno', 'title', 'description', 'ingredients', 'allergens', 'price'])

    save_path = os.path.abspath('./index/choco.csv')
    print(save_path)
    docs_df.to_csv(save_path, index=False)

    indexer = pt.DFIndexer(index_path, overwrite=True)
    index_ref = indexer.index(docs_df["description"], docs_df["docno"])

    index = pt.IndexFactory.of(index_ref)

    print(index.getCollectionStatistics().toString())

    br = pt.BatchRetrieve(index, wmodel="BM25")  # Alternative Models: "TF_IDF", "BM25"
    results = br.search(query)
    
    return results

# Example usage
query = "white chocolate CHF 20"
search_results = create_index_and_search(query)
print(search_results)
