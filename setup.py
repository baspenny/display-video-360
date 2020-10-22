import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="k8s-secretgenerator",
    version="1.0.3",
    packages=setuptools.find_packages(),
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.7",
    install_requires=[],
    url='https://github.com/baspenny/k8s_secretgenerator'
)
