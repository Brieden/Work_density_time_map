from dataflows import Flow, add_field
import math


def flow(parameters, datapackage, resources, stats):

    category_mapping_list = [
        {
            'cividi_category':
            'Sonstige Dienstleistungen',
            'bfs_categorys':
            [  # no in DB: 'B0844VZA', 'B0857VZA', 'B0876VZA', 'B0883VZA'
                'B0801VZA', 'B0802VZA', 'B0803VZA', 'B0835VZA', 'B0836VZA',
                'B0837VZA', 'B0841VZA', 'B0842VZA', 'B0850VZA', 'B0851VZA',
                'B0853VZA', 'B0858VZA', 'B0859VZA', 'B0860VZA', 'B0861VZA',
                'B0862VZA', 'B0863VZA', 'B0868VZA', 'B0869VZA', 'B0870VZA',
                'B0871VZA', 'B0875VZA', 'B0877VZA', 'B0878VZA', 'B0880VZA',
                'B0881VZA', 'B0882VZA', 'B0884VZA'
            ]
        },
        {
            'cividi_category':
            'Industrie & produzierendes Gewerbe',
            'bfs_categorys': [  # no in DB:'B0804VZA','B0840VZA',
                'B0805VZA', 'B0806VZA', 'B0807VZA', 'B0808VZA', 'B0810VZA',
                'B0811VZA', 'B0812VZA', 'B0813VZA', 'B0814VZA', 'B0815VZA',
                'B0816VZA', 'B0817VZA', 'B0818VZA', 'B0819VZA', 'B0820VZA',
                'B0821VZA', 'B0822VZA', 'B0823VZA', 'B0824VZA', 'B0825VZA',
                'B0826VZA', 'B0827VZA', 'B0828VZA', 'B0829VZA', 'B0830VZA',
                'B0831VZA', 'B0832VZA', 'B0833VZA', 'B0838VZA', 'B0839VZA',
                'B0852VZA'
            ]
        },
        {
            'cividi_category':
            'Finanzdienstleistungen',
            'bfs_categorys': [
                'B0843VZA', 'B0864VZA', 'B0865VZA', 'B0866VZA', 'B0895VZA',
                'B0896VZA'
            ]
        },
        {
            'cividi_category': 'Publikumsorientierte Nutzungen',
            'bfs_categorys': ['B0845VZA', 'B0846VZA', 'B0847VZA', 'B0849VZA']
        },
        {
            'cividi_category':
            'Freizeit, Gastronomie, Hotelerie',
            'bfs_categorys': [  # no in DB: 'B0848VZA', 'B0854VZA', 'B0889VZA',
                'B0855VZA', 'B0886VZA', 'B0887VZA', 'B0888VZA', 'B0890VZA',
                'B0892VZA'
            ]
        },
        {
            'cividi_category': 'Bildung & Forschung',
            'bfs_categorys': ['B0872VZA', 'B0873VZA', 'B0874VZA', 'B0885VZA']
        },
        {
            'cividi_category': 'Gesundheit & Soziale Einrichtungen',
            'bfs_categorys': ['B0894VZA']
        }
    ]

    def calc_new_category_score():
        """sum up the the values of bfs_categorys to store it in the representing cividi_category"""
        def step(row):
            for category in category_mapping_list:
                row[category['cividi_category']] = 0
                for bfs_category in category['bfs_categorys']:
                    row[category['cividi_category']] += float(
                        row[bfs_category])

        return step

    def calc_biggest_category():
        """find the biggest cividi_category per tile and store the name"""
        def step(row):
            biggest_category = {'name': '', 'VZA': 0}
            for category in category_mapping_list:
                if row[category['cividi_category']] >= biggest_category['VZA']:
                    biggest_category['name'] = category['cividi_category']
                    biggest_category['VZA'] = row[category['cividi_category']]
            row['biggest_category'] = biggest_category['name']

        return step

    return Flow(add_field('Sonstige Dienstleistungen', 'number'),
                add_field('Industrie & produzierendes Gewerbe', 'number'),
                add_field('Finanzdienstleistungen', 'number'),
                add_field('Publikumsorientierte Nutzungen', 'number'),
                add_field('Freizeit, Gastronomie, Hotelerie', 'number'),
                add_field('Bildung & Forschung', 'number'),
                add_field('Gesundheit & Soziale Einrichtungen', 'number'),
                calc_new_category_score(),
                add_field('biggest_category', 'string'),
                calc_biggest_category())
