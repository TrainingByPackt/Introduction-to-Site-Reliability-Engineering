#!/usr/bin/env python3
import csv
from flask import Flask
import yaml
import logging
from prettytable import from_csv
import json

# Instantiate a logger because we're taking user input and it can always go bad.
logger = logging.getLogger(__name__)

application = Flask(__name__)

@application.route('/list')
def list_items():
    item_table = from_csv(open('items.csv')).get_html_string()
    return item_table

@application.route('/list/json')
def list_json():
    with open('items.csv', 'r') as skufile:
        # read in all the values in the CSV file
        rowlist = csv.reader(skufile)
        # Skip the headers for our JSON
        next(rowlist)
        # Populate a dictionary with the values
        dict = {row[0]:[row[1],row[2],row[3]] for row in rowlist}
    return json.dumps(dict)

@application.route('/SKU/<sku>')
def list_item(sku: str) -> str:
    try:
        with open('items.csv', 'r') as skufile:
            # read in all the values in the CSV file
            rowlist = csv.reader(skufile)
            # Skip the headers for our JSON
            next(rowlist)
            # Populate a dictionary with the values
            dict = {row[0]:[row[1],row[2],row[3]] for row in rowlist}
            itemsummary = "{}: | Price: ${} | Cost Basis: {}".format(dict[sku][0], dict[sku][1], dict[sku][2])
    except KeyError as k:
        logger.error("Failed to load item {}!".format(k))
        itemsummary = "Error! Please try a numbered SKU!"
    return itemsummary

@application.route('/ping')
def health():
    return "OK"

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=80, debug=True)
