#!/usr/bin/env python
# coding: utf-8

# In[8]:


import csv
time=[208.7133800983429, 135.62777972221375, 179.78176403045654, 111.06691122055054, 218.42338848114014, 349.30329728126526, 362.7245376110077, 61.384018421173096, 128.65686130523682, 293.4410490989685, 257.1202311515808, 176.0993115901947, 99.61482524871826, 188.2633171081543, 227.80447912216187, 149.89113068580627, 452.4840176105499, 417.497430562973, 128.62110877037048, 218.63702034950256, 440.1166522502899, 297.6168911457062, 318.3990969657898, 100.72965598106384, 100.72965598106384, 209.26376914978027, 173.29814505577087, 458.5433933734894, 306.49381589889526, 129.227534532547, 171.57951378822327, 332.8140141963959, 260.7096064090729, 311.51833939552307, 133.87119722366333, 172.95134735107422, 179.59322476387024, 225.5516288280487, 721.8786392211914, 286.96784353256226, 153.72603154182434, 216.78307938575745, 309.1633188724518, 268.96244072914124, 127.9039978981018, 119.80234909057617, 199.87805271148682, 402.4983067512512, 407.71006059646606, 381.69515895843506, 315.6492109298706, 76.28204083442688, 213.59277606010437, 344.2993083000183, 137.6688346862793,140.2928466796875, 112.80537939071655, 142.16640090942383, 223.26786708831787, 142.03691864013672, 257.2778196334839, 254.6521487236023, 232.7581558227539, 125.16602110862732, 266.1774146556854, 204.03434872627258, 280.6443614959717, 199.2194118499756, 160.4031503200531, 167.27761912345886, 343.4018359184265, 419.17458033561707, 761.583324432373, 190.04885578155518, 143.87972736358643, 301.73620891571045, 123.6330668926239, 166.06362199783325, 108.67385268211365, 170.69138360023499, 248.9096176624298, 142.9843020439148, 294.94529700279236, 225.24116683006287, 84.43312954902649, 181.6201376914978, 267.8663446903229, 191.51133108139038, 178.2396388053894, 99.13160490989685, 252.64483904838562, 262.7026698589325, 219.08405089378357, 377.70781540870667, 255.04838299751282, 118.81273365020752, 158.51230669021606, 319.5718421936035, 171.1913297176361, 172.5461709499359, 101.58276963233948, 116.51613211631775, 160.02915811538696, 220.3242700099945, 331.25085496902466, 1004.5193758010864, 92.90349626541138, 133.7368552684784, 411.48442792892456, 205.28071999549866]
import numpy as np
import numpy.linalg as la

from mergehdf51 import DataMerger
import matplotlib.pyplot as plt

