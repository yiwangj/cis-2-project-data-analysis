#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
force=[0.18033457228267263, 0.18033906781228423, 0.23901967070628108, 0.14367495870210284, 0.20361473878232747, 0.09913806542841287, 0.17430788071522604, 0.16060641198599165, 0.28578775965004605, 0.38655268148364186, 0.12944605199251566, 0.20189461104347872, 0.34998779224659543, 0.18482718626370107, 0.11648836538675403, 0.16264210991236186, 0.10211682868680479, 0.21840571294939198, 0.9044992569908759, 0.25543331139052283, 0.19317951315381685, 0.13588674653099367, 0.2581189714590836, 0.3369540823206421, 0.3369540823206421, 0.15234576859837867, 0.1883863935079098, 0.12297807076525633, 0.16145944295393294, 0.5006964725731385, 0.2949582084423049, 0.1744329674109626, 0.1886687166190007, 0.229502172602097, 0.29277242291601285, 0.2566425217525285, 0.15762209598632365, 0.20977671764155312, 0.12101277682211667, 0.33227507831801356, 0.2623066656638799, 0.27238777843822193, 0.34374183774921496, 0.1958527861050808, 0.18644724665433468, 0.42454384742298673, 0.23207744775714576, 0.11584882191326121, 0.15746408079950178, 0.18033546026862407, 0.17567257360708555, 0.48954424986255335, 0.24169969030274094, 0.2784241379118365, 0.18310496761558506,0.2621758368683224, 0.38821864522015054, 0.152157748254327, 0.14989170918496036, 0.22733727834351872, 0.15642548146575821, 0.6168914991315634, 0.1922684427289063, 0.34397404628983486, 0.39267397046347846, 0.17491368336002502, 0.2476397976660031, 0.686877599150128, 0.3138460595153785, 0.21535097766861533, 0.22136424228090618, 0.14933821253748422, 0.2688253619500689, 0.4762704325488646, 0.47071588463864195, 0.31945033285910174, 0.23497990368367444, 0.2612277910058245, 0.2563305807315853, 0.28830719869296806, 0.12082365418561004, 0.17974779427161316, 0.1052680583473639, 0.2071688706784853, 0.2883868851657753, 0.1944080388751278, 0.43038874162763147, 0.16654654576252323, 0.24687428512629786, 0.2201904896635752, 0.22125803042774722, 0.14752803205796652, 0.21924661986208116, 0.20361303475399678, 0.19700659152993155, 0.18958843013590496, 0.30669085849985883, 0.5044258389086258, 0.7224992686770584, 0.15366446454477461, 0.21698547044364574, 0.1935408600429171, 0.13070077336801358, 0.17218986726046012, 0.10434169441181951, 0.24867894291285678, 0.9839632471714954, 0.2518441907218534, 0.2661248404645288, 0.11394712137297687]
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
with open('force.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "participant","Name", "time"])


    for lab, fl in files: 
        rem=count%11
        
        writer.writerow([participant[rem],lab,force[count]])
        count=count+1
    


# In[ ]:




