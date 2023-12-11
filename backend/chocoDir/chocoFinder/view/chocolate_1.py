from django.http import JsonResponse
import requests
import logging
from .chocolate import Chocolate


def get_choco(request, query):
    api_url = f'http://127.0.0.1:8000/api/chocolate/get-choco/{query}/'
    response = requests.get(query)
    logging.info("Caioooooooooo")
    try:
        
        chocolates = []
        # response = requests.get(query)
        # json_response = response.json()
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
                
        #terteive docments based on docno
        # api_url = f'http://127.0.0.1:8000/api/chocolate/get-choco/{query}/'
    #     response = requests.get(query)
    #     print("CIAO")
    #     if response.status_code == 200:
    #         json_response = response.json()
    #         chocolates = []
    #         print(json_response)
    #         for docno in json_response.get("docno", []):
    #             try:
    #                 current_doc = Chocolate.objects.get(docno=docno)
    #                 chocolates.append({
    #                     'docno': current_doc.docno,
    #                     'title': current_doc.title,
    #                     'img_link': current_doc.image,
    #                     'description': current_doc.description,
    #                     'ingredients': current_doc.ingredients,
    #                     'allergens': current_doc.url,
    #                     'price': current_doc.price,
    #                 })
    #             except Chocolate.DoesNotExist as e:
    #                 logging.error(f"Chocolate with docno={docno} not found. Error: {e}")
    #             except Exception as e:
    #                 logging.error(f"An error occurred while processing docno={docno}: {e}")

    #         return JsonResponse({"documents": chocolates})
    #     else:
    #         return JsonResponse({"error": "External API request failed"}, status=response.status_code)

    # except Exception as e:
    #     logging.error(f"An error occurred: {e}")
    #     return JsonResponse({"error": "Internal Server Error"}, status=500)
