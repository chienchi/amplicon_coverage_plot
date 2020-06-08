from setuptools import setup, find_packages
import sys

def get_version():
    sys.path.insert(0, "amplicon_coverage_plot")
    import version
    return version.__version__

setup(
    name='amplicon_coverage_plot',
    version= get_version(),
    author='Chienchi Lo',
    author_email='chienchi@lanl.gov',
    packages=find_packages(),
    scripts=['amplicon_coverage_plot/amplicon_coverage.py'],
    url='https://github.com/chienchi/amplicon_coverage_plot',
    license='LICENSE.txt',
    description='a script to generate amplicon coverage plot',
    keywords="amplicon genome coverage",
    long_description=open('README.md').read(),
    install_requires=[
        "plotly >=4.7.1",
        "numpy >= 1.15.1",
        "pysam >= 0.15.4",
    ],
)
