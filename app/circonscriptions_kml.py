import requests, zipfile, StringIO
from pykml import parser

r = requests.get('http://ftp.geogratis.gc.ca/pub/nrcan_rncan/vector/geobase_fed_cf/kml_fra/fed_cf_CA_2_1_kml_fr.kmz')
z = zipfile.ZipFile(StringIO.StringIO(r.content))

kml_str = z.read('doc.kml')

root = parser.fromstring(kml_str)

root