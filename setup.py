from setuptools import setup, find_packages
import sys

setup(
    name='amplicon_coverage_plot',
    version= '0.1.0',
    author='Chienchi Lo',
    author_email='chienchi@lanl.gov',
    packages=find_packages(),
    scripts=['amplicov/amplicov'],
    url='https://github.com/chienchi/amplicon_coverage_plot',
    license='LICENSE.txt',
    description='script to generate amplicon coverage plot',
    keywords="amplicon genome coverage",
    long_description=open('README.md').read(),
    install_requires=[
        "plotly >=4.7.1",
        "numpy >= 1.15.1",
        "pysam >= 0.15.4",
    ],
)
