from typing import List
import yaml
import base64
import os


class ManifestGenerator:
    """
    This class is a nice helper to create Kubernettes secret files
    It can create secrets from .env files or from files using the
    path of the file, and reading them

    Example:

        namespace = 'your-awesome-namespace'
        # Define file input
        credentials = [
            {
                'secret_name': 'google-credentials',
                'namespace': namespace,
                'type': 'Opaque',
                'input_files': [
                    {'name': 'service_account.json', 'path': './secrets/service_account.json'},
                ]
            }
        ]
        # Define env file input
        env_files = [
            {
                'secret_name': 'env-vars',
                'namespace': namespace,
                'type': 'Opaque',
                'input_file': '.env'
            }
        ]
        manifest_generator = ManifestGenerator(output_dir='secrets')

        manifest_generator.create_from_files(credentials)
        manifest_generator.create_from_env_files(env_files)
    """

    def __init__(self, output_dir):
        self.output_dir = output_dir

    def create_from_files(self, files: List[dict]):

        for file in files:
            res = {}
            for input_file in file.get('input_files'):
                base64_file_string = self.__create_base_encoded_str_from_path(input_file.get('path'))
                res.update({input_file.get('name'): base64_file_string})

            secrets_yaml = {
                'apiVersion': 'v1',
                'kind': 'Secret',
                'data': res,
                'type': file.get('type'),
                'metadata': {
                    'name': file.get('secret_name'),
                    'namespace': file.get('namespace')
                }
            }
            yaml_dump = yaml.dump(secrets_yaml)
            with open(os.path.join(f'{self.output_dir}', f'secrets-{file.get("secret_name")}.yaml'), 'w') as fh:
                fh.write(yaml_dump)

    def create_from_env_files(self, secrets_yaml_files_to_create: List[dict]):
        import yaml
        for secret in secrets_yaml_files_to_create:
            secret_name = secret.get('secret_name')
            namespace = secret.get('namespace')
            type = secret.get('type')
            input_file = secret.get('input_file')

            res = self.__create_dict_from_env_vars(input_file)

            secrets_yaml = {
                'apiVersion': 'v1',
                'kind': 'Secret',
                'data': res,
                'type': type,
                'metadata': {
                    'name': secret_name,
                    'namespace': namespace
                }
            }
            yaml_dump = yaml.dump(secrets_yaml)
            with open(os.path.join(f'{self.output_dir}', f'secrets-{secret_name}.yaml'), 'w') as fh:
                fh.write(yaml_dump)

    def __create_base_encoded_str_from_path(self, path: str) -> str:
        with open(path, 'r') as fh:
            str = fh.read()
        value_bytestring = str.encode('ascii')
        value_bytestring_base64 = base64.b64encode(value_bytestring)
        value = value_bytestring_base64.decode('ascii')

        return value

    def __create_dict_from_env_vars(self, input_file):
        res = {}
        with open(input_file) as fh:
            content = fh.readlines()

            for line in content:
                splitted_line = line.split('=')

                key = splitted_line[0]

                if len(splitted_line) > 2:
                    value = ''
                    for i, val in enumerate(splitted_line):
                        if i > 0:
                            value += f'={val}'
                    value = value[1:]
                    print(value)
                else:
                    value = splitted_line[1].strip('\n')

                value_bytestring = value.encode('ascii')
                value_bytestring_base64 = base64.b64encode(value_bytestring)
                value = value_bytestring_base64.decode('ascii')
                res.update({key: value})

        return res
