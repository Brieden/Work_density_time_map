from dataflows import Flow, add_field

from util import *
import math

default_style_dict = getting_dictionary('template/default_dict.json')


def flow(parameters, datapackage, resources, stats):
    def style_by_category():
        """set all style defaults depending the category"""
        def step(row):
            for style in default_style_dict:
                if (row['biggest_category'] == style['category']):
                    for k, v in style.items():
                        if k != 'category':
                            row[k] = v

        return step

    def radius_by_column():
        def step(row):
            # linear sizing
            if True:
                row['radius'] = float(row['B08VZAT']) / 20
            # linear sizing
            if False:
                row['radius'] = float(row['log_VZAT'])
            #Set limits of radius
            row['radius'] = min([row['radius'], 50])
            row['radius'] = max([row['radius'], 5])

        return step

    def fillOpacity_by_column():
        def step(row):
            row['fillOpacity'] = (row['work_diversity'] / 1.5) + 0.1

        return step

    return Flow(add_field('fill', 'string'), add_field('fillColor', 'string'),
                add_field('stroke', 'string'), add_field('color', 'string'),
                add_field('opacity', 'string'), add_field('weight', 'string'),
                add_field('radius', 'number'),
                add_field('fillOpacity', 'number'), style_by_category(),
                radius_by_column(), fillOpacity_by_column())
