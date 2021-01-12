from dataflows import Flow, add_field
import math
import statistics


def flow(parameters, datapackage, resources, stats):
    def diversity():
        """
        Calc the diversity of existing categorys in a tile.
        To calc a score for diversity we use the popular diversity index in the ecological literature: Shannon-Index 
        https://en.wikipedia.org/wiki/Diversity_index#Shannon_index
        H'=-\sum _{i=1}^{R}p_{i}\ln p_{i}
        """
        categorys = [
            "Sonstige Dienstleistungen", "Industrie & produzierendes Gewerbe",
            'Finanzdienstleistungen', 'Publikumsorientierte Nutzungen',
            'Freizeit, Gastronomie, Hotelerie', 'Bildung & Forschung',
            'Gesundheit & Soziale Einrichtungen'
        ]

        def step(row):
            category_values = []
            for column in categorys:
                category_values.append(row[column])
            if sum(category_values) == 0:
                # no VZA existing, shannon-algorith would crash
                row['work_diversity'] = 0
            else:
                # calc shannon-score for a tile
                shannon_sum = 0
                for i in category_values:
                    p_i = i / sum(category_values) + 1e-10
                    shannon_sum += p_i * math.log(p_i)
                row['work_diversity'] = -shannon_sum

            # Limiting decimal points
            row['work_diversity'] = round(row['work_diversity'], 2)

        return step

    return Flow(
        add_field('work_diversity', 'number'),
        diversity(),
    )
