import json
import records


zones = []

with open('cosmogony_fr.json', 'r') as file_i:
    tt = json.load(file_i)
    zones = tt['zones']

db = records.Database('postgres://ubuntu:-ubuntu-@localhost:12345/vtile')

for a_zone in zones:
     if a_zone['admin_level'] == 8:
         db.query('INSERT INTO ogrgeojson (id, admin_type, admin_level, geometry, parent, name) VALUES(:id, :admin_type, :admin_level, :geometry, :parent, :name)',
            id=a_zone['id'], admin_type=a_zone['zone_type'], admin_level=a_zone['admin_level'], geometry=str(a_zone['geometry']), parent=a_zone['parent'], name=a_zone['name'] )
db.query('update ogrgeojson set wkb_geometry = ST_SetSRID(ST_GeomFromGeoJSON(geometry),4326)')
db.query('SELECT UpdateGeometrySRID("ogrgeojson","wkb_geometry",4326)');
