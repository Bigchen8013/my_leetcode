import requests

limit = 3
name = 'In the Name Of '
entity_ids = requests.get('https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=en&limit=' + str(limit) + '&search='+name).json()
print(entity_ids)
