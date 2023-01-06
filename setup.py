from setuptools import setup

setup(
    name='dtopia',
    version='1.0.0',
    description='Dtopia Discord Tools',
    author='Toxbic',
    author_email='your@email.com',
    packages=['dtopia'],
    install_requires=[
        'requests',
        'websockets',
        'threading',
        'colorama',
    ],
)
