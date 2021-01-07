from dataflows import Flow, add_field
import math

def flow(parameters, datapackage, resources, stats):

    def apartment():
        def step(row):
            if row['max_number'] == row['WT1']:
                row['Category'] = 'WT1'   
            elif row['max_number'] == row['WT2']:
                row['Category'] = 'WT2'
            elif row['max_number'] == row['WT3']:
                row['Category'] = 'WT3'
            elif row['max_number'] == row['WT4']:
                row['Category'] = 'WT4'
            elif row['max_number'] == row['WT5']:
                row['Category'] = 'WT5'
            elif row['max_number'] == row['WT6']:
                row['Category'] = 'WT6'
            else: 
                row['Category'] = 'undefinied'
        return step

    return Flow(
        add_field('Category', 'string'),
        apartment()
    )
