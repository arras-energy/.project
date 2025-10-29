[![gridlabd](https://github.com/arras-energy/.project/actions/workflows/gridlabd.yml/badge.svg)](https://github.com/arras-energy/.project/actions/workflows/gridlabd.yml)

# Arras Energy project template

Before using the `gridlabd project` subcommand you must login to GitHub at the command, e.g.,

    git auth login

To create a project using this template, run the command

    gridlabd project create PROJECTNAME

where `PROJECTNAME` is the name of your project.

You can edit an existing project with the command

    gridlabd project edit PROJECTNAME

You can save your work using the command

    gridlabd project save PROJECTNAME

To open the project repository on GitHub, use the command

    gridlabd project open PROJECTNAME

For more details see `gridlabd project help`.

# GitHub actions

If the file `gridlabd.sh`, then the script will be in the default shell. Otherwise, if the file `gridlabd.glm` exists, then the model will be run in the latest version of Arras Energy.
