
import FWCore.ParameterSet.Config as cms


from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')
options.parseArguments()


process = cms.Process("ECALDQM")


process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '80X_dataRun2_Prompt_v12', '')



process.load("EventFilter.EcalRawToDigi.EcalUnpackerMapping_cfi")
process.load("EventFilter.EcalRawToDigi.EcalUnpackerData_cfi")

process.load("Geometry.EcalMapping.EcalMapping_cfi")

process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")

process.source = cms.Source("NewEventStreamFileReader",
     fileNames = cms.untracked.vstring(options.inputFiles)
     )

process.ecalDataSequence = cms.Sequence(process.ecalEBunpacker)

process.p = cms.Path(process.ecalDataSequence)

#process.ecalEBunpacker.silentMode =  True 
process.ecalEBunpacker.silentMode = False 
