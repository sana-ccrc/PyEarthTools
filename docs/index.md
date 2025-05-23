% scores documentation master file, created by
% sphinx-quickstart on Sat Sep  9 11:24:53 2023.
% You can adapt this file completely to your liking, but it should at least
% contain the root `toctree` directive.

# PyEarthTools: Reproducible machine learning for Earth system science

- An approachable way for a researchers to get going with ML research for Earth system science
- Suitable for students and newcomers, as well as providing a software framework for professional research
- Still under early-stage development - things are likely to change a lot. If you notice an issue, please free to raise it on Github

<figure style="display:inline-block; width:45%; margin-right:5%;">
    <img src="https://pyearthtools.readthedocs.io/en/latest/_images/notebooks_demo_FourCastNeXt_Inference_9_1.png" alt="A prediction of the weather" width="100%">
    <figcaption>A weather prediction from a trained model.</figcaption>
</figure>

<figure style="display:inline-block; width:45%; vertical-align:top;">
    <img src="https://pyearthtools.readthedocs.io/en/latest/_images/notebooks_tutorial_Working_with_Climate_Data_14_2.svg" alt="A data processing pipeline" width="300">
    <figcaption>A data processing flow composed for working with climate data.</figcaption>
</figure>

Source Code: [github.com/ACCESS-Community-Hub/PyEarthTools](https://github.com/ACCESS-Community-Hub/PyEarthTools)  
Documentation: [pyearthtools.readthedocs.io](https://pyearthtools.readthedocs.io)  
Tutorial Gallery: [available here](https://pyearthtools.readthedocs.io/en/latest/notebooks/Gallery.html)  

PyEarthTools is composed from multiple sub-packages which users may want separately. However, people also want a very quick installation options. Here is the quickest way to install "everything" and get moving:

```
git clone git@github.com:ACCESS-Community-Hub/PyEarthTools.git
pip install -r requirements-dev.txt
conda install graphviz
cd notebooks
jupyter lab
```

PyEarthTools is a Python framework containing modules for:
 - loading and fetching data; 
 - pre-processing, normalising and standardising data into a normal form suitable for machine learning; 
 - defining machine learning (ML) models; 
 - training ML models and managing experiments;
 - performing inference with ML models; 
 - and evaluating ML models. 

PyEarthTools comprises multiple sub-packages which can be used individually or together.

|    Sub-Package                 |  Purpose  |
|--------------------------------|---------------------- |
|  [Data](data/data_index.md)    | Loading and indexing into well-known Earth system data sets to produce ML-ready data structures |
|  [Utils](utils/utils_index.md)  | Code for common functionality across the sub-packages |
|  Pipeline       | Definining reproducible sequences of operations with the ability to cache results |
|  Training       | Code defining the training processes and schedules of a machine learning model |
|  Tutorial       | Contains helper code for data data sets used in tutorials |
|  Bundled Models | Maintained versions of specific, bundled models which can be easily trained and run |
|  Zoo            | Contains code for managing registered models (such as the bundled models) |
|  Evaluation     | (Coming soon) Contains code for producing standard evaluations (such as benchmarks and scorecards) |

# Overview of documentation

We have information for:

 - [New user guides and introduction to the concepts in PyEarthTools](https://pyearthtools.readthedocs.io/en/latest/newuser.html)
 - [Installation instructions](https://pyearthtools.readthedocs.io/en/latest/installation.html) for different usage scenarios
 - [Data catalogue setup](https://pyearthtools.readthedocs.io/en/latest/catalogue.html) for facility managers or individuals to establish their research data catalogue
 - [A tutorial gallery with a wide variety of examples](https://pyearthtools.readthedocs.io/en/latest/notebooks/Gallery.html)
 - Much more, including how-to guides, project setup guide, information on accessing data, guides to evaluation, orientiation for
   physical scientists and data scientists


```{toctree}
:caption: 'Index to Documentation:'
:maxdepth: 2

self
newuser
newproject
projectideas
installation
notebooks/Gallery
catalogue
config
api
roadmap
devguide
maintainer
```
