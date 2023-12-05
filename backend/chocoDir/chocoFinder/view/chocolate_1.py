
from django.http import JsonResponse
from ..models import Chocolate
import requests

def get_choco(request, query):
    # Fetch or obtain the JSON response containing 'docno' values
    # For example, assuming you have a URL that provides the JSON response:
    json_url = 'http://example.com/your_json_endpoint'
    json_response = requests.get(json_url).json()

    # Initialize the chocolates list
    chocolates = []

    # Iterate through docno values in the JSON response
    for docno in json_response.get("docno", []):
        try:
            # Retrieve Chocolate object based on docno
            current_doc = Chocolate.objects.get(docno=docno)

            # Append details to the chocolates list
            chocolates.append({
                'docno': current_doc.docno,
                'name': current_doc.name,
                'url': current_doc.url,
                'ingredient': current_doc.tags,
                'price': current_doc.price,
            })
        except Chocolate.DoesNotExist:
            pass

    # Return JsonResponse with the list of chocolates
    return JsonResponse({"documents": chocolates})
