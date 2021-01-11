from dataflows import Flow, add_field
import math


def flow(parameters, datapackage, resources, stats):
    def log_density():
        def step(row):
            if row['B08VZAT'] is not None:
                if float(row['B08VZAT']) > 1:
                    row['logVZAT'] = float(
                        round(math.log(float(row['B08VZAT'])))) * 6
                else:
                    row['logVZAT'] = 0

        return step

    return Flow(
        add_field('logVZAT', 'number'),
        log_density(),
    )
