from setuptools import setup, find_packages

setup(
    name='csv-into-db',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'psycopg2>=2.9.9'
    ],
    description='A package to convert the content of a .csv file into a PostgreSQL table using Python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='hsanfilippo',
    author_email='henrique.sanfilippo@gmail.com',
    url='https://github.com/hsanfilippo/csv-into-db',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
