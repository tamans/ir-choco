# views.py
from django.http import JsonResponse
from .models import Chocolate
from chocoFinder.Indexing.index_num import create_index_and_search  # Adjust the import path

def index_and_search_chocolates(request, query):
    # Run the indexing script to create an index and search
    search_results = create_index_and_search(query)

    # Save the search results to the Chocolate model
    chocolates = []
    for doc in search_results.scoredDocuments:
        chocolate = Chocolate(
            docno=doc.get("docno", ""),
            title=doc.get("title", ""),
            description=doc.get("description", ""),
            ingredients=doc.get("ingredients", ""),
            allergens=doc.get("allergens", ""),
            price=doc.get("price", ""),
        )
        chocolates.append(chocolate)

    # Bulk insert the records into the database
    Chocolate.objects.bulk_create(chocolates)

    # Return the search results as a JsonResponse
    return JsonResponse({"results": search_results.results, "chocolates": chocolates})
