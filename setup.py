from setuptools import setup

# List of dependencies installed via `pip install -e .`
# by virtue of the Setuptools `install_requires` value below.
requires = [
    'pyramid',
    'waitress',
    'pyramid_mongoengine',
    'pyramid_chameleon',
]


setup(
    name='ariel_mongo_pyramid',
    install_requires=requires,
    entry_points={
        'paste.app_factory': [
            'main = ariel_mongo_pyramid:main'
        ],
    },
)
