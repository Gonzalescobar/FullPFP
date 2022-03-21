from setuptools import find_packages, setup
setup(
    name='fullpfp',
    packages=find_packages(include=['fullpfp']),
    version='4.2.0',
    description='Get the full size ProFile Picture from any Instagram account.',
    author='Héctarea',
    license='MIT',
    install_requires=['beautifulsoup4==4.10.0', 'bs4==0.0.1', 'colorama==0.4.4', 'requests==2.26.0'],
)