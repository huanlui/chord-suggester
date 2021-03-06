# Chord Suggester

**Initial note**: This `readme` explains how to run this project. For a detailed memory about the scope of this project, please visit [this article at `Medium`](https://medium.com/@huanlui/chordsuggester-i-3a1261d4ea9e).

_ChordSuggester_ is a computer-aided musical composition system. It is not intended to be a professional tool but just the result of a Master’s thesis covering the whole process for a DataScience project:
  
* **Data Acquisition** by scraping data from `ultimate-guitar.com` using `Selenium` and `BeautifulSoup`. This part is interesting by itself since there are no examples of clean datasets including chord songs.
* **Data cleaning** and preparation, using `Pandas` and `music21`.
* **Data analysis**, using `Pandas`.
* **Modelling**, using `Keras` for training an LSTM neural network. 
* **Visualisation** of the results on a `React` Application that consumes the model using `TensorFlow.js` and shows the results using the music libraries `Tone.js` and `Vexflow`. This code is in a [separate repo](https://github.com/huanlui/chord-suggester-frontend).

## Notebooks

There are five notebooks that cover all the needs of the project. Before running them, please, read carefully the whole readme. The notebooks are, in order:

1. [Scraping - Extracting filter criteria](https://github.com/huanlui/chord-suggester/blob/master/src/01%20-%20Scraping%20-%20Extracting%20filter%20criteria.ipynb). Extracts the filter criteria (genre, style and decade) to be used by the next notebook. 
2. [Scraping - Extracting songs.](https://github.com/huanlui/chord-suggester/blob/master/src/02%20-%20Scraping%20-%20Extracting%20songs.ipynb). Extracts the songs (name, decade, url, genre, chords...)
3. [Feature extraction](https://github.com/huanlui/chord-suggester/blob/master/src/03%20-%20Feature%20extraction.ipynb). Feature engineering over the dataset extracted by the previous notebook. 
4. [Model](https://github.com/huanlui/chord-suggester/blob/master/src/04%20-%20Model.ipynb). Trains an LSTM to predict the most probable chords after a given chord sequence. 
5. [Exporting model to Javascript](https://github.com/huanlui/chord-suggester/blob/master/src/05%20-%20Exporting%20model%20to%20Javascript.ipynb). Some utilities to export dictionaries from Python to Javascript. 

The rest of the notebooks (name starting with `DRAFT_`) have been used to inspect data, explore different approaches, etc. They do not have to be run, but they could be interesting to see the development process. 

## Installing libraries

The easiest way to execute this project is by installing the last version of [`Anaconda`](https://www.anaconda.com/distribution/). Most libraries used by this project are included by this distribution. 

Once installed, there are three options to install the rest of required libraries:

- Install only libraries not included in `Conda` (automatic way) by executing:

```bash
pip install -r src/requirements.txt
```

- Install only libraries not included in `Conda` by executing:

```bash
pip install "pytest==5.3.2"
pip install "selenium==3.141.0"
pip install "music21==5.7.0"
pip install "beautifulsoup4==4.8.2"
```

- Create a `Conda` environment by using:

```bash
conda create --name <env> --file src/requirements-conda.txt
```

## Installing Selenium

Scraping notebooks (see [01 - Scraping - Extracting filter criteria.ipynb](https://github.com/huanlui/chord-suggester/blob/master/src/01%20-%20Scraping%20-%20Extracting%20filter%20criteria.ipynb) and [02 - Scraping - Extracting songs.ipynb](https://github.com/huanlui/chord-suggester/blob/master/src/02%20-%20Scraping%20-%20Extracting%20songs.ipynb)) need `Chrome Driver` to be installed from [here](https://sites.google.com/a/chromium.org/chromedriver/home) and copied (unzipped) to the same folder as the notebook (`src` folder). In the repo, my version is copied, but it could not work on your computer. The driver must be compatible with the installed `Chrome` version.

In `MacOS`, you must additionally allow MacOS to run non-known apps: open `System Preferences` and click `Security & Privacy`. Change `Allow apps downloaded from` to `Anywhere`.

## Showing sheets on notebooks

In order to make `show()` function work when using `music21` on Notebooks, any music engraving software (such as `Finale`, `Sibelius` or `MuseScore`) has to be installed. 

I recommend [MuseScore](https://musescore.org) because it is for free, open source, easy to install and lightweight. 

## Converting model created from Python Keras to TensorFlow.js format in a Conda Environment

`TensorFlow.js` is required but please, stop and don't write ``~pip install tensorflowjs~`` because it could break your Anaconda installation (it was my case...).

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

Note that the input path used above is a sub-folder generated automatically by `Keras` when it
saved a tf.keras model in the ModelCheckpoint layer.

The output folder will contain a .json file ready to be copied to frontend `public` folder. 

In order to easily convert all the generated models and copy them to frontend directory, two scripts are provided. They can be found in `model` folder, where all the generated models are saved:

* `convert-all-models.sh`: converts all the models (files with .h5 extensions) to `TensorFlow.js` models (a folder starting with `tfjs_model`). To execute them, type this code from a terminal:

```bash
sh convert-all-models.sh
```

* `copy-models-to-frontend.sh`: copies all the `TensorFlow.js` models (folders) into `public/models` folder of frontend project. This requires frontend repository to be under the same folder as this repository.  To execute from a terminal type:

```bash
sh copy-models-to-frontend.sh
```

## .py files

To avoid errors and improve codebase quality, some functions have been extracted from notebooks and included in `.py` files. All these files have this pattern as name: `jl_xxx.py`. This allows:

* Reuse function in different notebooks. 
* Test this functions. This is important in a DataScience project, where much time is wasted discovering errors or, even worse, where hidden errors are creating misbehaviours in production. 

## jl_pychord

`Pychord` is a nice library to manage musical chords in Python. It does not have all the necessary functionality, so its repo has been cloned an modified here. This is technical debt: the right action would have been to fork the repo, add the necessary documentation and even create a PR for asking the author to merge it. 

## Testing

In `requirements.txt` file, `pytest` is included. It is a unit test library.

Most `.py` files are covered by tests. 

To run the tests, once `pytest` is installed, write the following from src folder in terminal:

```bash
pytest
```

## Models

In `model` folder, several models have been exported in both h5 and TensorFlow.js formats. Some of them can be tests that do not work at all. 

The most accurate models (the ones used in front-end demo) are `tfjs_model_lstm_normalised__W_20_lr_0_0005_epochs=50_batch_128.h5` and `tfjs_model_lstm_normalised__W_20_lr_0_001_epochs=50_batch_128.h5`. 
