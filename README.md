# ECALDAQLocalRun


Where:

    /afs/cern.ch/user/a/amassiro/work/ECAL/DAQ/CMSSW_8_0_17/src/ECALDAQLocalRun
    
How:

    cmsrel CMSSW_8_0_17
    cd CMSSW_8_0_17/src
    
    cmsenv
    git cms-init
    
    git cms-addpkg EventFilter/Utilities/
    
    git clone git@github.com:amassiro/ECALDAQLocalRun.git

    
    
need to put:

    eventRunNumber_ = runNumber_;

instead of:

    eventRunNumber_=event_->run();

in the file:

    FedRawDataInputSource.cc

    
    
    
Example:

    cmsRun testRawReader.py

    cmsRun reco.py  inputFiles=file:output/run100000/run100000_ls0001_streamA_pid19674.dat
    

