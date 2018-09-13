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
- Run `mkdir processed`.
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
    - download and install anaconda 64bit https://www.anaconda.com/download/#windows
    - use anaconda prompt.
    - create virtual environment
        - get into the folder by `cd cadre`.
        - initialize the folder by running `virtualenv .`
        - activate virtual environment by `cd Scripts` then run `activate`.
        - get back to the cadre folder by `cd ..`
        - install other requirements
        - run `pip install os`
        - run `pip install pandas`
        - run `pip install sqlite3`
        - run `pip install scikit-learn`
        - run `pip install matplotlib`
        - run `pip install dateutil`
        - run `pip install datetime`
        - run `pip install dash==0.26.3`
        - run `pip install dash-html-components==0.12.0`
        - run `pip install dash-core-components==0.28.0`
        
     
   

Usage

- csv or xls files should already be in the data folder.
- use anaconda prompt.
- make sure you are in the `cadre` folder.
- process input data files by running `python assemble.py`.
- run `python annotate.py`
- run `python outlier_detection.py`
- make sure you are connected to the internet and run `python visualize_cases.py`

Analysis