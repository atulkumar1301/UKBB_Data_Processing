###This code calculates a dummy number for plate number and add that column at a desired location
library (tibble)
df <- fread ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/5_Olink_Data_Merged_Demographic.csv")
d = df_1$`30901-0.0` - 890000000000
df_1 <- add_column(df, plate = d, .after = 7)
write.table (df_1, "/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/6_Olink_Data_NPX_Demographic.txt", sep = "\t", quote = FALSE, row.names = FALSE)
