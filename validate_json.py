import json
import jsonschema


def validate_json(json_data, schema_data):
    try:
        # loading JSON Schema
        schema = json.loads(schema_data)

        # loading JSON doc
        doc = json.loads(json_data)

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
        print("Error decoding JSON:", e)
    except Exception as e:
        print("Error:", e)