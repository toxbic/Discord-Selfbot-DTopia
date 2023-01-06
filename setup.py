from setuptools import setup,find_packages

setup(
    name='dtopia',
    version='1.0.0',
    description='Dtopia Discord Tools',
    author='Toxbic',
    author_email='your@email.com',
    packages=find_packages(),
    install_requires=[
        'requests',
        'websockets',
        'colorama',
    ],
    entry_points={
        'egg_info.writers': [
            'dtopia.egg_info',
        ],
    },
)
