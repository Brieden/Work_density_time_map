from dataflows import Flow, add_field
import math

def flow(parameters, datapackage, resources, stats):

    def apartment():
        def step(row):
            if row['max_number'] is not None:
                if row['WT1'] == row['max_number']:
                    row['Category'] = 'WT1'   
                elif row['WT2'] == row['max_number']:
                    row['Category'] = 'WT2'
                elif row['WT3'] == row['max_number']:
                    row['Category'] = 'WT3'
                elif row['WT4'] == row['max_number']:
                    row['Category'] = 'WT4'
                elif row['WT5'] == row['max_number']:
                    row['Category'] = 'WT5'
                else:
                    row['Category'] = 'WT6'
        return step

    return Flow(
        add_field('Category', 'string'),
        apartment()
    )
