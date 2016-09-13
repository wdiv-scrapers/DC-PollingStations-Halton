from dc_base_scrapers.geojson_scraper import GeoJsonScraper


districts_url = "http://inspire.halton.gov.uk/geoserver/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=inspire%3Apolling_districts&outputFormat=json"
council_id = 'E06000006'

districts_scraper = GeoJsonScraper(districts_url, council_id, 'utf-8', 'districts')
districts_scraper.scrape()
