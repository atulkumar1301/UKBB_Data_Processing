### This code merges NPX and LOD data
f_m = open("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/8_Olink_Data_NPX_LOD.txt", 'w', 1)
with open ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/6_Olink_Data_Merged_Demographic.txt", 'r') as olink:
    pro = olink.readline ()
    f_m.write (pro)
    for pro in olink:
        pro_list = pro.split ("\t")
        with open ("/Volumes/ATUL_6TB/Data/UKBB/Olink_Data/Olink_New/7_Olink_Data_Lod.txt", 'r') as lod:
            lod_line = lod.readline ()
            for lod_line in lod:
                 lod_list = lod_line.split ("\t")
                 #print (type (lod_list [1]))
                 if ((int(pro_list [610]) == int(lod_list [1])) and (int(lod_list [2]) == 0)):
                     f_m.write (str.rstrip (pro) + "\t" + lod_line)
