import os
from validate_json import *

if __name__ == '__main__':
    json_doc_path = os.path.join(os.path.dirname(__file__), 'sample_doc', 'valid', 'TransactionEventResponse', 'TransactionEventResponse_2.txt')
    json_schema_path = os.path.join(os.path.dirname(__file__), 'sample_schema', 'TransactionEventResponse', 'TransactionEventResponse.json')

    # reading both files
    with open(json_doc_path, "r") as json_file, open(json_schema_path, "r") as schema_file:
        json_dta = json_file.read()
        schema_dta = schema_file.read()

    # function call
    validate_json(json_dta, schema_dta)
