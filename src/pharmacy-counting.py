# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:02:59 2019

@author: shubh
"""
import csv
from csv_reader import *
from data_manager import *

# Opening the data file from default path
file = open('./input/itcont.txt','r')

csv_reader = create_csv_reader(file)

data_dict = generate_prescriber_drug_key_to_drug_value(csv_reader)  

data_dict_1 = aggregating_drug_cost_per_person(data_dict)

drugs_dict = aggregating_same_drug_cost_for_all_prescriber(data_dict)

desired_data_array = generating_data_in_output_format(drugs_dict)

# Sorting the final output firstly on drug cost and if tie then based on name of the drug
final_sorted_data = sorted(desired_data_array, key=lambda x: [float(x[2]), x[0]], reverse=True)

generate_output_csv_file(final_sorted_data)

# Closing the file
file.close()


