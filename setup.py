from setuptools import setup

setup(
   name='jsonbuilder',
   version='0.1',
   description='A module for converting Excel-like data to JSON',
   author='Oskar Petersen',
   author_email='oskar.petersen@trioptima.com',
   packages=['jsonbuilder'],
   install_requires=[
       'xlrd', 
       'pandas', 
       'asteval',
       'python-rapidjson',
       'pytest',
    ]
)