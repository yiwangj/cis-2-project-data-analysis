#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
list1=[40860, 27388, 27748, 27992, 27442, 27570, 26314, 26110, 31292, 29528, 28554, 70108, 52462, 55846, 55368, 56616, 55908, 71090, 48466, 59746, 58044, 56468, 60152, 58452, 58452, 60958, 59094, 63084, 61214, 63466, 64018, 60708, 61112, 97548, 82842, 93086, 94156, 97114, 95010, 96172, 88172, 97088, 99388, 95066, 54660, 33950, 30398, 35426, 35718, 38846, 36208, 35430, 36070, 36426, 36242]
list2=[61190, 50254, 52824, 63634, 57890, 58104, 65378, 55682, 60478, 99634, 45564, 106486, 88036, 87926, 112302, 100748, 89992, 122872, 85330, 95464, 108040, 63668, 62014, 50176, 59976, 60996, 59054, 58484, 61046, 52040, 62132, 66298, 49476, 62152, 38760, 47636, 60180, 62294, 63086, 61302, 52962, 63126, 86054, 31182, 46504, 30976, 39744, 37166, 31570, 37584, 51762, 34718, 47428, 45238, 38622]
list3=[41328, 14434, 9440, 11306, 11166, 7130, 26262, 442, 33200, 28026, 21760, 22348, 7862, 6312, 5766, 10996, 3682, 18826, 1536, 29210, 29188, 18198, 28090, 13222, 13222, 18288, 19292, 17408, 26232, 392, 43432, 38340, 27360, 30126, 3186, 2232, 2868, 29544, 7606, 6968, 1288, 32924, 42764, 10106, 13104, 1916, 778, 966, 8552, 3390, 6072, 3084, 18112, 21106, 5152]
list4=[31612, 9328, 4610, 18952, 18478, 4268, 12726, 7306, 27222, 64976, 1652, 51640, 17978, 8410, 1330, 34478, 2536, 93740, 11120, 12550, 37064, 50, 24288, 23666, 12162, 8500, 4520, 2382, 10092, 17848, 18824, 46576, 3440, 31720, 11816, 9140, 19560, 16708, 4546, 28366, 4292, 29736, 73154, 12080, 11238, 11402, 2416, 11242, 13020, 2212, 50346, 2946, 18110, 24138, 142]
list5=[42882, 22208, 20940, 21468, 24668, 22692, 27104, 7294, 28272, 27522, 27848, 38640, 21060, 28752, 25838, 32916, 31576, 35774, 7432, 40836, 41206, 36802, 62436, 37558, 37558, 55316, 58840, 56662, 61946, 16444, 65520, 65668, 60228, 74868, 22634, 32716, 38446, 65468, 50522, 47162, 13124, 74306, 74764, 53724, 36795, 13808, 6078, 16640, 24706, 21286, 21446, 6800, 26884, 27720, 19778]
list6=[42232, 27488, 19808, 32272, 29752, 24338, 33850, 25096, 37124, 46788, 10982, 54182, 22218, 22782, 8368, 54504, 11104, 65172, 20340, 33290, 41422, 5132, 40486, 26080, 30884, 31584, 22634, 14494, 36482, 25888, 38306, 39488, 21784, 54718, 23398, 19386, 41126, 30002, 26842, 52008, 19136, 49378, 60742, 29530, 29086, 11464, 11966, 15582, 11646, 10154, 40180, 12278, 31378, 30438, 6274]
combined_list = []
combined_list.extend(list1)
combined_list.extend(list2)
combined_list.extend(list3)
combined_list.extend(list4)
combined_list.extend(list5)
combined_list.extend(list6)
print(len(combined_list))
import numpy.linalg as la

from mergehdf51 import DataMerger
import matplotlib.pyplot as plt

data_merger = DataMerger()
files = []
files.append(['C_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L1_color/2023-04-13 10:15:01'])
files.append(['K_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L1_color/2023-04-06 09:56:30'])
files.append(['P_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L1_color/2023-04-06 09:08:17'])
files.append(['T_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L1_color/2023-04-06 11:48:45'])
files.append(['E_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P0_L1_color_v2'])
files.append(['G_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P0_L1_color'])
files.append(['O_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P0_L1_color'])
files.append(['V_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P0_L1_color'])
files.append(['A_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P0_L1_color'])
files.append(['J_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P0_L1_color'])
files.append(['Z_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P0_L1_color'])


files.append(['C_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L3_color/2023-04-13 10:51:15'])
files.append(['K_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L3_color/2023-04-06 10:24:32'])
files.append(['P_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L3_color/2023-04-06 09:34:53'])
files.append(['T_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L3_color_v2/2023-04-06 11:13:31'])
files.append(['E_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P0_L3_color'])
files.append(['G_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P0_L3_color'])
files.append(['O_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P0_L3_color'])
files.append(['V_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P0_L3_color'])
files.append(['A_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P0_L3_color'])
files.append(['J_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P0_L3_color'])
files.append(['Z_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P0_L3_color'])


