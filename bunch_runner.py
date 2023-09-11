import os
from validate_json import *


if __name__ == '__main__':
    base_path = os.path.dirname(__file__)

    sample_schema_list = os.listdir(os.path.join(base_path, 'sample_schema'))
    for schema_type in sample_schema_list:
        json_schema_path = os.path.join(base_path, 'sample_schema', schema_type, f'{schema_type}.json')

        # valid docs
        doc_list = os.listdir(os.path.join(base_path, 'sample_doc', 'valid', schema_type))
        for doc_path in doc_list:
            json_doc_path = os.path.join(base_path, 'sample_doc', 'valid', schema_type, doc_path)

            # reading both files
            with open(json_doc_path, "r") as json_file, open(json_schema_path, "r") as schema_file:
                json_dta = json_file.read()
                schema_dta = schema_file.read()

            # function call
            validate_json(json_dta, schema_dta)

        # invalid docs
