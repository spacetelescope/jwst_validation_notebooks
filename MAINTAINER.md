# JWST Validation Notebooks

This document serves as a reference for "how do I contribute" to the `jwst_validation_notebooks`. This process will change in the future but as for now, these are the steps that a contributor should follow.

## What are the JWST Validation Notebooks?

The JWST Validation Notebooks are a suite of Jupyter Notebooks written by JWST Instrument Team members that diagnose the "scientific validity" of how the pipeline is performing by using output such as tables and figures. These cannot be diagnosed by a pass or fail criteria like the tests including the testing suite of the JWST pipeline software (unit and regression tests) but by human inspection. The goal of this project is to provide the unexecuted notebooks in a version-controlled repository and generate `html` "screen shots" of the executed notebooks and serve them to the INS team member via a website in a cadence defined by the DMS working group. These notebooks contain code, markdown and figures to conveniently wrap testing into a one stop shop where all of these things can be shared for new pipeline builds. We would like to have a repeatable, reliable, and automated process to provide the teams with testing information to quickly turn around pipeline build testing requirements without having to generate and rerun the same tests and write ups manually.

## Maintainer Checklist

When a user contributes a notebooks to the repository, what should you look for? Since there is standard reviewing process, these are just suggestions for what I would look for.

    1. Did the user follow the suggested notebook outline in the template?
    2. Did the contribute a notebook that has unexecuted cells?
    3. Have the requested access or do they have access to data on artifactory
    4. Do they need you to contribute data for them?
    5. When data is contributed to artifactory, did they test the notebook to use verify it's working?

If the user requests that you add the data for them, you can follow the outline for contributing data in the `CONTRIBUTOR.md` file if you are unfamiliar with the process.