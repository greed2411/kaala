# kaala
For Farmers. For Hard workers. For Thalaivar.😎😎😎.

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/greed2411/ASF/commits/master)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/greed2411)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![GitHub issues](https://img.shields.io/github/issues/greed2411/kaala.svg)](https://github.com/greed2411/ASF/issues)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/greed2411/badges)

![thalaivar](http://www.filmcompanion.in/wp-content/uploads/2018/03/FC_Kaala_teaser_lead_3.jpg)

## What is kaala?
Kaala (pronounced: *kaa-la*, kaala represents black, the color of hard work in Tamil) is a software that helps farmers to predict the best crop to cultivate for growing perennial crops for that particular season and specific soil conditions. We ([@MINOSai](https://github.com/MINOSai), [@bhaveshpraveen](https://github.com/bhaveshpraveen)) and myself made this web application for helping farmers. This is the Data Science Part. Also we won the ***second place in VIT SCOPE's Software Engineering Hackathon***.



## What are the features?


1. Rainfall
2. Temperature
3. Vegetation
4. Potential evapotranspiration
5. Length of growing period as a function of rainfall.
6. Soil storage
7. Soil scape
8. Soil type 
9. Current season 
10. Companion crops 
11. Time for plant to grow

Source: [How to determine the kinds of crops suitable to different types of soil? - ResearchGate](https://www.researchgate.net/post/How_to_determine_the_kinds_of_crops_suitable_to_different_types_of_soil)

## Classes/Labels/Crops

CEREALS

1. 	Rice 	
2. 	Jowar (Cholam) 	
3. 	Bajra (Cumbu) 	
4. 	Ragi 	

PULSES

5. 	Bengalgram 	
6. 	Redgram 	

Source: [Season and Crop Report of Tamil Nadu](http://www.tn.gov.in/crop/AreaProduction.htm)

which gives us 6 classes.

## More about the Data

I have used [scikit-learn](http://scikit-learn.org/stable/)'s [make_classification](http://scikit-learn.org/stable/modules/generated/sklearn.datasets.make_classification.html) for creating 6,04,800 observations for 11 above mentioned features and 6 classes, unsupervised learning -> k means clustering couldn't help us achieve a good accuracy, so I had to use [kNN](http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html) with k=30 to get the most probable values using `predict_proba` for the particular model. Also 11 features were there, I had to use [PCA](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html) to reduce the dimensions to 5 to get even better accuracy of `88.54%`. Final results and dumping them into pkl file using `Pipeline` and `joblib` is shown in [kaala-mark2.ipynb](https://github.com/greed2411/kaala/blob/master/kaala-mark2.ipynb). Note this is a normally distributed synthesized data. Not actual data from any particular source.

## Usage

`kaala.py` has the steps to execute the 11 values obtained from the farmer/technician to get the result, which is a list of probable values for that particular crop being fit for that type of soil.
Below is a demonstrated example.

```python
λ python
Python 3.6.0 |Anaconda custom (64-bit)| (default, Dec 23 2016, 12:22:00) 
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from kaala import result
>>> result([0.7355922448977834,
...  0.5241942948529987,
...  1.2148519094713788,
...  0.13122963308657765,
...  -0.15842665047198703,
...  0.25808805092069,
...  -1.6808344120353165,
...  0.09900267090424587,
...  -1.2541620126778479,
...  1.1452959921425545,
...  -0.4384289245048979])
[0.0, 0.9666666666666667, 0.03333333333333333, 0.0, 0.0, 0.0]
>>> 