files.append(['C_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L2_color/2023-04-13 10:38:13'])
files.append(['K_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
files.append(['P_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
files.append(['T_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L2_color/2023-04-06 11:34:55'])
files.append(['E_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P2_L2_color'])
files.append(['G_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P2_L2_color'])
files.append(['O_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P2_L2_color'])
files.append(['V_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P2_L2_color'])
files.append(['A_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P2_L2_color'])
files.append(['J_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P2_L2_color'])
files.append(['Z_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P2_L2_color'])


files.append(['C_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L2_color/2023-04-13 10:08:49'])
files.append(['K_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L2_color/2023-04-06 10:08:32'])
files.append(['P_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L2_color/2023-04-06 09:18:08'])
files.append(['T_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L2_color/2023-04-06 11:44:29'])
files.append(['E_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P4_L2_color'])
files.append(['G_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P4_L2_color'])
files.append(['O_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P4_L2_color'])
files.append(['V_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P4_L2_color'])
files.append(['A_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P4_L2_color'])
files.append(['J_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P4_L2_color'])
files.append(['Z_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P4_L2_color'])


files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])
files.append(['E_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P7_L1_color'])
files.append(['G_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P7_L1_color'])
files.append(['O_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P7_L1_color'])
files.append(['V_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P7_L1_color'])
files.append(['A_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P7_L1_color'])
files.append(['J_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P7_L1_color'])
files.append(['Z_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P7_L1_color'])

files.append(['C_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L1_no_color/2023-04-13 10:44:15'])
files.append(['K_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L1_no_color/2023-04-06 10:21:48'])
files.append(['P_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L1_no_color_v2/2023-04-06 08:52:32'])
files.append(['T_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L1_no_color/2023-04-06 11:26:28'])
files.append(['E_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P1_L1_no_color'])
files.append(['G_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P1_L1_no_color'])
files.append(['O_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P1_L1_no_color'])
files.append(['V_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P1_L1_no_color_v2'])
files.append(['A_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P1_L1_no_color'])
files.append(['J_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P1_L1_no_color'])
files.append(['Z_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P1_L1_no_color'])

files.append(['C_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L3_no_color/2023-04-13 10:32:25'])
files.append(['K_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L3_no_color/2023-04-06 09:59:55'])
files.append(['P_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L3_no_color/2023-04-06 09:14:06'])
files.append(['T_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L3_no_color/2023-04-06 11:39:26'])
files.append(['E_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P1_L3_no_color'])
files.append(['G_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P1_L3_no_color'])
files.append(['O_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P1_L3_no_color'])
files.append(['V_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P1_L3_no_color'])
files.append(['A_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P1_L3_no_color'])
files.append(['J_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P1_L3_no_color'])
files.append(['Z_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P1_L3_no_color'])

files.append(['C_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L1_no_color/2023-04-13 10:23:43'])
files.append(['K_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L1_no_color/2023-04-06 10:17:49'])
files.append(['P_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P2_L1_no_color/2023-04-06 09:22:09'])
files.append(['T_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L1_no_color/2023-04-06 11:07:07'])
files.append(['E_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P2_L1_no_color'])
files.append(['G_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P2_L1_no_color'])
files.append(['O_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P2_L1_no_color'])
files.append(['V_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P2_L1_no_color'])
files.append(['A_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P2_L1_no_color'])
files.append(['J_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P2_L1_no_color'])
files.append(['Z_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P2_L1_no_color'])






files.append(['C_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L1_no_color/2023-04-13 10:19:26'])
files.append(['K_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L1_no_color/2023-04-06 09:53:16'])
files.append(['P_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L1_no_color/2023-04-06 08:57:24'])
files.append(['T_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L1_no_color/2023-04-06 11:18:42'])
files.append(['E_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P4_L1_no_color'])
files.append(['G_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P4_L1_no_color'])
files.append(['O_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P4_L1_no_color_v2'])
files.append(['V_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P4_L1_no_color'])
files.append(['A_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P4_L1_no_color'])
files.append(['J_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P4_L1_no_color'])
files.append(['Z_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P4_L1_no_color'])




files.append(['C_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L3_no_color/2023-04-13 10:28:22'])
files.append(['K_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L3_no_color/2023-04-06 10:15:10'])
files.append(['P_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L3_no_color/2023-04-06 09:31:26'])
files.append(['T_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L3_no_color/2023-04-06 11:31:01'])
files.append(['E_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P7_L3_no_color'])
files.append(['G_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P7_L3_no_color'])
files.append(['O_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P7_L3_no_color'])
files.append(['V_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P7_L3_no_color'])
files.append(['A_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P7_L3_no_color'])
files.append(['J_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P7_L3_no_color'])
files.append(['Z_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P7_L3_no_color'])


participant=['cxoxe','klobo','pexvxk','tbpq','exoofp','grxk','oxzebi','vbpex','axkfbi','jxga','zixox']
color=['green','red','yellow']
count=0
with open('voxel_color_removed.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "participant","Name", "color","number"])


    for lab, fl in files: 
        rem=count%11
        if count<110:
            color='green'
        elif count>219:
            color='yellow'
        else:
            color='red'
            
        writer.writerow([participant[rem],lab,color,combined_list[count]])
        count=count+1
    for lab, fl in files: 
        rem=count%11
        if count<110:
            color='green'
        elif count>219:
            color='yellow'
        else:
            color='red'
            
        writer.writerow([participant[rem],lab,color,combined_list[count]])
        count=count+1
    for lab, fl in files: 
        rem=count%11
        if count<110:
            color='green'
        elif count>219:
            color='yellow'
        else:
            color='red'
            
        writer.writerow([participant[rem],lab,color,combined_list[count]])
        count=count+1


# In[ ]:




