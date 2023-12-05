import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'choco.settings')  

django.setup()

from chocoFinder.models.chocolate import Chocolate

csv_file_path = os.path.abspath('./../../Indexing/index/chocolate.csv') 
print(csv_file_path)
chocolates = []

Chocolate.objects.all().delete()  

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        chocolate = Chocolate(
            docno=row['docno'],
            title=row['title'],
            description=row['description'],
            ingredients=row['ingredients'],
            allergens=row['allergens'],
            price=row['price']
        )
        chocolates.append(chocolate)

# Bulk insert the records into the database
Chocolate.objects.bulk_create(chocolates)

print('Chocolate added successfully')

# Retrieve the inserted objects
inserted_chocolates = Chocolate.objects.filter(docno__in=[choco.docno for choco in chocolates])

# Now, inserted_chocolates contains the Chocolate objects that were just inserted
for choco in inserted_chocolates:
    print(f"Inserted Chocolate: {choco.docno}, {choco.title}")