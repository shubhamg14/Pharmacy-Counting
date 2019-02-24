from collections import defaultdict

# Generate key-value pair for each line in the input file (Key: first_name, last_name, drug_name | value: drug_cost)
def generate_prescriber_drug_key_to_drug_value(csv_reader):
    data_dict = defaultdict(list)
    for row_item in  csv_reader:
        # split the line into key value pairs
        first_name, last_name, drug_name, drug_cost = row_item[1], row_item[2], row_item[3], row_item[4]

        key = first_name+','+last_name+','+drug_name
        value = drug_cost

        # Storing the key value pairs in dictionary        
        data_dict[key].append(value)
    return data_dict

# Aggregating drug cost per unique prescriber
def aggregating_drug_cost_per_person(data_dict):
    return {k:sum(map(float, v)) for k, v in data_dict.items()}

# Aggregating unique drug cost through all prescibers 
def aggregating_same_drug_cost_for_all_prescriber(data_dict):
    drugs_dict = defaultdict(list)
    for k, v in data_dict.items():
        drug_name = k.rsplit(',')[2]
        drugs_dict[drug_name].append(v)

    return drugs_dict


