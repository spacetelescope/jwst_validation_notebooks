# JWST Validation Notebooks

[![Build Status](https://travis-ci.com/spacetelescope/jwst_validation_notebooks.svg?branch=master)](https://travis-ci.com/spacetelescope/jwst_validation_notebooks)
[![STScI](https://img.shields.io/badge/powered%20by-STScI-blue.svg?colorA=707170&colorB=3e8ddd&style=flat)](http://www.stsci.edu)


This repository contains *jupyter* notebooks that are used to perform validation testing of the [JWST Calibration Pipeline](https://jwst-pipeline.readthedocs.io/en/latest/jwst/introduction.html) (hereafter referred to as the calibration pipeline). These notebooks are structured to capture documentation, code, tests, figures, and other outputs that JWST instrument teams use to validate data from the calibration pipeline.

This repository is integrated with the [JWST pipeline software repository](https://github.com/spacetelescope/jwst) and the Jenkins automation server. To see most recent build status, go [here](https://plwishmaster.stsci.edu:8081/job/Notebooks/job/jwst_validation_notebooks_spacetelescope/).

## Current Validation Suite
To see the current suite of validation notebooks, visit our [website](https://jwst-validation-notebooks.stsci.edu/). Please note that the website is currently only available to internal STScI staff who are on the VPN. Contact Misty Cracraft ([@cracraft](https://github.com/cracraft)) or Alicia Canipe ([@aliciacanipe](https://github.com/aliciacanipe)) for questions or access issues.

## Executing Validation Notebooks Locally

### Install the JWST Calibration Pipeline ###
If you have not installed the calibration pipeline software, visit the [JWST pipeline software repository](https://github.com/spacetelescope/jwst#installation) for the most up-to-date installation instructions.

### CRDS Set-Up ###
Inside the STScI network, the pipeline works with the default CRDS setup with no modifications. To run it outside the network, CRDS must be configured according to the instructions [provided in the repository](https://github.com/spacetelescope/jwst#crds-setup).

### Notebook Kernel Set-Up ###
To activate and use your JWST conda environment in the notebook setting, you will need to install `nb_conda` and `ipykernel`:

```
conda install nb_conda
conda install ipykernel
```

### Obtaining a Local Copy of the Notebooks ###
Clone the repository:

```
git clone https://github.com/spacetelescope/jwst_validation_notebooks.git
cd jwst_validation_notebooks
```

### Opening and Running the Notebooks ###
Start *jupyter* with:

```
jupyter notebook
```    

This will open a *jupyter* instance in your web browser, where you can access the notebooks by selecting the `jwst_validation_notebooks` folder.

![Notebook Home](docs/static/notebook_home.png)

From there, you can select the specific testing directory and notebook. *jupyter* notebooks have an `.ipynb` extension.

### Selecting a Kernel ###
To change the kernel you are using, select the *Kernel* drop down button in the top left corner of the notebook and hover over "Change Kernel".

![Select Kernel](docs/static/kernel.png)

From there, you can select the *conda* environment kernel that includes your JWST pipeline installation. Then, you should be able to execute the notebook. For more information about *jupyter* notebooks, see the [Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/stable/). There is also a handy [cheat sheet](https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/) with shortcuts and commands.

### Running Notebooks with *nbpages* ###
If you would like to generate HTML outputs locally, make sure you are in the `jwst_validation_notebooks` repository and execute the following commands:

```
pip install nbpages
python convert.py
```

## Contributing ##

### New Notebooks ###
Prior to contributing to `jwst_validation_notebooks` development, please review our [style guide](https://github.com/spacetelescope/mirage/blob/master/style_guide/style_guide.md). Note that **notebook cell outputs must be cleared prior to submission**.

Make sure to follow the template outlined in our repository [here](https://github.com/spacetelescope/jwst_validation_notebooks/blob/master/jwst_validation_notebooks/templates/jwst_validation_notebook_template.ipynb). More information about storing test data is included below.

This repository operates using the standard [fork and pull request github](https://gist.github.com/Chaser324/ce0505fbed06b947d962) workflow. The following is a bare bones example of this work flow for contributing to the project:

1. Create a fork off of the `spacetelescope` `jwst_validation_notebooks` repository.
2. Make a local clone of your fork.
3. Ensure your personal fork is pointing `upstream` properly.
4. Create a branch on that personal fork.
5. Make your notebook changes and **be sure to clear the outputs from the cells**.
6. Push that branch to your personal GitHub repository (i.e. `origin`).
7. On the `spacetelescope` `jwst_validation_notebooks` repository, create a pull request that merges the branch into `spacetelescope:master`.
8. Assign a reviewer from the team for the pull request ([@cracraft](https://github.com/cracraft) or Alicia Canipe [@aliciacanipe](https://github.com/aliciacanipe)).
9. Iterate with the reviewer over any needed changes until the reviewer accepts and merges your branch.
10. Iterate with the reviewer over copying your test data into either Box or Artifactory.
10. Delete your local copy of your branch.

### New Test Data ###
If you have a notebook that uses updated test data or new test data, follow the steps below to request a data update.

#### Artifactory Workflow ####
Artifactory should be used for data that is for internal use only.

1. Create a [github Issue](https://github.com/spacetelescope/jwst_validation_notebooks/issues) requesting to have your data added to Artifactory, along with the pipeline step and location of the data. Once your data has been added to Artifactory, Misty Cracraft ([@cracraft](https://github.com/cracraft)) or Alicia Canipe ([@aliciacanipe](https://github.com/aliciacanipe)) will resolve the issue and notify you that your data is ready to be used (the full path to the data will be provided by the person who notified you that your data was ingested successfully).

2. Make sure you have the proper OS environmental variable set to access STScI's instance of Artifactory. This can be done via command line or put into a setup file like a ```.bash_profile``` file.

```
export TEST_BIGDATA=https://bytesalad.stsci.edu/artifactory/
```

3. Make sure your environment has ```ci_watson``` installed.
```
pip install ci_watson
```

4. In your notebook, import the ```ci_watson``` package needed.

```
from ci_watson.artifactory_helpers import get_bigdata
```

5. Read in each file stored in Artifactory (the full path should have been provided by the person who ingested the data).

```
satfile = get_bigdata('jwst_validation_notebooks',
                                     'validation_data',
                                     'jump',
                                    'jump_miri_test',
                                    'miri_sat_55k.fits')
```

6. Follow the normal workflow for contributing a notebook once you have confirmed that your notebook is running successfully.

#### Box Folder Workflow ####
Artifactory is only accessible to internal users on the STScI network. If you would like to contribute a test notebook that uses externally available data, this test data should be stored in a Box folder instead. The final workflow using Box is still in discussion, but for now you can use a Box folder with the correct permissions set up:

```
from astropy.utils.data import download_file

main_box_url ="https://data.science.stsci.edu/redirect/JWST/TSO/pipeline_testing_miri_ima_tso/"
filename = 'pipetest_miri_imtso_FULL_10g10i_F770W.fits'
file = download_file(mainurl+filename)
```

Box assigns a default alpha-numerical string as the filename, so you may want to update the filename before processing, or verify that the format is correct. Depending on the data, you can try:

```
# open file into correct format and write to local disk for processing
hdu = fits.open(file)
hdu.info()
hdu.writeto(filename)
```
or use a ```jwst datamodel```:

```
from jwst.datamodels import RampModel
model = RampModel(file)
model.save(filename)
```

## Code of Conduct
Users and contributors to the `jwst_validation_notebooks` repository should adhere to the [Code of Conduct](https://github.com/spacetelescope/mirage/blob/master/CODE_OF_CONDUCT.md).  Any issues or violations pertaining to the Code of Conduct should be brought to the attention of a `jwst_validation_notebooks` team member or to `conduct@stsci.edu`.


## Questions
For any questions about the `jwst_validation_notebooks` project or its software or documentation, please [open an Issue](https://github.com/spacetelescope/jwst_validation_notebooks/issues).


## Current Core Development Team
- Misty Cracraft [@cracraft](https://github.com/cracraft)
- Mees Fix [@mfixstsci](https://github.com/mfixstsci)
- Maria Pena-Guerrero [@penaguerrero](https://github.com/penaguerrero)
- Alicia Canipe [@aliciacanipe](https://github.com/aliciacanipe)
