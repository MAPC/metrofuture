import os
from django.contrib.gis.utils import LayerMapping
from models import Municipality

town_mapping = {
    'muni_id': 'town_id',
    'name': 'name',
    'geometry': 'MULTIPOLYGON',
}

towns_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'C:/gis/greenstreets/towns.shp'))
    
def load_towns(verbose=True):
    lm = LayerMapping(Municipality, towns_shp, town_mapping,
                      transform=True, source_srs=26986, encoding='iso-8859-1')

    lm.save(strict=True, verbose=verbose)  
