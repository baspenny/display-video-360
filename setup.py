import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="display-video-360",
    version="0.0.1",
    packages=setuptools.find_packages(),
    long_description_content_type="text/markdown",
    long_description=long_description,
    python_requires=">=3.7",
    install_requires=[
        "google-api-python-client",
        "httplib2",
        "oauth2client"
    ],
    url='https://github.com/baspenny/display-video-360'
)
