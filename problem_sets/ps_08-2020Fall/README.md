# SI 506: Problem Set 08

## This week's problem set

This week's problem set includes 5 problems. You will continue working with dictionaries and build several functions that read/write a comma-separated values (csv) file or a txt file using Python. These functions can be used as your utility functions in future assignments as well as later for your own work.

## Background

You are asked to analyze the total number of COVID-19 cases per US state and the total number of policies US states enacted for prevention. This analysis is based on data collected through late October 2020. The datasets are provided as two files: a csv file `us_policy_updates.csv` and a txt file
`us_covid19_cases.txt`. Build a python script that reads the two files, performs the analysis, and create a csv file ("covid_related_info_by_state.csv") that contains rows in the following format:

```commandline
state,state_id,total_policies,total_cases
Michigan,MI,18,190000
California,CA,16,900000
New York,NY,20,500000
...
```

The final result may be different from the example above. This is only to show the format.

## Data description and Set up

### Data

* `us_policy_updates.csv` is obtained from <https://healthdata.gov/dataset/covid-19-state-and-county-policy-orders>.
* `us_covid19_cases.txt` is adopted from <https://covid.cdc.gov/covid-data-tracker/#cases_casesper100k>.
* The 50 states and their ids  are obtained from <https://gist.github.com/rogerallen/1583593>.
* All data were modified for the purpose of this excercise. Last accessed on October 30th, 2020.

### Set up

* An in-built package, `csv`, is imported to read a csv file.
* A dictionary `state2state_id` is pre-defined, which contains the 50 states and their id's as key-value pairs.
* All input and output files are expected to be located in the same directory with your python script.

### Additional notes

* These datasets may include US territories or federal districts in `state` or `state_id` column. During this exercise, you may ignore those and proceed until Problem 04. In Problem 04, you will use the dictionary `state2state_id` to filter only the 50 states.
* There is NO NEED to make data as lowercase letters or other forms. Just use the data as they are.
* All examples below may contain different or incomplete information than the actual data. They are just to provide clarification and expected formats of outcome.

## 1.0 Problem 01 (20 Points)

Let's first build two functions to read the datasets

1. Implement a function  `read_txt()` that takes a txt filepath string and returns a list of lists where
   each item (list) contains row information seperated by tab `\t`. The first row (column names) will be excluded.

   The txt file is structured as following:

   ```commandline
   State\tCases\n
   Alabama\t189149\n
   Alaska\t15417\n
   ...
   ```

   After reading the txt file through `read_txt()`, the returned list is:

   ```python
   [['Alabama', '189149'], ['Alaska', '15417'], ... ]
   ```

2. Call the function `read_txt()` to read the txt file and assign the returned list to a variable `cases`.

3. Implement a function  `read_csv()` that takes a csv filepath string and returns a list of dictionaries 
   where each item (dictionary) contains columns as keys and relevant row information as values. Hint: consider the csv method DictReader().

   The csv file is structured as the followings:

   ```commandline
   state_id,county,policy_level,date,policy_type,start_stop
   TX,Borden,county,7/3/20,Mask Requirement,start
   TN,,state,3/25/20,Stop Initiation Of Evictions Overall Or Due To Covid Related Issues,start
   ...
   ```

   After reading the csv file through `read_csv()`, the returned list is:

   ```python
   [{'state_id' : 'TX',
   'county' : 'Borden',
   'policy_level' : 'county',
   'date' : '7/3/20',
   'policy_type' : 'Mask Requirement',
   'start_stop' : 'start'},
   {'state_id' : 'TN',
   'county' : '',
   'policy_level' : 'state',
   'date' : '3/25/20',
   'policy_type' : 'Stop Initiation ...',
   'start_stop' : 'start'},
   ... ]
   ```

   :exclamation: the second row `TN,,state,3/25/20,Stop Initiation Of Evictions Overall Or Due To Covid Related Issues,start` has an empty value in the second position. The second value will become an empty string for the corresponding key (e.g., `'county' : ''`).

4. Call the function `read_csv()` to read the csv file and assign the returned list to a variable `policies`.

