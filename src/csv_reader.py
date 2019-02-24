import csv

# Reading input text file as a CSV
def create_csv_reader(file):
    #Reading text file as CSV
    csv_reader = csv.reader(file, quotechar='"', delimiter=',',
                        quoting=csv.QUOTE_ALL, skipinitialspace=True) 
    
    # Skipping the header while reading the file
    next(csv_reader)
    return csv_reader

# Arranging and Generating the output in the desired format
def generating_data_in_output_format(drugs_dict):
    desired_data_array = []
    for key, value in drugs_dict.items():
        finalKey = key
        finalUniqueCount = len([item for item in value if item]) 
        finalPrice = sum([float(item) for sublist in value for item in sublist])
        desired_data_array += [(finalKey,finalUniqueCount,"%g" % finalPrice)] 
    
    return desired_data_array

# Writing final output to a text file
def generate_output_csv_file(final_sorted_data):
    with open('./output/top_cost_drug.txt','w',newline='\n') as outFile:
        csv_out=csv.writer(outFile)
        csv_out.writerow(['drug_name','num_prescriber','total_cost'])
        for row in final_sorted_data:
            csv_out.writerow(row)
    outFile.close()