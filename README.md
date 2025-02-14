# PhotoSenseAI

[![Python](https://img.shields.io/pypi/pyversions/PhotoSenseAI)](https://img.shields.io/pypi/pyversions/PhotoSenseAI)
[![Pypi](https://img.shields.io/pypi/v/PhotoSenseAI)](https://pypi.org/project/PhotoSenseAI/)
[![Docs](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/PhotoSenseAI/)
[![LOC](https://sloc.xyz/github/erdogant/PhotoSenseAI/?category=code)](https://github.com/erdogant/PhotoSenseAI/)
[![Downloads](https://static.pepy.tech/personalized-badge/PhotoSenseAI?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month)](https://pepy.tech/project/PhotoSenseAI)
[![Downloads](https://static.pepy.tech/personalized-badge/PhotoSenseAI?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)](https://pepy.tech/project/PhotoSenseAI)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/PhotoSenseAI/blob/master/LICENSE)
[![Forks](https://img.shields.io/github/forks/erdogant/PhotoSenseAI.svg)](https://github.com/erdogant/PhotoSenseAI/network)
[![Issues](https://img.shields.io/github/issues/erdogant/PhotoSenseAI.svg)](https://github.com/erdogant/PhotoSenseAI/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![DOI](https://zenodo.org/badge/228166657.svg)](https://zenodo.org/badge/latestdoi/228166657)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://towardsdatascience.com/what-are-PhotoSenseAI-loadings-and-biplots-9a7897f2e559)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg?logo=github%20sponsors)](https://erdogant.github.io/PhotoSenseAI/pages/html/Documentation.html#colab-notebook)
![GitHub Repo stars](https://img.shields.io/github/stars/erdogant/PhotoSenseAI)
![GitHub repo size](https://img.shields.io/github/repo-size/erdogant/PhotoSenseAI)
[![Donate](https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors)](https://erdogant.github.io/PhotoSenseAI/pages/html/Documentation.html#)
<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->





<!---[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)-->
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

* ``PhotoSenseAI`` is Python package

# 
**Star this repo if you like it! ⭐️**
#


## Blog/Documentation

* [**PhotoSenseAI documentation pages (Sphinx)**](https://erdogant.github.io/PhotoSenseAI/)
* [**Notebook with examples**](https://colab.research.google.com/github/erdogant/PhotoSenseAI/blob/master/notebooks/PhotoSenseAI.ipynb)
* [**Read more details and usage about PhotoSenseAI in this blog!**](https://towardsdatascience.com/PhotoSenseAI)

* <a href="https://erdogant.github.io/PhotoSenseAI/"> <img src="https://img.shields.io/badge/Sphinx-Docs-Green" alt="Open documentation pages"/> </a> PhotoSenseAI documentation pages 
* <a href="https://colab.research.google.com/github/erdogant/PhotoSenseAI/blob/master/notebooks/PhotoSenseAI.ipynb"> <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open example In Colab"/> </a> Notebook example 
* <a href="https://towardsdatascience.com/a-step-by-step-guide-for-clustering-images-4b45f9906128"> <img src="https://img.shields.io/badge/Medium-Blog-blue" alt="Open Blog"/> </a> Blog: A step-by-step guide for clustering images 


### Contents
- [Installation](#-installation)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

### Installation
* Install PhotoSenseAI from PyPI (recommended). PhotoSenseAI is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* A new environment can be created as following:

```bash
conda create -n env_PhotoSenseAI python=3.8
conda activate env_PhotoSenseAI
```

```bash
pip install PhotoSenseAI            # normal install
pip install --upgrade PhotoSenseAI # or update if needed
```

* Alternatively, you can install from the GitHub source:
```bash
# Directly install from github source
pip install -e git://github.com/erdogant/PhotoSenseAI.git@0.1.0#egg=master
pip install git+https://github.com/erdogant/PhotoSenseAI#egg=master
pip install git+https://github.com/erdogant/PhotoSenseAI

# By cloning
git clone https://github.com/erdogant/PhotoSenseAI.git
cd PhotoSenseAI
pip install -U .
```  

#### Import PhotoSenseAI package
```python
import PhotoSenseAI as PhotoSenseAI
```

#### Example:
```python
df = pd.read_csv('https://github.com/erdogant/hnet/blob/master/PhotoSenseAI/data/example_data.csv')
model = PhotoSenseAI.fit(df)
G = PhotoSenseAI.plot(model)
```
<p align="center">
  <img src="https://github.com/erdogant/PhotoSenseAI/blob/master/docs/figs/fig1.png" width="600" />
  
</p>


#### References
* https://github.com/erdogant/PhotoSenseAI

#### Citation
Please cite in your publications if this is useful for your research (see citation).
   
### Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

### Contribute
* All kinds of contributions are welcome!
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)

### Licence
See [LICENSE](LICENSE) for details.
