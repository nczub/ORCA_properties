# ORCA_properties
For data cleaning of ORCA properties

Results of ORCA calculations are presented in folder "GLASS_db_results". Based on this directory and inside of each molecule folder you can find file with propert e.g. GLASS_100738_property.txt. This is an output of ORCA calculation after setting output as !MiniPrint. 

In Python script you need to asign you directory. Based on this code will clean your data from ORCA calculation.

Result for each compound will be saved in GLASS_results directory and final result in file 'FINAL_ORCA_GLASS_results.csv'

# Requirements
- pandas
- numpy
- os
- glob

