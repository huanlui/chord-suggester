# Chord Suggester

This repo contains the code for my KSchool Data Science Master's thesis. 

This readme will be improved. [This document](doc/initial-presentation.pdf) contains an brief intruduction. 

## Installing libraries

The easiest way to execute this proyect is by installing the last version of [Anaconda](https://www.anaconda.com/distribution/), a distribution that contains the most of the libraries used in this project. 

Once installed, there are three options:

- Install only libraries not included in conda (automatic way) by executing:

```bash
pip install -r src/requirements.txt
```

- Install only libreries not included in conda by executing:

```bash
pip install "pytest==5.3.2"
pip install "selenium==3.141.0"
pip install "music21==5.7.0"
pip install "beautifulsoup4==4.8.2"
```

- Create a conda environment by using:

```bash
conda create --name <env> --file src/requirements-conda.txt
```

## Installing Selenium

Scraping notebooks need `Chrome Driver` to be installed from [here](https://sites.google.com/a/chromium.org/chromedriver/home) and copied (unzipped) to the same folder as the notebook (`src` folder). In the repo, my version is copied, but it could not work on your computer. The driver must be compatible with the installed chrome version.

In `MacOS`, you must additionally allow mac-os to run non-known apps: open `System Preferences` and click `Security & Privacy`. Change `Allow apps downloaded from` to `Anywhere`.

## Showing sheets on notebooks

In order to make `show()` function work when using `music21` on Notebooks, any music engraving software (such as `Finale`, `Sibelius` or `MuseScore`) needs to be installed. 

I recommend [MuseScore](https://musescore.org) because it is for free, open source, easy to install and light. 

## Converting model created from Python Keras to TensorFlow.js format in a Conda Environment

`TensorFlow.js` is required but please, stop and don't write ``~pip install tensorflowjs~`` becasue it could break your Anaconda installation (it was my case...).

The reason is that it requires Python 3.6.8 to work and recent Anaconda distributions have a higher version. 

__1. Install Python 3.6.8 in a virtual environment:__

To force Python 3.6.8 in your local project, you can install
[`pyenv`](https://github.com/pyenv/pyenv) and proceed as follows in the target
directory:

```bash
pyenv install 3.6.8
pyenv local 3.6.8
```

Now, you can
[create and activate](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
a `venv` virtual environment in your current folder:

```bash
virtualenv --no-site-packages venv
. venv/bin/activate
```

__2. Install the TensorFlow.js pip package:__

```bash
 pip install tensorflowjs
```

__3. Run (from command line) the converter script provided by the pip package:__

In this case, our models have HDF5 format. 

```bash
tensorflowjs_converter \
    --input_format=keras \
    /tmp/my_keras_model.h5 \
    /tmp/my_tfjs_model
```

Note that the input path used above is a subfolder generated automatically by `tensorflow` when it
saved a tf.keras model in the SavedModel format.

The output folder will contain a .json file ready to be copied to frontend `public` folder. 


In order to easily convert all the generated models and copy to frontend directory, two scripts are provided. They can be found in `model` folder, where all the generated models are saved:

* `convert-all-models.sh`: converts all the models (files with .h5 extensions) to `TensorFlow.js` models (a folder starting with `tfjs_model`). To execute, from a  terminal type:

```bash
sh convert-all-models.sh
```

* `copy-models-to-frontend.sh`: copies all the `TensorFlow.js` models (folders) into `public/models` folder of frontend project. This requires that frontend repository is under the same folder as this repository.  To execute, from a  terminal type:

```bash
sh copy-models-to-frontend.sh
```
## .py files

To avoid errors and improve the codebase quality, some funtions have been extracted from the notebooks and included in `.py` files. All these files have this pattern as name: `jl_xxx.py`. This allows:

* Reuse function in different notebooks. 
* Test this functions. This is important in a DataScience project, where much time is wasted discovering errors or, even worse, where hidden errors are creating misbehaviours in production. 

## jl_pychord

Pychord is a library to managed musical chords in Python. It does not have all the necessary functionality, so its repo has been cloned an modified here. This is technical debt: the right action would have been to fork the repo, add the necessary documentation an even create a PR for asking the author to merge it. 

## Testing

In requirements files, `pytest` is included. It is a unit test library.

Most .py files are covered by test. 

To run the test, once `pytest` is installed, from src folder in terminal:

```bash
pytest
```

