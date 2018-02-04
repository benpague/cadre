Claims Audit Decision-Support and Recommendation System (CADRE)
===============================================================

A  suite of tools for decision-support in the claims and provider audit cycle.
Utilizes unsupervised machine learning techniques applied to identified metrics
to build suspicion on potential fraudulent providers. 

Installation
===============================================================

Download the data
- Clone this repo to your computer
- Get into the folder using `cd cadre` .
- Run `mkdir data`.
- switch to the `data` directory using cd `data`.
- Download claims data files(csv)
    -It's recommended to use 2012 to current regional claims data set
     with the following features:
     - series number(SERIES)
     - hospital name (INST_NAME)
     - first case rate claimed(PRIMARY_CASE)
     - second case rate claimed(SECONDARY_CASE)
     - patient sex(PAT_SEX)
     - patient age(PAT_AGE)
     - date admitted(DATE_ADM)
     - date discharged (DATE_DIS)
     - name of attending physician
     - membership category (WORKER_TYP)
     
 Install the requirements
 
 - Install the requirements
    - make sure to use Python 3
    - you may want to use a virtual environment on this

Usage
