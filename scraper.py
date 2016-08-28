from geojson_scraper import scrape


districts_url = "http://inspire.halton.gov.uk/geoserver/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3Apolling_districts&outputFormat=json"
council_id = 'E06000006'

scrape(districts_url, council_id, 'utf-8', 'districts')
