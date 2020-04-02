#!/usr/bin/env python3

"""
Script that reads information from the KiwiBuild website.
Hopefully will make finding a house easier.
"""

import json


def print_extract(filename):
    """Open the extract file and prettyprint it"""
    with open(filename, 'r') as file:
        extract_raw = file.read()
        extract_json = json.loads(extract_raw)
        print(json.dumps(extract_json, indent=4, sort_keys=True))

#print_extract('extract.json')


def print_records(filename):
    """Open the extract file and iterate through the record objects"""
    with open(filename, 'r') as file:
        extract_raw = file.read()
        extract_json = json.loads(extract_raw)
        record_count = 0

        # Iterate through json object and print stuff
        for record in extract_json['Records']:
            development_id = ''
            property_name = ''
            bedrooms = ''
            property_type = ''
            price = ''
            record_count += 1
            for attribute in record['Attributes']:
                if attribute['Name'] == 'kbnz_developmentid':
                    development_id = attribute['DisplayValue']
                elif attribute['Name'] == 'kbnz_propertyname':
                    property_name = attribute['DisplayValue']
                elif attribute['Name'] == 'kbnz_propertytype':
                    property_type = attribute['DisplayValue']
                elif attribute['Name'] == 'kbnz_numberofbedrooms':
                    bedrooms = attribute['DisplayValue']
                elif attribute['Name'] == 'kbnz_price':
                    price = attribute['DisplayValue']
            print(f'{property_name} {development_id}, {bedrooms} bdrm {property_type}: {price}')


    print(f'Record count: {record_count}')

print_records('extract.json')
