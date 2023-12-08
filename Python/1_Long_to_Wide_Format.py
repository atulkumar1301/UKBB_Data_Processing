### This code converts long-format Olink Data to wide-format 
import pandas as pd
df = pd.read_csv ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/olink_data_3000.txt", delimiter="\t")
df_1 = pd.pivot_table (df, index = ['eid', 'ins_index'], columns = 'protein_id', values = 'result', aggfunc = 'first')
df_1.to_csv ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/Olink_Data_Full.csv", sep=",", index=True)
