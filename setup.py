from setuptools import setup, find_packages


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='imagetiler',
    version='1.0',
    description='a python project for image tiler',
    long_description=readme(),
    long_description_content_type='text/markdown',
    author='Kris Shen',
    author_email='kris.shen.yang@gmail.com',
    url='https://www.github.com/xxx',
    packages=find_packages(exclude=['tests', 'tests.*']),
    test_suite='tests',
    install_requires=[
        'Pillow'
    ]
)
