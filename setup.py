from setuptools import find_packages, setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    long_description=long_description,
    long_description_content_type='text/markdown',
    name='fullpfp',
    packages=find_packages(include=['FullPFP']),
    version='4.21.1',
    description='Get the full size ProFile Picture from any Instagram account.',
    author='Héctarea',
    license='MIT',
    install_requires=['beautifulsoup4==4.10.0', 'bs4==0.0.1', 'colorama==0.4.4', 'requests==2.26.0'],
    author_email = 'gonzalescobar@gmail.com',
    url = 'https://hectarea.netlify.app/',
    keywords = ['Instagram', 'Scraping', 'Tool'],
    download_url= 'https://github.com/Hectarea/FullPFP/archive/refs/tags/v4.2.0.tar.gz',)