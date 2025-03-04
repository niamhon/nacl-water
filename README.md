# Supplementary data for a paper on the ion pairing of NaCl in water

This repository contains supplementary data supporting the findings of the paper:

"To pair or not to pair? Machine-learned explicitly-correlated electronic structure for NaCl in water"
Niamh O'Neill, Benjamin X Shi, Kara Fong, Angelos Michaelides, and Christoph Schran
[arXiv 2023](https://doi.org/10.48550/arXiv.2311.01527)

## License
The content of this repository is licensed under the CC-BY-SA-4.0 license. See the file `LICENSE` for details.

## Contents
* `models/*/final_model`:
All parameters of the C-NNP models for different electronic structure setups used
* `input`:
Example input file for CP2K simulations using the C-NNP model including the Coulomb baseline
* `data-sets`
Training sets for all models provided in both .xyz and .data formates. Also includes CP2K input file. BASIS also includes RI basis sets for RPA and MP2 calculations.

