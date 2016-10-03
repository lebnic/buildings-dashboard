import pandas as pd
from app import app

@app.route('/')
@app.route('/index')
def index():
    url = 'http://donnees.ville.montreal.qc.ca/dataset/772087ee-e11f-42a8-ab6b-a175d6c6e249/resource/9d77d85a-f54c-408a-b6ff-3d847c05b2e0/download/sause01direction01directiondonneesouvertesbatimentsvacantsbatimentsvacantsvm2015.csv'
    buildings = pd.read_csv(url, sep = ',')
    locations = buildings[['COMPLET','LATITUDE','LONGITUDE','ID']].to_json(orient='values')
    html_string = '''
    <!DOCTYPE html>
    <html> 
    <head> 
      <meta http-equiv="content-type" content="text/html; charset=UTF-8" /> 
      <title>Google Maps Multiple Markers</title> 
      <script src="http://maps.google.com/maps/api/js?sensor=false" 
              type="text/javascript"></script>
    </head> 
    <body>
      <div id="map" style="width: 500px; height: 400px;"></div>

      <script type="text/javascript">
      
        var locations = ''' + locations + ''';

        var map = new google.maps.Map(document.getElementById('map'), {
          mapTypeId: google.maps.MapTypeId.ROADMAP
        });

        var infowindow = new google.maps.InfoWindow();

        var marker, i;

        var bounds = new google.maps.LatLngBounds();
        
        
        for (i = 0; i < locations.length; i++) {
          bounds.extend(new google.maps.LatLng(locations[i][1], locations[i][2]));
          marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map
          });

          google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
              infowindow.setContent(locations[i][0]);
              infowindow.open(map, marker);
            }
          })(marker, i));
        }
        
        map.fitBounds(bounds);
        
      </script>
    </body>
    </html>
    '''
    return html_string