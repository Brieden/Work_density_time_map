import json
import ast
import geopandas as gpd
import tempfile

def legend_reader(path):
    with open(path, 'r') as legend:
        document = json.load(legend)
        legend = document['views'][0]['spec']['legend']
    return legend

def translate(legend):
    custom_styles = [0 for x in range(len(legend))]
    for idx, leg in enumerate(legend):
        for k, v in leg.items():
            if k == 'label':
                custom_styles[idx]= (dict(label=v))
            elif k == 'fillColor':
                custom_styles[idx].update(fill='true', fillColor=v)
            elif k == 'fillOpacity':
               custom_styles[idx].update(fillOpacity=v)
            elif k == 'strokeColor':
               custom_styles[idx].update(stroke='true', strokeColor=v)
            elif k == 'strokeWidth':
               custom_styles[idx].update(weight=v)
            elif k == 'size':
                custom_styles[idx].update(radius=v)

    return custom_styles

def translate_marker(legend):
    custom_styles = [0 for x in range(len(legend))]
    for idx, leg in enumerate(legend):
        for k, v in leg.items():
            if k == 'label':
                custom_styles[idx]= (dict(label=v))
            elif k == 'fillColor':
                custom_styles[idx].update(fill='true', fillColor=v, markercolor=v)
            elif k == 'fillOpacity':
               custom_styles[idx].update(fillOpacity=v)
            elif k == 'strokeColor':
               custom_styles[idx].update(stroke='true', strokeColor=v)

    return custom_styles



def getting_dictionary(path):
    with open(path, 'r') as inFile:
        d = ast.literal_eval(inFile.read())
    return(d)

def bounds_to_set(bounds):
  if not isinstance(bounds, list):
    print('Unknown boundary format, ignoring')
    return None
  if bounds[0].startswith('geo:'):
    btl = bounds[0].strip('geo:').split(',')
    bbr = bounds[1].strip('geo:').split(',')
    return (
      float(btl[1].strip()),
      float(btl[0].strip()),
      float(bbr[1].strip()),
      float(bbr[0].strip()),
    )
  else:
    return set(bounds)

def set_to_bounds(bounds):
  if bounds is None: return []
  print("setting", bounds)
  return ['geo:%f,%f' % (bounds[1], bounds[0]), 'geo:%f,%f' % (bounds[3], bounds[2])]

def points_reduce(filename, factor=2):
  data = gpd.read_file(filename)
  newgp = data.copy().iloc[::factor, :]
  newgp.reindex()
  newfile = "output/temp.reduced.geojson"
  print('Writing 1/%d reduced data to' % factor, newfile)
  newgp.to_file(newfile, driver='GeoJSON')
  return newfile
