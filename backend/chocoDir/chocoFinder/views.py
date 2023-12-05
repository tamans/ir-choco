# import os
from django.shortcuts import render
from django.http import HttpResponse
# import os
# import sys

# # Get the current script's directory
# current_dir = os.path.dirname(os.path.abspath(__file__))

# # Construct the path to Indexing directory
# indexing_dir = os.path.join(current_dir, '..', 'Indexing')
# indx = os.path.abspath('../.././Indexing')
# print("@@@index:",indx)

# # Add the Indexing directory to sys.path
# # sys.path.append(indx)
# # print("hell",sys.path)

# # Get the absolute path to the package directory
# package_path = os.path.abspath('../.././Indexing')

# # Add the package directory to the Python path
# sys.path.append(package_path)

# # Now you can import index_num.py
# # from index_num import create_index_and_search
# # from ....Indexing.index_num import create_index_and_search
# from .models import Chocolate
# from Indexing import index_num
# import csv

# def search_view(request):
#     if request.method == 'GET':
#         query = request.GET.get('q', '')

#         # Call the create_index_and_search function with the appropriate parameters
#         search_results = index_num.create_index_and_search(query)

#         # Assuming you have a template for displaying search results (e.g., search_results.html)
#         context = {'results': search_results, 'query': query}
#         return render(request, 'Results.vue', context)
