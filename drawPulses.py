import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('reco_RECO.root')

mg = ROOT.TMultiGraph()

handle  = Handle ('EBDigiCollection')
label = ("ecalDigis","ebDigis")

       
max_events = 100
num_events = 0

for event in events:
  #print "event = ", event
  num_events += 1 
  
  if num_events < max_events :
  
    event.getByLabel (label, handle)
    ebdigi = handle.product()  

    gr = ROOT.TGraph()
    gr.Clear()
    for isample in range (10) :    
      #print " [" , isample, "] = ", ((ebdigi[0][isample]) & 0xFFF)
      gr.SetPoint(isample,isample*25,  ((ebdigi[0][isample]) & 0xFFF) );
  
    if num_events%5 == 1 :
     color = ROOT.kRed -10 + num_events%15
    elif num_events%5 == 2 :
     color = ROOT.kCyan -10 + num_events%15
    elif num_events%5 == 3 :
     color = ROOT.kMagenta -10 + num_events%15
    elif num_events%5 == 4 :
     color = ROOT.kGreen -10 + num_events%15
    else :
     color = ROOT.kAzure -10 + num_events%15


    gr.SetMarkerColor()
    gr.SetLineColor  (ROOT.kRed -10 + num_events%20)
    
    gr.SetMarkerSize(1)
    gr.SetMarkerStyle(20 + num_events%14)

    mg.Add(gr)
  
  
print " now draw "   
print " analyzed = ", num_events
 
cc = ROOT.TCanvas("cc","pulses from local run", 800, 600) 
mg.Draw("apl")
mg.GetXaxis().SetTitle("time [ns]")
mg.GetYaxis().SetTitle("ADC")

mg.SaveAs("mg.root")
#mg.Draw("a fb l3d")
 
     
   
