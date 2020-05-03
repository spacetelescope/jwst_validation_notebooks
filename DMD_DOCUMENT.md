# JWST Validation Notebooks

This document serves as a reference for the "technical infrastructure" for the `jwst_validation_notebooks`. Here I will explain the purpose of the repository, breakout the components of the project, and outline the execution of the steps.

## What are the JWST Validation Notebooks?

The JWST Validation Notebooks are a suite of Jupyter Notebooks written by JWST Instrument Team members that diagnose the "scientific validity" of how the pipeline is performing by using output such as tables and figures. These cannot be diagnosed by a pass or fail criteria like the tests including the testing suite of the JWST pipeline software (unit and regression tests) but by human inspection. The goal of this project is to provide the unexecuted notebooks in a version-controlled repository and generate `html` "screen shots" of the executed notebooks and serve them to the INS team member via a website in a cadence defined by the DMS working group. These notebooks contain code, markdown and figures to conveniently wrap testing into a one stop shop where all of these things can be shared for new pipeline builds. We would like to have a repeatable, reliable, and automated process to provide the teams with testing information to quickly turn around pipeline build testing requirements without having to generate and rerun the same tests and write ups manually.

## Components of the JWST Validation Notebooks

There are three main components of this project and I will explain how they all tie together into a single effort:

    1. Notebooks
    2. Jenkins CI Pipeline
    3. Website

### 1. Notebooks ###

The pristine(unexecuted) notebooks live in the master branch of the repository. The reason we version control the unexecuted notebooks and not the executed versions is because they are easier to track actual changes and the executed versions of the notebooks require a lot of disk space that should be used to store more notebook content. 

The notebooks are executed cell by cell using the [`nbpages` package](https://github.com/eteq/nbpages) located here. This package also generates the `html` "screenshots" of the executed notebooks.

The executed notebooks and `html` output is captured in the `gh-pages` branch of the repository. The reasoning for naming the branch `gh-pages` comes from the [STScI Notebooks](https://github.com/spacetelescope/notebooks) effort. The `notebooks` repository provides a very similar service to that of the `jwst_validation_notebooks` so why not synergize our efforts and consolidate into one place. Here are the main reasons why:

    1. The notebooks rely on data and information being publically accessable, which the JWST data and pipeline are not at the moment.
    2. The notebooks currently rely on CIRCLECI and Travis to perform their regression builds. These systems can not peform the task to get data behind the STScI firewall.
    3. The `html` output is served through the github pages (github.io) page that is associated with the repository. These pages are publically accessable regardless of the permissions set on the repository itself.

The main take away is, since there is ITAR sensitive material associated with the notebooks, we need to protect and keep all of the input and output of the notebooks internal facing. The `notebooks` repository is where the majority of the notebooks that will be contributed to this project should be maintained when possible (pipeline and data are public). These notebooks serve as good benchmarks of how the pipeline is performing and future JWST users might be curious about the this as well as the notebooks that are teaching them how to use `drizzlepac` or how to produce a light curve from Kepler data.

### 2. Jenkins CI Pipeline ###

We automate and test the JWST Validation Notebooks using Jenkins CI. The main reason we use Jenkins is because it interfaces well with how we store the data for the notebooks using artifactory, see our artifactory repo [here](https://bytesalad.stsci.edu/artifactory/webapp/#/artifacts/browse/tree/General/jwst_validation_notebooks). The pipeline is broken down into 3 steps:

    1. Environment
    2. Convert/Check
    3. Deploy

The first step sets up and builds environment and all of the dependencies required to execute the notebooks. The second step converts the notebooks to html, it then makes sure that the notebooks cells are unexecuted after they were run and converted to html to make sure we aren't pushing changes to the pristine notebooks. At this step, the `index.html` file and `report.xml` file are created. `index.html` outlines and provides link to the executed notebooks in an organized fashion. Lastly, the deploy step clones and checkout the `gh-pages` repo for the changes to be added and then pushed back up to the repo. This stage also collects and rsync’s the html pages to generate the webpage to their proper location before tear down.

To see the build status of the project [here](https://plwishmaster.stsci.edu:8081/job/Notebooks/job/jwst_validation_notebooks_spacetelescope/).

### 3. Website ###

Finally, the website is the final portion of the project and the main product delivered to the users. This is the place where team members can come to check the output of their notebooks. Visit the website here https://jwst-validation-notebooks.stsci.edu/