import json
import os
import tensorflow as tf


def ParsJson():
    file_path = './Json/ManualTruckLoading_20107.json'

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    with open(file_path, 'r') as file:
        parsed_data = json.load(file)
        print("file found")

    truck_number = parsed_data['truckNumber']
    truck_dimension = {item['key']: float(item['value']) for item in parsed_data['truckDimension']}
    total_used_skus = {item['skuName']: int(item['totalUsedSkusCount']) for item in parsed_data['totalUsedSkus']}
    skus_info_data = []

    for item in parsed_data['skusInfoData']:
        sku_info = {
            'skuName': item['skuName'],
            'skuLocalPosition': {pos['key']: float(pos['value']) for pos in item['skuLocalPosition']},
            'skuCoordinates': {coord['key']: float(coord['value']) for coord in item['skuCoordinates']}
        }
        skus_info_data.append(sku_info)

    print("Truck Number:", truck_number)
    print("Truck Dimension:", truck_dimension)
    print("Total Used SKUs:", total_used_skus)
    print("SKUs Info Data:",len( skus_info_data))

if __name__ == '__main__':
    ParsJson()
