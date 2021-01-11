from dataflows import Flow, add_field, select_fields
import math


def flow(parameters, datapackage, resources, stats):

    return Flow(
        select_fields([
            'wkt', 'fill', 'fillColor', 'fillOpacity', 'stroke', 'color',
            'opacity', 'weight', 'radius'
        ]))