## 2.0 Problem 02 (10 Points)

The variable `cases` has US states and their total number of COVID-19 cases. Currently, the data structure is somewhat less optimal for this analysis. Let's make it into a dictionary so that you can easily access COVID-19 cases for US states.

1. Implement a function `convert_to_dict()` that takes a list of lists `cases` and returns a dictionary
   that have US states and their number of COVID-19 cases as key-value pairs.

   `cases` is structured as the followings:

   ```python
   [['Alabama', '189149'], ['Alaska', '15417'], ... ]
   ```

   After running `convert_to_dict()`, the returned list is:

   ```python
   {'Alabama' : '189149',
   'Alaska' : '15417',
   ...}
   ```

2. Call the function `convert_to_dict()` to convert `cases` and assign the returned dictionary to a variable `state2cases`.

## 3.0 Problem 03 (30 Points)

Let's analyze how many state-level polices were enacted for each state.

1. Implement a function `get_total_num_policies()` that takes a list of dictionaries `policies` and
   returns a dictionary that has keys represent each state id and values represent the number of state-level policies enacted.

   You need to filter the policy level as state and avoid double counting the number of policies. For example,

   ```commandline
   state_id,policy_level,policy,start_stop
   MI,state,x,start
   MI,state,y,start
   MI,county,z,start
   MI,state,y,stop
   MI,state,w,start
   ```

   Then, (1) state-level policy x has been started, (2) state-level policy y was started and stopped, and (3) state-level w has been started. In total, 3 state_level policies have been enacted in MI.

   The returned dictionary would be as the followings:

   ```commandline
   {'MI' : 3,
   'MA' : 5,
   ...}
   ```

2. Call the function `get_total_num_policies()` to get the number of state-level policies per state and
   assign the returned dictionary to a variable `state_id2policies`. Again, `policies` needs to be passed as a parameter.

## 4.0 Problem 04 (30 Points)

You have created variables `state2cases` and `state_id2policies`. Let's summarize the analysis.

1. Implement a function `summarize_data()` that takes three dictionaries in the order of
   `state2state_id`, `state_id2policies`, and `state2cases` as parameters and returns a list of dictionaries where each dictionary contains 4 key-value pairs for state information such as state name, state id, the total number of state-level policies, and the total number of COVID-19 cases. Hint: consider how each dictionary's key-value pairs are linked.

   Keys are `state` for state name, `state_id` for state id, `total_policies` for the total number of state-level policies, and `total_cases` for the total number of COVID-19 cases.

   Values are the relevant information for each state.

   For example, if Michigan had 15 state-level policies and 15000 COVID-19 cases, then a dicionary would contain the following:

   ```commandline
   {'state' : 'Michigan',
   'state_id' : 'MI',
   'total_policies' : 15,
   'total_cases' : 15000}
   ```

   The returned list would contain the 50 states dictionaries.

2. Call the function `summarize_data()` to summarize the analysis and assign the returned list to a 
   variable `summarized_info`. Again, `state2state_id`, `state_id2policies`, and `state2cases` need to be passed as parameters.

## 5.0 Problem 05 (10 Points)

Let's write your work to a csv file.

1. Implement a function `write_csv()` that takes two parameters: a list of dictionaries and a csv
   filepath. The function writes the list of dictionaries to a csv file.

   For example, if the function was correctly implemented, then we should be able to find a csv fille `state_covid19_related_info.csv` in the same directory after running `write_csv(summarized_info, "state_covid19_related_info.csv")`. The csv file would contain as the followings:

   ```commandline
   state,state_id,total_policies,total_cases
   Alabama,AL,17,189149
   Alaska,AK,16,15417
   Arizona,AZ,14,242480
   ...
   ```

   :exclamation: you will not see the commas in your csv file if you open it in Excel or another spreadsheet app. Rather, each data would be stored in cells as comma-seprated values.

2. Call the function `write_csv()` to write your analysis `summarized_info` to a new csv file with any name you would like. Open the file and see your analysis. Enjoy!
