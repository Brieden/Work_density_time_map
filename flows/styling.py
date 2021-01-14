from dataflows import Flow, add_field

from util import *
import math


def flow(parameters, datapackage, resources, stats):
    style_dict = {
        "fill": "true",
        "fillColor": "#000000",
        "fillOpacity": "0.5",
        "stroke": "true",
        "color": "#232323",
        "opacity": "1.0",
        "weight": "1.0",
    }

    def set_default_style():
        """set all style defaults depending the category"""
        def step(row):
            for k, v in style_dict.items():
                row[k] = v

        return step

    def radius_by_column():
        def step(row):
            # linear sizing
            if False:
                row['radius'] = float(row['B08VZAT'])
            # linear sizing
            if True:
                row['radius'] = row['log_VZAT'] * 13
            #Set limits of radius

            row['radius'] = min([row['radius'], 50])
            row['radius'] = max([row['radius'], 2])

        return step

    return Flow(add_field('fill', 'string'), add_field('fillColor', 'string'),
                add_field('stroke', 'string'), add_field('color', 'string'),
                add_field('opacity', 'string'), add_field('weight', 'string'),
                add_field('radius', 'number'),
                add_field('fillOpacity', 'number'), set_default_style(),
                radius_by_column())
