from django.http import JsonResponse
from ..models import Chocolate
import requests


def get_choco(request, query):

    #jsonresponce will be the result of the indexing process
    chocolates = []
    for docno in json_response.get("docno", []):
        try:
            current_doc = Chocolate.objects.get(docno=docno)
            Chocolate.append({
                'docno': current_doc.docno,
                'name': current_doc.name,
                'url': current_doc.url,
                'ingredient': current_doc.tags,
                'price': current_doc.price,
            })
        except Chocolate.DoesNotExist:
            pass

    return JsonResponse({"documents": chocolates})
