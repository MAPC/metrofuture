import os
from django.contrib.gis.utils import LayerMapping
from iamap.models import Municipality

town_mapping = {
    'muni_id': 'MUNI_ID',
    'name': 'NAME',
    'geometry': 'MULTIPOLYGON',
}

towns_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/towns_3857.shp'))
    
def load_towns(verbose=True):
    lm = LayerMapping(Municipality, towns_shp, town_mapping,
                      transform=False, source_srs=3857, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)  
