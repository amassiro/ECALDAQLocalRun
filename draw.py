import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('reco_RECO.root')
#handle  = Handle ('edm::SortedCollection<EcalUncalibratedRecHit,edm::StrictWeakOrdering<EcalUncalibratedRecHit> >')
#label = ("ecalMultiFitUncalibRecHit","EcalUncalibRecHitsEB")

#for event in events:
     #print " event ... "
     #event.getByLabel (label, handle)
     #ebrechits = handle.product()
     #for rh in ebrechits:
          #print rh.pedestal()
          #print rh.amplitude(),rh.pedestal(),rh.flags(),rh.outOfTimeAmplitude(4),rh.outOfTimeAmplitude(5),rh.outOfTimeAmplitude( 6)
          






#handle  = Handle ('edm::SortedCollection<EBdigi,edm::StrictWeakOrdering<EBdigi> >')
handle  = Handle ('EBDigiCollection')
label = ("ecalDigis","ebDigis")

print " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ "
print " ciao "

#for (int j=0; j<10; j++){ 
    #_pulse[j] = float(digi[j]&0xFFF);
    #_gain[j] = float((digi[j]>>12)&0x3);
    #_gainmask |= 1<<(int(_gain[j]));
    #_position[j] = j;
  #}



for event in events:
     print " event ... "
     event.getByLabel (label, handle)
     ebdigi = handle.product()
     print " ebdigi = ", ebdigi
     print " ebdigi.size() = ", ebdigi.size()
     
       #for (uint i=0; i<ebdigis->size(); i++) FillDigi((*ebdigis)[i],ebrechits,w_ebrechits);



     #print " ebdigi[0] = ", ebdigi
     #ebdigis
     
     #print float(ebdigi[0]&0xFFF)
     
   
