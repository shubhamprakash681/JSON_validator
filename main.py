import json
import jsonschema
import os

def validate_json(json_data, schema_data):
    try:
        # loading JSON Schema
        schema = json.load(schema_data)

        # loading JSON doc
        doc = json.load(json_data)

        # creating validator
        validator = jsonschema.Draft7Validator(schema)

        # validating doc against schema
        errors = list(validator.iter_errors(doc))

        if not errors:
            print('Doc is Valid according to the schema')
        else:
            print('JSON doc is not valid. Errors: ')
            for err in errors:
                print(err.message)

    except json.JSONDecodeError as e:
        print('Error Decoding JSON: ', e)
    except Exception as e:
        print('Error: ', e)


if __name__ == '__main__':
    json_doc_path = os.path.join(os.path.dirname(__file__), 'sample_doc', 'valid', 'TransactionEventResponse', 'TransactionEventResponse.txt')
    json_schema_path = os.path.join(os.path.dirname(__file__), 'sample_schema', 'TransactionEventResponse', 'TransactionEventResponse.json')

    # reading both files
    with open(json_doc_path, 'r') as json_file, open(json_schema_path, 'r') as schema_file:
        json_data = json_file.read()
        schema_data = schema_file.read()

    # function call
    validate_json(json_data, schema_data)