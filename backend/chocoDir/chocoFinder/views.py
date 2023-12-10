# views.py
from django.http import JsonResponse
from django.http import HttpResponseServerError
import requests
from .models import Chocolate
from chocoFinder.Indexing.index_num import create_index_and_search 

def index_and_search_chocolates(request, query):
    # try:
    # # Run the indexing script to create an index and search
        # search_results = create_index_and_search(query)

    #     # Save the search results to the Chocolate model
    #     chocolates = []
    #     for doc in search_results.scoredDocuments:
    #         chocolate = Chocolate(
    #             docno=doc.get("docno", ""),
    #             title=doc.get("title", ""),
    #             description=doc.get("description", ""),
    #             ingredients=doc.get("ingredients", ""),
    #             allergens=doc.get("allergens", ""),
    #             price=doc.get("price", ""),
    #         )
    #         chocolates.append(chocolate)

    #     # Bulk insert the records into the database
    #     Chocolate.objects.bulk_create(chocolates)

    #     # Return the search results as a JsonResponse
    #     return JsonResponse({"results": search_results.results, "chocolates": chocolates})
    # except Exception as e:
    #     # Handle exceptions and return an error response
    #     return HttpResponseServerError(f"An error occurred: {str(e)}")


    IP = "http://localhost:8000"
    print(f"QUERY ----------------> {query}")
    url = f"{IP}/search?query={query}"

    try:
        print(url)
        response = requests.get(url)
        response.raise_for_status()
    
        json_response = response.json()

        chocolates = []
        for docno in json_response["docno"].values():
            current_doc = Chocolate.objects.get(docno=docno)
            chocolates.append({
                'docno': current_doc.docno,
                'title': current_doc.title,
                'description': current_doc.description,
                'ingredients': current_doc.ingredients,
                'allergens': current_doc.url,
                'price': current_doc.price,
            })
            print(chocolates)
        return JsonResponse({"chococlates": chocolates})
    except requests.exceptions.RequestException as e:
        return JsonResponse({'error': str(e)}, status=500)