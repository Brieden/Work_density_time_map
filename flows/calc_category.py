from dataflows import Flow, add_field
import math


def flow(parameters, datapackage, resources, stats):
    def find_category():
        def step(row):
            """ This function returns the must include common category per step/tile.
            In the future, because it's not yet implemented.
            """
            if row['B0896VZA'] is not None:
                if float(row['B0896VZA']) >= 3:
                    row['Category'] = 'WT1'
                else:
                    row['Category'] = 'WT2'

        return step

    return Flow(add_field('Category', 'string'), find_category())
