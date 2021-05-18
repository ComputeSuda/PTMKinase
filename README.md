# PTM Kinase

## Contents of PTMKinase

- [Overview](#overview)
- [Repo Contents](#repo-contents)
- [System Requirements](#system-requirements)
- [Installation Guide](#installation-guide)
  - [Dependencies](#dependencies)
  - [Download](#download)
- [Instructions for Use](#Instructions-for-Use)

## Overview

Post-translational modifications (PTMs) on protein contribute to variouse protein isoforms with
little evolutionary cost, regulating protein functions in cell signaling events and being involved 
in many diseases. The increasingly wealth of information on PTMs presents the challenge of 
understanding the dynamical properties of PTM sites, by which mechanism the allosteric regulation 
underlying PTMs would extremely enlarge the target space in drug design. Here, we integrate the 
sequence information, structural topology and in particular dynamics features to characterize the 
PTMs in the well known targets—kinase dataset. We demonstrate that machine learning can successfully
classify the PTM sites and active sites compared with other residues, especially with the dynamics 
features.
  
## Repo Contents

- [DL](DL): PTM prediction using deep learning method.
- [RF](RF): PTM prediction using random forest method.

For more details, please see each subfolder.

## System Requirements

All the calculations were done with Ubuntu 18.04.4 LST and python 3.7.7.

## Installation Guide

More details to run deep learning and random forests models can be found at the corresponding
folders.

## Instructions for Use

Mode details can be found at [DL](DL) and [RF](RF).

## Download

```
git@github.com:ComputeSuda/PTMKinase.git
```

# Citation

For usage of the package and associated manuscript, please cite according to the enclosed.
```
Sijie Yang, et al, PTM inspired drug design in kinase family
Characterization of structural dynamics of PTMs in kinase family, Journal Name, 
Date, Volume, Page. (to be updated)
```

This repository is distributed under [GNU General Public License v3.0](LICENSE).
