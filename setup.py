from setuptools import setup, find_packages
import sys

setup(
    name='amplicov',
    version= '0.3.4',
    author='Chienchi Lo',
    author_email='chienchi@lanl.gov',
    packages=find_packages(),
    scripts=['amplicov/amplicov'],
    url='https://github.com/chienchi/amplicon_coverage_plot',
    license='LICENSE.txt',
    description='script to generate amplicon coverage plot',
    keywords="amplicon genome coverage",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        "plotly >=4.7.1",
        "numpy >= 1.15.1",
        "pysam >= 0.15.4",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
