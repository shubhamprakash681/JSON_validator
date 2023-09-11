import json
import jsonschema

def validate_json(json_data, schema_data):
    try:
        # Load the JSON schema
        schema = json.loads(schema_data)

        # Load the JSON document
        document = json.loads(json_data)

        # Create a JSONSchema validator
        validator = jsonschema.Draft7Validator(schema)

        # Validate the JSON document against the schema
        errors = list(validator.iter_errors(document))
        if not errors:
            print("JSON document is valid according to the JSON Schema.")
        else:
            print("JSON document is NOT valid according to the JSON Schema. Errors:")
            for error in errors:
                print(error.message)

    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
    except Exception as e:
        print("Error:", e)

# Specify the paths to your JSON document and JSON Schema files
json_document_path = "TransactionEventRequest_2.txt"
json_schema_path = "TransactionEventRequest.json"

# Read the JSON document and JSON Schema files
with open(json_document_path, "r") as json_file, open(json_schema_path, "r") as schema_file:
    json_data = json_file.read()
    schema_data = schema_file.read()

# Validate the JSON document with the JSON Schema
validate_json(json_data, schema_data)