data_merger = DataMerger()
files = []
file.append(['name','https://github.com/yiwangj/cis-2-project-data-analysis/tree/main/Data%20Set')
# files.append(['C_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L1_color/2023-04-13 10:15:01'])
# files.append(['K_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L1_color/2023-04-06 09:56:30'])
# files.append(['P_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L1_color/2023-04-06 09:08:17'])
# files.append(['T_P0_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L1_color/2023-04-06 11:48:45'])
# files.append(['E_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P0_L1_color_v2'])
# files.append(['G_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P0_L1_color'])
# files.append(['O_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P0_L1_color'])
# files.append(['V_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P0_L1_color'])
# files.append(['A_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P0_L1_color'])
# files.append(['J_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P0_L1_color'])
# files.append(['Z_P0_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P0_L1_color'])


# files.append(['C_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P0_L3_color/2023-04-13 10:51:15'])
# files.append(['K_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/klobo_P0_L3_color/2023-04-06 10:24:32'])
# files.append(['P_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P0_L3_color/2023-04-06 09:34:53'])
# files.append(['T_P0_L3_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P0_L3_color_v2/2023-04-06 11:13:31'])
# files.append(['E_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P0_L3_color'])
# files.append(['G_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P0_L3_color'])
# files.append(['O_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P0_L3_color'])
# files.append(['V_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P0_L3_color'])
# files.append(['A_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P0_L3_color'])
# files.append(['J_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P0_L3_color'])
# files.append(['Z_P0_L3_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P0_L3_color'])


# files.append(['C_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L2_color/2023-04-13 10:38:13'])
# files.append(['K_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
# files.append(['P_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L2_color/2023-04-06 10:11:54'])
# files.append(['T_P2_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L2_color/2023-04-06 11:34:55'])
# files.append(['E_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P2_L2_color'])
# files.append(['G_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P2_L2_color'])
# files.append(['O_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P2_L2_color'])
# files.append(['V_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P2_L2_color'])
# files.append(['A_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P2_L2_color'])
# files.append(['J_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P2_L2_color'])
# files.append(['Z_P2_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P2_L2_color'])


# files.append(['C_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L2_color/2023-04-13 10:08:49'])
# files.append(['K_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L2_color/2023-04-06 10:08:32'])
# files.append(['P_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L2_color/2023-04-06 09:18:08'])
# files.append(['T_P4_L2_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L2_color/2023-04-06 11:44:29'])
# files.append(['E_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P4_L2_color'])
# files.append(['G_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P4_L2_color'])
# files.append(['O_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P4_L2_color'])
# files.append(['V_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P4_L2_color'])
# files.append(['A_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P4_L2_color'])
# files.append(['J_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P4_L2_color'])
# files.append(['Z_P4_L2_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P4_L2_color'])


# files.append(['C_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L1_color/2023-04-13 10:48:22'])
# files.append(['K_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L1_color/2023-04-06 10:05:35'])
# files.append(['P_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L1_color/2023-04-06 09:03:13'])
# files.append(['T_P7_L1_color', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L1_color/2023-04-06 10:58:37'])
# files.append(['E_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P7_L1_color'])
# files.append(['G_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P7_L1_color'])
# files.append(['O_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P7_L1_color'])
# files.append(['V_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P7_L1_color'])
# files.append(['A_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P7_L1_color'])
# files.append(['J_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P7_L1_color'])
# files.append(['Z_P7_L1_color', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P7_L1_color'])



# files.append(['C_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L1_no_color/2023-04-13 10:44:15'])
# files.append(['K_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L1_no_color/2023-04-06 10:21:48'])
# files.append(['P_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L1_no_color_v2/2023-04-06 08:52:32'])
# files.append(['T_P1_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L1_no_color/2023-04-06 11:26:28'])
# files.append(['E_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P1_L1_no_color'])
# files.append(['G_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P1_L1_no_color'])
# files.append(['O_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P1_L1_no_color'])
# files.append(['V_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P1_L1_no_color_v2'])
# files.append(['A_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P1_L1_no_color'])
# files.append(['J_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P1_L1_no_color'])
# files.append(['Z_P1_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P1_L1_no_color'])

# files.append(['C_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P1_L3_no_color/2023-04-13 10:32:25'])
# files.append(['K_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P1_L3_no_color/2023-04-06 09:59:55'])
# files.append(['P_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P1_L3_no_color/2023-04-06 09:14:06'])
# files.append(['T_P1_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P1_L3_no_color/2023-04-06 11:39:26'])
# files.append(['E_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P1_L3_no_color'])
# files.append(['G_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P1_L3_no_color'])
# files.append(['O_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P1_L3_no_color'])
# files.append(['V_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P1_L3_no_color'])
# files.append(['A_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P1_L3_no_color'])
# files.append(['J_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P1_L3_no_color'])
# files.append(['Z_P1_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P1_L3_no_color'])

# files.append(['C_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P2_L1_no_color/2023-04-13 10:23:43'])
# files.append(['K_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P2_L1_no_color/2023-04-06 10:17:49'])
# files.append(['P_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P2_L1_no_color/2023-04-06 09:22:09'])
# files.append(['T_P2_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P2_L1_no_color/2023-04-06 11:07:07'])
# files.append(['E_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P2_L1_no_color'])
# files.append(['G_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P2_L1_no_color'])
# files.append(['O_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P2_L1_no_color'])
# files.append(['V_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P2_L1_no_color'])
# files.append(['A_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P2_L1_no_color'])
# files.append(['J_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P2_L1_no_color'])
# files.append(['Z_P2_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P2_L1_no_color'])






# files.append(['C_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P4_L1_no_color/2023-04-13 10:19:26'])
# files.append(['K_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P4_L1_no_color/2023-04-06 09:53:16'])
# files.append(['P_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P4_L1_no_color/2023-04-06 08:57:24'])
# files.append(['T_P4_L1_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P4_L1_no_color/2023-04-06 11:18:42'])
# files.append(['E_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P4_L1_no_color'])
# files.append(['G_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P4_L1_no_color'])
# files.append(['O_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P4_L1_no_color_v2'])
# files.append(['V_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P4_L1_no_color'])
# files.append(['A_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P4_L1_no_color'])
# files.append(['J_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P4_L1_no_color'])
# files.append(['Z_P4_L1_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P4_L1_no_color'])




# files.append(['C_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/cxoxe_P7_L3_no_color/2023-04-13 10:28:22'])
# files.append(['K_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/klobo_P7_L3_no_color/2023-04-06 10:15:10'])
# files.append(['P_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/pexvxk_P7_L3_no_color/2023-04-06 09:31:26'])
# files.append(['T_P7_L3_nocolor', '/Users/wangyi/Downloads/Source_Data/tbpq_P7_L3_no_color/2023-04-06 11:31:01'])
# files.append(['E_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/exoofp-participant/exoofp_P7_L3_no_color'])
# files.append(['G_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/grxk-participant/grxk_P7_L3_no_color'])
# files.append(['O_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/oxzebi-participant/oxzebi_P7_L3_no_color'])
# files.append(['V_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/4-27-Testing/vbpex-participant/vbpex_P7_L3_no_color'])
# files.append(['A_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/axkfbi-participant/axkfbi_P7_L3_no_color'])
# files.append(['J_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/jxga-participant/jxga_P7_L3_no_color'])
# files.append(['Z_P7_L3_nocolor', '/Users/wangyi/Downloads/Laminectomy_UserStudy_Data/5-4-Testing/zixox-participant/zixox_P7_L3_no_color'])



participant=['cxoxe','klobo','pexvxk','tbpq','exoofp','grxk','oxzebi','vbpex','axkfbi','jxga','zixox']
count=0
with open('voxel_time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "participant","Name", "time"])


    for lab, fl in files: 
        rem=count%11
        
        writer.writerow([participant[rem],lab,time[count]])
        count=count+1
    


# In[ ]:




