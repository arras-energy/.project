import marimo

__generated_with = "0.10.17"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Running GridLAB-D simulations

        The following tutorial will walk you through a simple project to run the IEEE 123-bus model in Arras Energy using GridLAB-D.
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""First, you need to load the module that you will use. By convention, this is normally done in the last cell of the notebook because the order of the cell doesn't matter--the order of cell execution is based on the dependencies between the cells.""")
    return


@app.cell
def _():
    import marimo as mo
    import os
    import json
    import gridlabd.runner as gld
    import pandas as pd
    return gld, json, mo, os, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""First, we check the GridLAB-D version installed on your system.  It should be 4.3.17 or greater. We will save this result to prevent other cells from running if the version is too old.""")
    return


@app.cell
def _(gld):
    version_ok = gld.gridlabd("--version=-ge 4.3.17")==""
    return (version_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Next, after being assured that the version is ok, we download the IEEE 123 model from the GridLAB-D model library.""")
    return


@app.cell
def _(gld, mo, version_ok):
    mo.stop(not version_ok,"version check failed")
    model_ok = gld.gridlabd("model","get","IEEE/123")==""
    return (model_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Once the model GLM file is downloaded, we can run the simulation to generate a JSON file that contains the results.""")
    return


@app.cell
def _(gld, mo, model_ok):
    mo.stop(not model_ok,"model download failed")
    solver_ok = gld.gridlabd("123.glm","-o","123.json")==""
    return (solver_ok,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""After verifying that the results are ok, we can load the JSON data.""")
    return


@app.cell
def _(json, mo, solver_ok):
    mo.stop(not solver_ok,"solver failed")
    with open("123.json","r") as fh:
        data = json.load(fh)
    return data, fh


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""We then check the JSON results to make sure they are ok.""")
    return


@app.cell
def _(data, mo):
    mo.stop(data["application"]!="gridlabd","not a gridlabd model")
    mo.stop(len(data["objects"])==0,"not objects in model")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""The following classes are found in the model:""")
    return


@app.cell(hide_code=True)
def _(data, mo):
    _options = sorted(set([x['class'] for x in data["objects"].values()]))
    class_ui = mo.ui.radio(options=_options,value=_options[0],label="(Choose a class to tabulate)")
    class_ui
    return (class_ui,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""Now we tabulate the data for the selected class in a Pandas dataframe""")
    return


@app.cell
def _(class_ui, data, pd):
    pd.DataFrame(
        {x: y for x, y in data["objects"].items() 
         if y["class"] == class_ui.value}
    ).T
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        For more information on running GridLAB-D in Arras Energy, see https://docs.arras.energy/.

        For more information on using Marimo notebooks, see https://docs.marimo.io/.
        """
    )
    return


if __name__ == "__main__":
    app.run()