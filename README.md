# amplicon_coverage_plot
[![DOI](https://zenodo.org/badge/270555241.svg)](https://zenodo.org/badge/latestdoi/270555241)
[![Build Status](https://travis-ci.org/chienchi/amplicon_coverage_plot.svg?branch=master)](https://travis-ci.org/chienchi/amplicon_coverage_plot)
[![codecov](https://codecov.io/gh/chienchi/amplicon_coverage_plot/branch/master/graph/badge.svg)](https://codecov.io/gh/chienchi/amplicon_coverage_plot)

The script will generate an [interactive barplot](https://chienchi.github.io/amplicon_coverage_plot/index.html) given amplicon info in bed/bedpe format and coverage information in cov/bam file.

## Dependencies

### Programming/Scripting languages
- [Python >=v3.7](https://www.python.org/)
    - The pipeline has been tested in v3.7.6

### Python packages
- [numpy >=1.15.1](http://www.numpy.org/) 
- [plotly >=4.7.1](https://plotly.com/python/)
- [pysam >= 0.15.4](https://github.com/pysam-developers/pysam)

### Third party softwares/packages
- [samtools >=1.9](http://www.htslib.org) - process bam file

## Installation

### Install by pip

```
pip install amplicov
```

### Install from source
Clone the `amplicon_coverage_plot` repository.

```
git clone https://github.com/chienchi/amplicon_coverage_plot
```

Then change directory to `amplicon_coverage_plot` and install.

```
cd amplicon_coverage_plot
python setup.py install
```

If the installation was succesful, you should be able to type `amplicon_coverage.py -h` and get a help message on how to use the tool.

```
amplicov -h
```


## Usage
```
usage: amplicov [-h] (--bed [FILE] | --bedpe [FILE])
                (--bam [FILE] | --cov [FILE]) [-o [PATH]] [-p [STR]]
                [--version]

Script to parse amplicon region coverage and generate barplot in html

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit

Amplicon Input (required, mutually exclusive):
  --bed [FILE]          amplicon bed file
  --bedpe [FILE]        amplicon bedpe file

Coverage Input (required, mutually exclusive):
  --bam [FILE]          bam file
  --cov [FILE]          coverage file [position coverage]

Output:
  -o [PATH], --outdir [PATH]
                        output directory
  -p [STR], --prefix [STR]
                        output prefix
```

## Test

```
cd tests
./runTest.sh
```

## Outputs 

-- prefix_amplicon_coverage.txt

| ID          | Whole_Amplicon | Unique  |
|-------------|----------------|---------|
| nCoV-2019_1 | 217.74         | 53.18   | 
| nCoV-2019_2 | 1552.83        | 1235.50 |
| nCoV-2019_3 | 3164.22        | 2831.73 |
| nCoV-2019_4 | 2005.16        | 1658.00 |
| etc...      |                |         |

#### Table Header Definition in the amplicon_coverage.txt 

<img width="481" alt="Screen Shot 2020-06-15 at 3 22 17 PM" src="https://user-images.githubusercontent.com/737589/84707575-2ef56280-af1c-11ea-8ccb-1857c1979900.png">

-- prefix_amplicon_coverage.html


<a href="https://chienchi.github.io/amplicon_coverage_plot/index.html">![html](https://user-images.githubusercontent.com/737589/84234283-2d0d4880-aab1-11ea-8d9d-40c78a0e6a85.png)</a>

