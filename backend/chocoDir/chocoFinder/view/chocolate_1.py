from django.http import JsonResponse
from ..models import Chocolate
import requests

def get_choco(request, query):
    # Make a request to the external API (replace 'API_ENDPOINT' with the actual API endpoint)
    api_url = f'http://127.0.0.1:8000/api/chocolate/get-choco/{query}/'
    response = requests.get(api_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        json_response = response.json()

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
    else:
        # Return an error JsonResponse if the external API request fails
        return JsonResponse({"error": "External API request failed"}, status=response.status_code)
