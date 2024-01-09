### This code keeps only the zeroth instance in the UKBB Data File
library(data.table)
options(scipen = 999) ## To avoid scientific notation
df <- fread ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/2_Olink_Data_T.txt")
df_1 <- subset (df, df$ins_index == 0)
write.table (df_1, "/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/3_Olink_Data_Full_O_Instance.txt")), sep="\t", quote=FALSE, row.names=FALSE, col.names=TRUE)
