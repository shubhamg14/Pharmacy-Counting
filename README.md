# Pharmacy-Counting-Coding-Challenge

This program uses python3 to generate a list of all drugs, the total number of unique individuals who prescribed the medication, and the total drug cost, which is listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order.

The code is written in python 3.7 and uses only csvReader library to read input and write output to a file. All other functionality is implemented using input data structures in python i.e Lists and Dictionaries.

Note: As per instructions, for this challenge, prescriber's id is not taken into consideration to mark an individual as unique prescriber, rather if two lines have same first name and last name then it is considered as same prescriber even if prescriber id is different. 

### Input Dataset (itcont.txt)

    Dataset provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name. It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication.

        id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
        1952310666,A'BODJEDI,ENENGE,ALPRAZOLAM,1964.49
        1952310666,A'BODJEDI,ENENGE,AMANTADINE,1129.94
        1952310666,A'BODJEDI,ENENGE,AMBIEN,4792.29
        1952310666,A'BODJEDI,ENENGE,AMBIEN CR,4792.29
        1952310666,A'BODJEDI,ENENGE,AMITRIPTYLINE HCL,692.78

### Output Dataset (top_cost_drug.txt)

    Each line of this file contains these fields:

    drug_name: the exact drug name as shown in the input dataset
    num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
    total_cost: total cost of the drug across all prescribers

        drug_name,num_prescriber,total_cost
        HARVONI,2,1.53061e+06
        SPIRIVA,25,793432
        LANTUS SOLOSTAR,19,685977
        LANTUS,17,637497
        ADVAIR DISKUS,26,580005

### Implementation

#### Directory Structure

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy_counting.py
    |   └── csv_reader.py
    |   └── data_manager.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt

##### Files Explanation

- README.md - This file gives a brief on what this code does, the directory structure of code, input/output files, instructions on how to run code.

- run.sh - This file can directly execute the code which is residing under src directory using python3

- src
    - pharmacy_counting.py - This is the main code file which calls all the other methods residing inside csv_reader.py and data_manager.py. 
    This file calls methods to read input text file, perform transformations and write final output to a file.

    - csv_reader.py - This file contains methods to read input text file as a CSV, method to arrange columns in desired output format and method to write final output to a text file.

    - data_manager.py - This file contains method to aggregate same drug cost through unique prescribers and then a method to aggregate unique drug cost through all prescribers.

    NOTE: All the above code files have been commented to give an insight as to what each function does
- input
    - itcont.txt - The input text file which contains 24 miliion records on which the program is tested.

- output
    - top_cost_drug.txt - The output text file containing the names of all unique drugs, with their unique number of prescribers and the totalselling cost for that drug.

- insight_testsuite - The unit test case which was provided by Insight team to verify the result.

    The output for test result was PASS

    [Sun, Feb 24, 2019  1:18:04 PM] 1 of 1 tests passed