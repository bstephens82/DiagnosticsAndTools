#!/usr/bin/env python

import os


print("cleaning diags_output/*")
os.system("rm -rf diags_output/*")

print("cleaning data/*")
os.system("rm data/*")

print("cleaning data_job* files...")
os.system("rm -rf data_job*")

print("removing runcasp/runder files")
os.system("rm runcasp.clubb_profiles_*")

print("removing CAM_CLUBB_diag_*")
os.system("rm CAM_CLUBB_diag_*")
#print("replacing config files")
#os.system("cp orig/* .")



