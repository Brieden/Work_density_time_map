from dataflows import Flow, add_field

from util import *
import math

default_dict = getting_dictionary('template/default_dict.txt')

def flow(parameters, datapackage, resources, stats):

    def category():
        def step(row):
            if (row['Category'] == 'WT1'):
                for k,v in default_dict[0].items():
                    row[k] = v
            elif (row['Category'] == 'WT2'):
                for k,v in default_dict[1].items():
                    row[k] = v
            elif (row['Category'] == 'WT3'):
                for k,v in default_dict[2].items():
                    row[k] = v
            elif (row['Category'] == 'WT4'):
                for k,v in default_dict[3].items():
                    row[k] = v
            elif (row['Category'] == 'WT5'):
                for k,v in default_dict[4].items():
                    row[k] = v
            elif (row['Category'] == 'WT6'):
                for k,v in default_dict[5].items():
                    row[k] = v
            else:
                for k,v in default_dict[0].items():
                    row[k] = 'undefinied'
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
