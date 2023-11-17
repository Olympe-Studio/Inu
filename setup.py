from setuptools import setup, find_packages


with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='inu',
    version='1.0.0',
    packages=find_packages(),
    install_requires=required,
    entry_points={
        'console_scripts': [
            'inu=main:cli'
        ]
    },
)
