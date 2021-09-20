import setuptools
from setuptools import setup

setup(
    name='drone-api-client',
    version='0.1',
    use_scm_version=False,
    description='Drone Api Python Client',
    author='Biriukov Maksym',
    author_email='maximbirukov77@gmail.com',
    url="https://github.com/Slamnlc/drone-api-client",
    download_url='https://github.com/Slamnlc/drone-api-client/archive/refs/tags/v0.1.tar.gz',
    packages=setuptools.find_packages(exclude=("tests", "dev_tools")),
    install_requires=[
        'requests'
    ],
    entry_points={
        "drone_api": [
            "drone-api-client = drone_api_client.drone_api_client",
        ]
    },
)
