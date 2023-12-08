library(data.table)
options(scipen = 999) ## To avoid scientific notation
df <- fread ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/Olink_Data_Full.csv")
write.table (df_1, "/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/2_Olink_Data_T.txt")), sep="\t", quote=FALSE, row.names=FALSE, col.names=TRUE)
