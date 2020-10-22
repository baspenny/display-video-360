# Kubernetes Secret Generator

This package contains a nice and convienient class to create Kubernetes secret files  
It can create secrets from .env files or from files using the  
path of the file, and reading them.


## installation

```
pip install k8s-secretgenerator
```


## Examples

Below two examples. One for creation of secrets from files like eg. service account credentials or other files  
you want in a variable for Kubernetes.

The other one is an example to generate a secret file from a .env file.

All values will be base64 encoded, just the way Kubernetes likes them.

```python  
# Example:

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
```