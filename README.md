# JWST Validation Notebooks

[![Build Status](https://travis-ci.com/spacetelescope/jwst_validation_notebooks.svg?branch=master)](https://travis-ci.com/spacetelescope/jwst_validation_notebooks)
[![STScI](https://img.shields.io/badge/powered%20by-STScI-blue.svg?colorA=707170&colorB=3e8ddd&style=flat)](http://www.stsci.edu)


This repository contains [*jupyter*][jupyter] notebooks that are used to
perform validation testing of the
[JWST Calibration Pipeline](https://jwst-pipeline.readthedocs.io/en/latest/jwst/introduction.html)
(hereafter referred to as the calibration pipeline). These notebooks are structured to
capture documentation, code, tests, figures, and other outputs that JWST instrument teams
use to validate data from the calibration pipeline.

This repository is integrated with the
[JWST pipeline software repository](https://github.com/spacetelescope/jwst) and the
Jenkins automation server. To see most recent build status, go to the
[STScI Jenkins server](https://plwishmaster.stsci.edu:8081/job/Notebooks/job/jwst_validation_notebooks_spacetelescope/).

## Current Validation Suite

To see the current suite of validation notebooks, visit our
[website](https://jwst-validation-notebooks.stsci.edu/). Please note that the website is
currently only available to internal STScI staff who are on the VPN. Contact Misty
Cracraft ([@cracraft](https://github.com/cracraft)) or Alicia Canipe
([@aliciacanipe](https://github.com/aliciacanipe)) for questions or access issues.

## Executing Validation Notebooks Locally

You must be an internal user in order to execute the Validation Notebooks locally, because
the test data is only available internally. In order to execute the notebooks or test a
new notebook, you can use the following setup:

1. Clone the validation notebooks repository: `git clone https://github.com/spacetelescope/jwst_validation_notebooks.git`
2. Open a terminal window into the newly created directory
3. Create the Validation Notebooks conda environment: `source setup_environment.sh`

You should now be able to run the notebooks with jupyter (type `jupyter notebook`), or
test the creation and running of the test suite by typing `python convert.py`.

## Opening and Running the Notebooks ##

### Starting the Jupyter server ###

Start [*jupyter*][jupyter] with:

```
jupyter notebook
```

This will open a [*jupyter*][jupyter] instance in your web browser, where you can access
the notebooks by selecting the `jwst_validation_notebooks` folder.

![Notebook Home](docs/static/notebook_home.png)

From there, you can select the specific testing directory and notebook.
[*jupyter*][jupyter] notebooks have an `.ipynb` extension.

### Selecting a Kernel ###

To change the kernel you are using, select the *Kernel* drop down button in the top left
corner of the notebook and hover over "Change Kernel".

![Select Kernel](docs/static/kernel.png)

From there, you can select the [*conda*][conda] environment kernel that includes your
JWST pipeline installation. Then, you should be able to execute the notebook. For more
information about [*jupyter*][jupyter] notebooks, see the
[Jupyter Notebook documentation](https://jupyter-notebook.readthedocs.io/en/stable/).
There is also a handy [cheat sheet](https://cheatography.com/weidadeyue/cheat-sheets/jupyter-notebook/pdf_bw/)
with shortcuts and commands.

### Running Notebooks with *nbpages* and `convert.py` ###

If you would like to generate HTML outputs locally, make sure you are in the
`jwst_validation_notebooks` repository and execute the following commands:

```
python convert.py
```

In order to get a full list of run instructions, run

```
python convert.py --help
```

There are, however, a few flags that could be especially useful, and a few notes about
`convert.py` which need to be kept in mind.

* In the main notebook directory is a file named `exclude_notebooks`. This file is
  currently passed to the `--exclude` flag if that flag is not set at the command line.
  As such, it is not currently possible to use the `--include` flag when running from the
  main notebook directory.
* To run a subset of notebooks, use some combination of the `--notebook-path` command-line
  option to only run the notebooks in a particular directory and the `--exclude` option to
  avoid running particular individual notebooks.

## Contributing ##

### New Notebooks ###

Prior to contributing to `jwst_validation_notebooks` development, please review our
[style guide](https://github.com/spacetelescope/mirage/blob/master/style_guide/style_guide.md).
Note that **notebook cell outputs must be cleared prior to submission**.

Make sure to follow the template outlined in
[our repository](https://github.com/spacetelescope/jwst_validation_notebooks/blob/master/jwst_validation_notebooks/templates/jwst_validation_notebook_template.ipynb).
More information about storing test data is included below.

Before your notebook will be accepted, you must test it in the proper environment
described in the [Executing Validation Notebooks Locally](https://github.com/spacetelescope/jwst_validation_notebooks#executing-validation-notebooks-locally)
section above. This will help ensure a smoother delivery of new tests.

This repository operates using the standard
[fork and pull request github](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
workflow. The following is a bare bones example of this work flow for contributing to the
project:

1.  [Create a fork][github_fork] off of the `spacetelescope` `jwst_validation_notebooks`
    repository.
2.  Make a local clone of your fork.
3.  Ensure your personal fork [is pointing `upstream` properly][github_upstream].
4.  [Create a branch][github_branch] on that personal fork.
5.  Make your notebook changes and **be sure to clear the outputs from the cells**.
6.  Push that branch to your personal GitHub repository (i.e. `origin`).
7.  On the `spacetelescope` `jwst_validation_notebooks` repository, create a pull request
    that merges the branch into `spacetelescope:master`.
8.  Ensure that the pull request passes the continuous integration check.
9.  Assign a reviewer from the team for the pull request
    (Misty Cracraft [@cracraft](https://github.com/cracraft) or Alicia Canipe
    [@aliciacanipe](https://github.com/aliciacanipe)).
10. Iterate with the reviewer over any needed changes until the reviewer accepts and
    merges your branch.
11. Iterate with the reviewer over copying your test data into either Box or Artifactory.
12. Delete your local copy of your branch.

### Temporary Directory ###

In order to avoid conflicts between multiple notebooks in the same directory (especially
when being run by an automated process), the template notebook contains a cell that sets
up a temporary directory and moves the notebook execution into that directory. Even if
you don't start your notebook as a copy of the template, you should copy this cell. For
development purposes, you may wish to set the `use_tempdir` variable to False, but when
you are ready to submit the notebook in a pull request, please change it to True.

### CRDS Cache Location ###

The Jenkins instance is running on a virtual machine inside STScI, so it works best with
its CRDS cache set to "/grp/crds/cache", but especially when working over the VPN this
location may not work best for you. In order to use a local CRDS cache, set the 
`CRDS_CACHE_TYPE` environment variable to "local" (e.g. `export CRDS_CACHE_TYPE=.local`).
This will tell CRDS to cache files in the directory `${HOME}/crds/cache`

### New Test Data ###

If you have a notebook that uses updated test data or new test data, follow the steps
below to request a data update.

#### Artifactory Workflow ####

Artifactory should be used for data that is for internal use only.

1. Create a [Jira "Task" Issue in the JWST Simulations Jira project][jira_task] requesting
   to have your data added to Artifactory. Assign the ticket to Misty Cracraft
   ([@cracraft](https://github.com/cracraft)) or Alicia Canipe
   ([@aliciacanipe](https://github.com/aliciacanipe)), and provide more information about
   the data: simulation information, data location, and pipeline step(s). Once your data
   has been added to Artifactory, Misty Cracraft ([@cracraft](https://github.com/cracraft))
   or Alicia Canipe ([@aliciacanipe](https://github.com/aliciacanipe)) will resolve the
   issue and notify you that your data is ready to be used (the full path to the data will
   be provided by the person who notified you that your data was ingested successfully).
2. Make sure you have the proper OS environmental variable set to access STScI's instance
   of Artifactory. This can be done via command line or put into a setup file like a
   ```.bash_profile``` file. If you are working in the `jwst_validation_notebooks`
   environment, your environment will be set up automatically.

   ```
   export TEST_BIGDATA=https://bytesalad.stsci.edu/artifactory/
   ```

3. Make sure your environment has ```ci_watson``` installed. This is done automatically by
   the `jwst_validation_notebooks` environment.

   ```
   pip install ci_watson
   ```

4. In your notebook, import the ```ci_watson``` package needed.

   ```
   from ci_watson.artifactory_helpers import get_bigdata
   ```

5. Read in each file stored in Artifactory (the full path should have been provided by the
   person who ingested the data).

   ```
   satfile = get_bigdata('jwst_validation_notebooks',
                         'validation_data',
                         'jump',
                         'jump_miri_test',
                         'miri_sat_55k.fits')
   ```

6. Follow the normal workflow for contributing a notebook once you have confirmed that
   your notebook is running successfully.

#### Box Folder Workflow ####

Artifactory is only accessible to internal users on the STScI network. If you would like
to contribute a test notebook that uses externally available data, this test data should
be stored in our Box folder (`jwst_validation_notebooks`) instead.

1. Create a [Jira "Task" Issue in the JWST Simulations Jira project][jira_task] requesting
   to have your data added to the Box folder. Assign the ticket to Misty Cracraft
   ([@cracraft](https://github.com/cracraft)) or Alicia Canipe
   ([@aliciacanipe](https://github.com/aliciacanipe)), and provide more information about
   the data: simulation information, data location, and pipeline step(s). Once your data
   has been added to Box, Misty Cracraft ([@cracraft](https://github.com/cracraft))
   or Alicia Canipe ([@aliciacanipe](https://github.com/aliciacanipe)) will resolve the
   issue and notify you that your data is ready to be used (the Box link to the data will
   be provided by the person who notified you that your data was ingested successfully).
2. Then, in your validation notebook, you will use the following command to import your
   file from Box (we are using an example file link, you will substitute yours):

```
from astropy.utils.data import download_file

your_file_box_url ="https://stsci.box.com/shared/static/tpks98b3voqg7r13jt8i6el3yfg9dqoc.fits"
file = download_file(your_file_box_url)
```

Box assigns a default alphanumerical string as the filename, so you may want to update the
filename before processing, or verify that the format is correct. Depending on the data,
you can try:

```
# open file into correct format and write to local disk for processing
with fits.open(file) as hdu:
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
Users and contributors to the `jwst_validation_notebooks` repository should adhere to the
[Code of Conduct](https://github.com/spacetelescope/mirage/blob/master/CODE_OF_CONDUCT.md).
Any issues or violations pertaining to the Code of Conduct should be brought to the
attention of a `jwst_validation_notebooks` team member or to `conduct@stsci.edu`.


## Questions

For any questions about the `jwst_validation_notebooks` project or its software or
documentation, please
[open an Issue](https://github.com/spacetelescope/jwst_validation_notebooks/issues).


## Current Core Development Team
- Alicia Canipe [@aliciacanipe](https://github.com/aliciacanipe)
- Misty Cracraft [@cracraft](https://github.com/cracraft)
- Maria Pena-Guerrero [@penaguerrero](https://github.com/penaguerrero)
- Brian York [@york_stsci](https://github.com/york_stsci)


[conda]: https://docs.anaconda.com/anaconda/ "Anaconda Individual Edition Documentation"
[github_branch]: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/creating-and-deleting-branches-within-your-repository#creating-a-branch "Creating a github branch"
[github_fork]: https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo "Creating a fork"
[github_upstream]: https://docs.github.com/en/free-pro-team@latest/github/collaborating-with-issues-and-pull-requests/configuring-a-remote-for-a-fork "Github configuring remote for a fork"
[jira_task]: https://jira.stsci.edu/issues/?jql=project%20%3D%20JWSTSIMS%20AND%20resolution%20%3D%20Unresolved%20ORDER%20BY%20priority%20DESC%2C%20updated%20DESC
[jupyter]: https://jupyter.org "The Jupyter Project"
