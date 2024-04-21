# Stellar Classification - SDSS17

## Authors
[Igor Kołodziej](https://github.com/IgorKolodziej)

[Kamil Eliaszuk](https://github.com/kamil5555579)

## Introduction
This project focuses on the classification of stars, galaxies, and quasars using spectral characteristics. The dataset used for this project is derived from the Sloan Digital Sky Survey (SDSS) DR17. The goal is to create a robust model that accurately identifies celestial objects to optimize the allocation of resources for further research.

## Business Case
Suppose a team of astrophysicists has tasked us with developing a model to classify celestial objects reliably. 
Given the high cost associated with further research on classified objects, maximizing the **precision** of the classification model is paramount. 
The team requires assurance that objects are identified correctly to streamline subsequent investigations.

## Folder Structure
- **dataset:** Contains the dataset used for training and evaluation.
- **models:** Stores trained machine learning models.
- **notebooks:** Jupyter notebooks documenting data exploration, model training, and evaluation.
- **scripts:** Python scripts for automated data exploration.
- **envs:** Anaconda environments used in this project.

## Virtual environments
Anaconda environments used in this project are available in the `envs` directory.
- Use `env_automated_eda` to run the scripts
- Use `env` for anything else

## Best Model
After extensive testing of various architectures, the random 
forest model achieved the highest performance, with weighted precision of 0.977 using only 4 features of the dataset.

## Dataset Overview
The dataset comprises 100,000 observations from the SDSS, each described by 17 feature columns and 1 class column. The features include spectral characteristics such as ultraviolet, green, red, and infrared filters, along with identifiers such as object ID, right ascension angle, declination angle, and more.

- **obj_ID:** Object Identifier
- **alpha:** Right Ascension angle (at J2000 epoch)
- **delta:** Declination angle (at J2000 epoch)
- **u:** Ultraviolet filter
- **g:** Green filter
- **r:** Red filter
- **i:** Near Infrared filter
- **z:** Infrared filter
- **run_ID:** Run Number
- **rereun_ID:** Rerun Number
- **cam_col:** Camera column
- **field_ID:** Field number
- **spec_obj_ID:** Unique ID for optical spectroscopic objects
- **class:** Object class (galaxy, star, or quasar)
- **redshift:** Redshift value
- **plate:** Plate ID
- **MJD:** Modified Julian Date
- **fiber_ID:** Fiber ID

## Dataset Citation
- **Author:** fedesoriano
- **Date:** January 2022
- **Dataset:** Stellar Classification Dataset - SDSS17
- **Link:** [Kaggle](https://www.kaggle.com/fedesoriano/stellar-classification-dataset-sdss17)
