Claims Audit Decision-Support and Recommendation System (CADRE)
===============================================================

A  suite of tools for decision-support in the claims and provider audit cycle.
Utilizes data visualization and unsupervised machine learning techniques applied to identified features
to build suspicion on potential fraudulent providers. 

Installation
===============================================================

Download the data
- Clone this repo to your computer
- Get into the folder using `cd cadre` .
- Run `mkdir data`.
- switch to the `data` directory using `cd data`.
- Download claims data files csv or ms excel('.csv' or '.xls')
    -It's recommended to use 2014 to current regional claims data set
     with the following features:
     - series number(SERIES)
     - hospital name (INST_NAME)
     - first case rate claimed(PRIMARY_CASE)
     - second case rate claimed(SECONDARY_CASE)
     - patient sex(PATSEX)
     - patient age(PATAGE)
     - date admitted(DATE_ADM)
     - hospital level(CLASS_DEF)
     
 Requirements
 - Windows 10 64bit
 - RAM 16GB or higher
 
 - Install 
    - download and install anaconda 
    - create virtual environment
        - get into the folder using `cd cadre`

Usage
