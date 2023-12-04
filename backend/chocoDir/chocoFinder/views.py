import os
from django.shortcuts import render
from django.http import HttpResponse

from Indexing.index import create_index_and_search
from .models import Chocolate
import csv

def search_view(request):
    if request.method == 'GET':
        query = request.GET.get('q', '')

        # Call the create_index_and_search function with the appropriate parameters
        search_results = create_index_and_search(query)

        # Assuming you have a template for displaying search results (e.g., search_results.html)
        context = {'results': search_results, 'query': query}
        return render(request, 'search_results.html', context)
