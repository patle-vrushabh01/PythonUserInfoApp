import json
import os
import logging
from flask import Blueprint, jsonify, request, abort
from flasgger import swag_from

log = logging.getLogger(__name__)
api = Blueprint('api', __name__)


# Singleton CSV Object

def is_file_empty(file_path):
    return os.path.getsize(file_path) == 0


@api.route('/create-customer', methods=['Post'])
@swag_from("../swagger/create-customer.yaml")
# this function create customers
def create_customers():
    try:
        customer_name = request.args.get('customer_name')
        customer_email = request.args.get('customer_email')
        customer_id = request.args.get('customer_id')
        value = {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "customer_email": customer_email
        }

        file_name = "savedata.json"

        if is_file_empty(file_name):
            # the json file to save the output data
            save_file = open("savedata.json", "w")
            json.dump(value, save_file, indent=6)
            json_data = value
            save_file.close()

        else:
            with open(file_name) as fp:
                json_data = json.load(fp)

                if type(json_data) != list:
                    list_jsondata = [json_data]
                    list_jsondata.append(value)
                else:
                    list_jsondata = json_data
                    list_jsondata.append(value)

            f = open("savedata.json", "r+")

            # absolute file positioning
            f.seek(0)

            # to erase all data
            f.truncate()

            with open(file_name, 'w') as json_file:
                json.dump(list_jsondata, json_file, indent=6)
        return jsonify("Saved Successfully"), 200

    except Exception as e:
        abort(500, e)

#Get Customers
@api.route('/get-customers', methods=['GET'])
@swag_from("../swagger/get-customer.yaml")
# this function get customers
def get_customers():
    try:
        with open('savedata.json', 'r') as file:
            data = json.load(file)

        print(data)

    except Exception as e:
        abort(500, e)

    return jsonify(data), 200


def update_list_of_dictionaries(lst, search_key, search_value, customer_name, customer_email):
    for dictionary in lst:
        if dictionary.get(search_key) == search_value:
            for key in dictionary:
                if key == "customer_email":
                    dictionary[key] = customer_email
                if key == "customer_name":
                    dictionary[key] = customer_name


# Update Customers
@api.route('/update-customer', methods=['PUT'])
@swag_from("../swagger/update-customer.yaml")
def update_customer():
    try:
        customer_name = request.args.get('customer_name')
        customer_email = request.args.get('customer_email')
        customer_id = request.args.get('customer_id')
        with open('savedata.json', 'r') as file:
            data = json.load(file)

        json_data_list = data

        # Update dictionaries with a specific key-value pair
        update_list_of_dictionaries(json_data_list, 'customer_id', customer_id, customer_name, customer_email)

        with open("savedata.json", 'w') as json_file:
            json.dump(json_data_list, json_file, indent=6)
    except Exception as e:
        abort(500, e)

    return jsonify("updated"), 200


def delete_from_list_of_dictionaries(lst, search_key, search_value):
    lst[:] = [d for d in lst if d.get(search_key) != search_value]


# Delete Customers
@api.route('/delete-customers', methods=['DELETE'])
@swag_from("../swagger/delete-customers.yaml")
def delete_customers():
    try:

        customer_id = request.args.get('customer_id')
        with open('savedata.json', 'r') as file:
            data = json.load(file)

        json_data_list = data

        # Update dictionaries with a specific key-value pair
        delete_from_list_of_dictionaries(json_data_list, 'customer_id', customer_id)

        with open("savedata.json", 'w') as json_file:
            json.dump(json_data_list, json_file, indent=6)
    except Exception as e:
        abort(500, e)

    return jsonify("deleted"), 200
