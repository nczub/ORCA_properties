# import packages
import pandas as pd
import numpy as np
import os
import glob

# assign directory
directory = 'GLASS_db_results'

list_of_compounds = os.listdir(directory)

# make directory for results
os.mkdir("GLASS_results")


for filename in list_of_compounds:
#     if filename.is_file():
    id_compound = filename
    # read file
    text_file = pd.read_csv(f"{directory}/{id_compound}/{id_compound}_property.txt", header = None, sep = "\t")
    text_file.columns = ["information"]

    # delete rows starting with --
    df = text_file[text_file["information"].str.contains("--") == False]

    # limit dataframe - until coordinates
    index_number = df.index[df['information'] == "    Coordinates:"][0]
    df_1 = df.loc[:index_number-1]

    # delete rows which are starting with $ and *
    df_2 = df_1[~df_1.information.str.startswith(('$', '*'))]

    df = df_2
    df=df.replace('\:',' ',regex=True)

    # get last value from column and save as another column
    df["info"] = df["information"].str.split('(\s{2,})').str[-1]

    # save file and read to update indexes
    df.to_csv("info.csv", index = False)
    df = pd.read_csv("info.csv")
    
    # column one by one changing values in column information by index number
    df.information[0] = "description_the_PAL_flags"
    df.information[1] = "PAL_flags_geom_index"
    df.information[2] = "PAL_flags_prop_index"
    df.information[3] = "Diskflag"
    df.information[4] = "description_the_SCF_energy"
    df.information[5] = "SCF_geom_index"
    df.information[6] = "SCF_prop_index"
    df.information[7] = "SCF_energy"
    df.information[8] = "description_the_DFT_energy"
    df.information[9] = "DFT_geom_index"

    df.information[10] = "DFT_prop_index"
    df.information[11] = "Number_of_Alpha_Electrons"
    df.information[12] = "Number_of_Beta_Electrons"
    df.information[13] = "Total_number_of_Electrons"
    df.information[14] = "Exchange_energy"
    df.information[15] = "Correlation_energy"
    df.information[16] = "Correlation_energy_NL"
    df.information[17] = "Exchange-Correlation_energy"
    df.information[18] = "Embedding_correction"
    df.information[19] = "Total_DFT_Energy_No_VdW_correction"

    df.information[20] = "description_Details_concerning_solvation"
    df.information[21] = "solvation_geom_index"
    df.information[22] = "solvation_prop_index"
    df.information[23] = "epsilon"
    df.information[24] = "Refrac"
    df.information[25] = "Rsolv"
    df.information[26] = "Surface_type"
    df.information[27] = "Number_of_points"
    df.information[28] = "Surface_area"
    df.information[29] = "Dielectric_Energy"

    df.information[30] = "description_Details_of_the_calculation"
    df.information[31] = "geom_index"
    df.information[32] = "prop_index"
    df.information[33] = "Multiplicity"
    df.information[34] = "Charge"
    df.information[35] = "Number_of_atoms"
    df.information[36] = "Number_of_electrons"
    df.information[37] = "number_of_frozen_core_electrons"
    df.information[38] = "number_of_correlated_electrons"
    df.information[39] = "number_of_basis_functions"

    df.information[40] = "number_of_aux_C_basis_functions"
    df.information[41] = "number_of_aux_J_basis_functions"
    df.information[42] = "number_of_aux_JK_basis_functions"
    df.information[43] = "number_of_aux_CABS_basis_functions"
    df.information[44] = "total_energy"
    df.information[45] = "description_The_SCF_Calculated_Electric_Properties"
    df.information[46] = "SCF_calculated_electronic_properties_geom_index"
    df.information[47] = "SCF_calculated_electronic_properties_prop_index"
    df.information[48] = "Filename"
    df.information[49] = "Do_Dipole_Moment_Calculation"

    df.information[50] = "Do_Quadrupole_Moment_Calculation"
    df.information[51] = "Do_Polarizability_Calculation"
    df.information[52] = "Magnitude_of_dipole_moment_Debye"
    df.information[53] = "Electronic_Contribution"
    df.information[54] = "0_delete"
    df.information[55] = "electronic_contribution_0"
    df.information[56] = "electronic_contribution_1"
    df.information[57] = "electronic_contribution_2"
    df.information[58] = "Nuclear_contribution"
    df.information[59] = "0_delete_1"

    df.information[60] = "nuclear_contribution_0"
    df.information[61] = "nuclear_contribution_1"
    df.information[62] = "nuclear_contribution_2"
    df.information[63] = "total_dipole_moment"
    df.information[64] = "0_delete_2"
    df.information[65] = "total_dipole_moment_0"
    df.information[66] = "total_dipole_moment_1"
    df.information[67] = "total_dipole_moment_2"
    df.information[68] = "Number_of_atoms_2"
    df.information[69] = "geometry_index"
    
    # delete rows where in info column there are missig values or string
    df = df.dropna(axis=0)

    df.drop(0, inplace = True)
    df.drop(4, inplace = True)
    df.drop(8, inplace = True)
    df.drop(20, inplace = True)
    df.drop(30, inplace = True)
    df.drop(45, inplace = True)
    df.drop(48, inplace = True)
    df.drop(53, inplace = True)
    df.drop(58, inplace = True)
    df.drop(63, inplace = True)
    
    # transpose file
    df.transpose().to_csv("info.csv", index = False, header = False)
    df = pd.read_csv("info.csv")

    # add row with id of compound
    df.insert(0, "id", id_compound)

    # save ready database
    df.to_csv(f"GLASS_results/{id_compound}.csv", index = False, header = True)
    
# setting the path for joining multiple files
files = os.path.join("GLASS_results/", "*.csv")

# list of merged files returned
files = glob.glob(files)

# print("Resultant CSV after joining all CSV files at a particular location...");

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
df.to_csv("FINAL_ORCA_GLASS_results.csv", index = False, header = True)
