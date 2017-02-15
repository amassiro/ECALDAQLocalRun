import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('reco_RECO.root')

mg = ROOT.TMultiGraph()

handle  = Handle ('EBDigiCollection')
label = ("ecalDigis","ebDigis")

       
max_events = 10000
num_events = 0

noise = ROOT.TH1F("noise", "noise", 100, 0, 4)
pedestal = ROOT.TH1F("pedestal", "pedestal", 1000, 0, 1000)

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
     color = ROOT.kRed -9 + num_events%13
    elif num_events%5 == 2 :
     color = ROOT.kCyan -9 + num_events%13
    elif num_events%5 == 3 :
     color = ROOT.kMagenta -9 + num_events%13
    elif num_events%5 == 4 :
     color = ROOT.kGreen -9 + num_events%13
    else :
     color = ROOT.kAzure -9 + num_events%13


    gr.SetMarkerColor(color)
    gr.SetLineColor  (color)
    
    gr.SetMarkerSize(1)
    gr.SetMarkerStyle(20 + num_events%14)

    noise.Fill(gr.GetRMS(2))
    pedestal.Fill(gr.GetMean(2))
    mg.Add(gr)
  
  
print " now draw "   
print " analyzed = ", num_events
 
cc = ROOT.TCanvas("cc","pulses from local run", 800, 600) 
mg.Draw("apl")
mg.GetXaxis().SetTitle("time [ns]")
mg.GetYaxis().SetTitle("ADC count")

mg.SaveAs("mg.root") 
  
noise.SetLineColor(ROOT.kRed)
noise.GetXaxis().SetTitle("ADC count")
noise.SaveAs("noise.root")
   
  
pedestal.SetLineColor(ROOT.kRed)
pedestal.GetXaxis().SetTitle("ADC count")
pedestal.SaveAs("pedestal.root")
   
