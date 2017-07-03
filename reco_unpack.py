import sys
import os
import json
from subprocess import call

if len(sys.argv) < 3:
    print "Please insert the folder containing the raw files and the output folder"
    exit(1)

inputFolder = sys.argv[1]
runNumber = inputFolder.split("/")[-1][3:]
tempFolder = "/tmp"
outputFolder = sys.argv[2] + "/run"+ runNumber


if len(sys.argv) == 4:
    threads = sys.argv[3]
else:
    threads = 2

print "\n====================================== Processing run: {0} ==============================\n".format(runNumber)

command_fu = "cmsRun RawReader.py inputFolder={0} fuBaseDir={1} runNumber={2} numThreads={3}".format(inputFolder, tempFolder, runNumber, threads)
print command_fu
call(command_fu, shell=True)

print "\n================================= Fixing output files =============================\n"

tempFolder += "/run"+ runNumber 
#now we have to do the cuts
ini = [tempFolder + "/" + f for f in os.listdir(tempFolder) if "streamDQM" in f and f.endswith(".ini")][0]
dats = sorted([tempFolder + "/"+ f for f in os.listdir(tempFolder) if "streamDQM" in f and f.endswith(".dat")])
jsn = sorted([tempFolder + "/"+ f for f in os.listdir(tempFolder) if "streamDQM" in f and f.endswith(".jsn")])[0]
jsn_name = jsn.split("/")[-1]
first_dat_name = dats[0].split("/")[-1]

call("cat {0} > {1}/run{2}.dat".format(ini, tempFolder, runNumber), shell=True)
for dat in dats:
    call("cat {0} >> {1}/run{2}.dat".format(dat, tempFolder, runNumber), shell=True)

# Fixing json
f = open(jsn,'r')
jsn_obj = json.loads(f.read())
f.close()
jsn_obj["data"].pop(2)
json.dump(jsn_obj, open(jsn,'w'), indent=4)

# Moving files
print "\n================================ Moving files to final directory ==============================\n"

make_dir = "mkdir {0}".format(outputFolder)
move_dat = "mv {0}/run{1}.dat {2}/{3}".format(tempFolder, runNumber, outputFolder, first_dat_name)
move_jsn = "mv {0} {1}/{2}".format( jsn, outputFolder, jsn_name)
touch_jsn = "touch {0}/run{1}_streamDQM_ls0000_EoR.jsn".format(outputFolder, runNumber)       

print make_dir
call(make_dir, shell=True)
print move_dat
call(move_dat, shell=True)
print move_jsn
call(move_jsn, shell=True)
print touch_jsn
call(touch_jsn, shell=True)

rm_temp = "rm -r {0}".format(tempFolder)
print rm_temp
call(rm_temp, shell=True)


