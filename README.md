# patchclamp
Scripts for python analysis of patch-clamp recordings.

Currently contains:
- memtest.ipynb
- action_spectra.ipynb


## Installation

1. Clone the repo
```
$ git clone https://github.com/deisseroth-lab/patchclamp.git
$ cd patchclamp
```

2. Create conda environment
```
$ conda env create -f environment.yml
```
3. Activate the conda environment
```
$ conda activate patchclamp
```
4. Run the Jupyter notebooks (e.g.
```
$ jupyter-lab
```

## Reference for pyABF:
"Analysis of electrophysiological recordings was performed with custom software written for this project using Python 3.7 and the pyABF module¹."
[1] Harden, SW (2020). pyABF 2.2.3. [Online]. Available: https://pypi.org/project/pyabf/, Accessed on: Sep. 24, 2019.