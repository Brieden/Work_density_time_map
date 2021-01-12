from dataflows import Flow, add_field
import math


def flow(parameters, datapackage, resources, stats):
    def log_density():
        def step(row):
            if float(row['B08VZAT']) > 1:
                row['log_VZAT'] = math.log(float(row['B08VZAT'])) * 6
            else:
                row['log_VZAT'] = 0

            # Limiting decimal points
            row['log_VZAT'] = round(row['log_VZAT'], 2)

        return step

    return Flow(
        add_field('log_VZAT', 'number'),
        log_density(),
    )
