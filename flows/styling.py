from dataflows import Flow, add_field

from util import *
import math

default_dict = getting_dictionary('template/default_dict.txt')


def flow(parameters, datapackage, resources, stats):
    def category():
        def step(row):
            if (row['Category'] == 'WT1'):
                for k, v in default_dict[0].items():
                    row[k] = v
            if (row['Category'] == 'WT2'):
                for k, v in default_dict[1].items():
                    row[k] = v
            row['radius'] = float(row['logVZAT'])

        return step

    return Flow(
        add_field('fill', 'string'),
        add_field('fillColor', 'string'),
        add_field('fillOpacity', 'string'),
        add_field('stroke', 'string'),
        add_field('color', 'string'),
        add_field('opacity', 'string'),
        add_field('weight', 'string'),
        add_field('radius', 'number'),
        category(),
    )
