import yaml
import json
import geopandas as gpd

gdf = gpd.read_file('output/ZHR3/clear_result3.csv')
gdf.to_file("output/ZHR3/preview.geojson", driver='GeoJSON')
# minx, miny, maxx, maxy = gdf.geometry.total_bounds
# bbox = [minx, miny, maxx, maxy]
# ['geo:%f,%f' % (bounds[1], bounds[0]), 'geo:%f,%f' % (bounds[3], bounds[2])]

with open("output/ZHR3/datapackage.json", 'r') as j, \
     open("output/ZHR3/preview.geojson", 'r') as l, \
     open("output/ZHR3/snapshot.json", 'w') as r:
    data = json.load(j)
    feed = json.load(l)
    data["resources"] = [{"name": "data-layer", "mediatype": "application/vnd.simplestyle-extended", "data": {"name": "data", "type": "FeatureCollection", "features": []}},{"name": "mapbox-background", "path": "mapbox://styles/gemeindescan/ck6rp249516tg1iqkmt48o4pz", "mediatype": "application/vnd.mapbox-vector-tile", "data":"" }]
  #  data['resources'] = '''[{name:mapbox-background, "path": "mapbox://styles/gemeindescan/ck6rp249516tg1iqkmt48o4pz", "mediatype": "application/vnd.mapbox-vector-tile", "data": null},{"name": "data-layer", "mediatype": "application/geo+json", "data": {"name": "data", "type": "FeatureCollection", "features": null}}]'''
    data['resources'][0]['data']['features'] = feed['features']
#    data['views'][0]['spec']['bounds'] = bbox
#    data['resources'][1]['data'] = null
    json.dump(data, r)  
