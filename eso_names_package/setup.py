from setuptools import setup, find_packages

setup(
    name='eso_names',
    version='0.2',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'filelock==3.13.1',
        'fsspec==2023.12.2',
        'Jinja2==3.1.3',
        'Levenshtein==0.23.0',
        'MarkupSafe==2.1.4',
        'mpmath==1.3.0',
        'networkx==3.2.1',
        'numpy==1.26.3',
        'pandas==2.2.0',
        'python-dateutil==2.8.2',
        'pytz==2023.3.post1',
        'rapidfuzz==3.6.1',
        'six==1.16.0',
        'sympy==1.12',
        'torch==2.1.2',
        'typing_extensions==4.9.0',
        'tzdata==2023.4',
    ],
)