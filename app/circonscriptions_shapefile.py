import pudb; pu.db
import pandas as pd
import xml.etree.ElementTree as ET
import requests, zipfile, StringIO
import shapefile

r = requests.get('http://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/geobase_fed_cf/shp_eng/fed_cf_CA_2_1_shp_en.zip')
z = zipfile.ZipFile(StringIO.StringIO(r.content), 'r')

z.extractall()
z.close()

sf = shapefile.Reader('FED_CA_2_1_en.shp')

print(sf.fields)