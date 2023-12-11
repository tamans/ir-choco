from django.http import JsonResponse
import requests
import logging
from chocoFinder.models.chocolate import Chocolate
from chocoFinder.Indexing.index_num import search_index


def get_choco(request, query):

    api_url = f'http://127.0.0.1:8000/api/chocolate/get-choco/{query}/'
    response = requests.get(query)
    logging.info("Is it working??")
    try:
        
        chocolates = []
        docno = search_index(query)
        for d in docno:
            print("d:", d,"docno:", docno)
            if d == Chocolate.objects.get(docno=docno):
                chocolates.append({
                        'docno': d.docno,
                        'title': d.title,
                        'img_link': d.image,
                        'description': d.description,
                        'ingredients': d.ingredients,
                        'allergens': d.url,
                        'price': d.price,
                    })
                return JsonResponse({"chocolates": chocolates})
            else:
                return JsonResponse({"error": "External API request failed"}, status=response.status_code)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        return JsonResponse({"error": "Internal Server Error"}, status=500)
                
