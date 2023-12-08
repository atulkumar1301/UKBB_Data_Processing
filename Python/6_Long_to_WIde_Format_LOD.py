import pandas as pd
df = pd.read_csv ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/olink_limit_of_detection.dat", delimiter="\t")
df_1 = pd.pivot_table (df, index = ['PlateID', 'Instance'], columns = 'Assay', values = 'LOD', aggfunc = 'first')
df_1.to_csv ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/Olink_Data_LOD.csv", sep=",", index=True)
