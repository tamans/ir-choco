import pyterrier as pt
import os
import json
import pandas as pd
import numpy as np

if not pt.started():
    pt.init()
    
# Revert SSL configuration to default uncomment when it gives ssl errors
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

def create_index(data_dir, index_filename):
    # data_dir = os.path.abspath("../../../chocolate_crawler/Crawled/")
    # json_files = ['laderach.json', 'spruengli.json', 'maxchocolatier.json']
    
    # initialize_terrier()

    all_data = load_data_from_json(data_dir, index_filename)

    # Create an index
    idx = ['d' + str(i + 1) for i in range(len(all_data))]

    # Extract relevant information
    titles = [item.get('title', '') for item in all_data]
    image = [item.get('img_link', '') for item in all_data]
    site = [item.get('page_link', '') for item in all_data]
    descriptions = [item.get('description', '') for item in all_data]
    ingredients = [item.get('ingredients', '') for item in all_data]
    allergens = [item.get('allergens', '') for item in all_data]
    prices = [item.get('price', '') for item in all_data]

    # Create a DataFrame
    docs_dict = {
        'docno': idx,
        'title': titles,
        'site': site,
        'img_link': image,
        'description': descriptions,
        'ingredients': ingredients,
        'allergens': allergens,
        'price': prices
    }
    
    return pd.DataFrame(docs_dict)

def search_index(query):
    try:
        reverse_index = pt.IndexFactory.of('./index')
        print(reverse_index)
        br = pt.BatchRetrieve(reverse_index, wmodel="BM25")
        results = br.search(query)
        print(reverse_index.getCollectionStatistics().toString())
        docnos = results['docno'].tolist()
        return docnos
    except Exception as e:
        print(f"Error during search: {e}")
        return []  


r = search_index("white chocolate")
print(r)



