import sys
import os
from subprocess import call

if len(sys.argv) < 3:
    print "Please insert the folder containing the raw files and the output folder"
    exit(1)

inputFolder = sys.argv[1]
runNumber = inputFolder.split("/")[-1][3:]
outputFolder = sys.argv[2]

if len(sys.argv) == 4:
    threads = sys.argv[3]
else:
    threads = 2

print "\n====================================== Processing run: {} ==============================\n".format(runNumber)

command_fu = "cmsRun RawReader.py inputFolder={0} fuBaseDir={1} runNumber={2} numThreads={3}".format(inputFolder,outputFolder, runNumber, threads)
call(command_fu, shell=True)

outputFolder += "/run"+ runNumber
#now we have to do the cuts
ini = [outputFolder + "/" + f for f in os.listdir(outputFolder) if "streamA" in f and f.endswith(".ini")][0]
dats = sorted([outputFolder + "/"+ f for f in os.listdir(outputFolder) if "streamA" in f and f.endswith(".dat")])

call("cat {0} > {1}/run{2}.dat".format(ini, outputFolder, runNumber), shell=True)
for dat in dats:
    call("cat {0} >> {1}/run{2}.dat".format(dat, outputFolder, runNumber), shell=True)


#now the reconstruction
print "\n===================================== Reconstruction ==========================================\n"
call("cmsRun reco.py inputFiles=file:{} outputFile={}".format(
		outputFolder +"/run"+str(runNumber)+".dat", outputFolder +"/reco_RECO.root"), shell=True)

