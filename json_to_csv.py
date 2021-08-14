#!/usr/bin/env python
# coding: utf-8

# -------- start json_to_csv.py -------- <br>
# The export the code below into json_to_csv.py

import json
import pandas as pd
import logging


# JSON to dict
with open('../newnewnew/data/my_file.json') as file:
    iris_dict = json.load(file)

print("Imported JSON file")

# read data as a DataFrame
df = pd.DataFrame(iris_dict['data'], columns=iris_dict['feature_names'])

# add new column called target from the target array
df['target'] = iris_dict['target']

# convert numerical target to target names
num_to_name = {
    0: 'setosa',
    1: 'versicolor',
    2: 'virginica'
}

def map_target_name(numerical_target, num_to_name):
    """map numerical target to target name
    
    Args:
        numerical_target (int): 0,1,2
    
    Returns:
        target_name (str): 'setosa', 'versicolor', 'virginica'
    """
    
    target_name = num_to_name[numerical_target]
    
    return target_name

# create a new column called 'target_names'
df['target_names'] = df['target'].apply(lambda x: map_target_name(x, num_to_name))

print("Converted dict to dataframe")

# drop some column
df = df.drop('target', axis=1)

print("Processed dataframe")

# save to csv
df.to_csv('../newnewnew/data/final_iris_table.csv', index=False)


# the code in json_to_csv.py ends here <br>
# -------- end json_to_csv.py --------
