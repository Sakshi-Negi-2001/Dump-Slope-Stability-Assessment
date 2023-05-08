# Artificial Intelligence based Tool for the Stability Assessment of Overburden Dump Slope 

## Problem Statement
Existing softwares to analyse slope stability are expensive with very high computation cost and high computation time.
Open source softwares that exist have a very limited use case. 
Most of the geotechnical engineers do not have necessary technical skills to use the open source tools.
There is an overall lack of existing dataset to use in machine learning or deep learning models for slope stability analysis in mines.


## Objective
Scraping data from various research articles related to overburden slope stability to extract relevant parameters for generating dataset (To be used in the ML/DL models).
To develop machine learning models for predicting the Factor of Safety (FOS) using generated dataset.
Hyper-tuning and validation of the results received from the machine learning models with processed data from industry-leading numerical simulation software.
To develop a graphical user interface tool.


## Methodology
![image](https://user-images.githubusercontent.com/77374152/236751451-c3699e3d-a3aa-4c77-a403-0e3a01ac4b76.png)

Generate a dataset using reputed journal paper’s pseudo-static conditioned analyses of overburden slope stability.
Refinement and cross validation of the dataset.
Apply pre-processing techniques on the dataset and division of the dataset into training and testing data.
Development of ML models on the dataset and assessment of various metrics .
Compare the result of each model with the validation set received by industry leading numerical simulation software.


## Result Comparision
![image](https://user-images.githubusercontent.com/77374152/236752441-a34f6c41-7d57-4ef4-bd98-8b56a8ce26e7.png)


## Image of Assesment Tool 
![image](https://user-images.githubusercontent.com/77374152/236752127-687b4720-174d-41a4-bdd8-e148f95ecee8.png)

## Refrences
[1] Lin S, Zheng H, Han C, Han B, Li W. Evaluation and prediction of slope stability using machine learning approaches. Front Struct Civ Eng 2021;15:821–33. https://doi.org/10.1007/S11709-021-0742-8/METRICS
[2] Karir D, Ray A, Kumar Bharati A, Chaturvedi U, Rai R, Khandelwal M. Stability prediction of a natural and man-made slope using various machine learning algorithms. Transp Geotech 2022;34:100745. https://doi.org/10.1016/j.trgeo.2022.100745
