# IR-choco
Authors:
- Foteini Rorri
- Sara Liberi
- Sapana Tamang


# Crawlers

- https://laderach.com/ch-en
- https://en.maxchocolatier.com/
- https://www.spruengli.ch/en/shop.html

```
scrapy crawl name_spider -o name.json
```

# Frontend 

If you have problems starting the frontend do 

```
yarn add --dev @vue/cli
```

# Backend

If you change anything in the models you have to run 

```
python3 manage.py
```

```
Start server:
./manage.py runserver
./manage.py makemigrations
./manage.py migrate
```


chocoDir
```
export DJANGO_SETTINGS_MODULE=choco.settings
python3 index_parser.py
```

if in Backend chocoDir, ModuleNotFoundError: No module named 'corsheaders'
```
pip install django-cors-headers
```
