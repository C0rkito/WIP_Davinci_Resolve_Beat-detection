#!/usr/bin/env python

posX,posY = 0,0
width,height = 450,250
path = ""


def window(posX,posY,width,height):
    ui = fusion.UIManager
    dispatcher = bmd.UIDispatcher(ui)

    win = dispatcher.AddWindow({ 'ID': 'myWindow','Geometry': [posX,posY,width,height]},
                               [ ui.Label({ 'Text': 'Hello World!' }),
                                 ui.Button({'ID' : 'Browse','Text':'Browse','Geometry': [width/2,height/2,width/5,height/5]}),
                                 ui.LineEdit({'ID':'le_1','PlaceholderText':'Name of the file','Events': {'TextEdited': True}})])

    
    def OnClose(ev):
            dispatcher.ExitLoop()
            win.Hide()
            
    
    def OnButtonClicked(ev):
        global path
        print(path)
        dispatcher.ExitLoop()
        win.Hide()

    def OnLineEditTextEdited(ev):
        global path
        path = ev["Text"]



    win.On.myWindow.Close = OnClose
    win.On['le_1'].TextEdited = OnLineEditTextEdited
    win.On['Browse'].Clicked = OnButtonClicked
    win.Show()
    dispatcher.RunLoop()
    
    


window(posX,posY,width,height)



projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
storage = resolve.GetMediaStorage()  
media_pool = project.GetMediaPool()
timeline = project.GetCurrentTimeline()

root_folder = media_pool.GetRootFolder()
clip_list = root_folder.GetClipList()

print(clip_list[5].AddMarker(10, "Green", "Marker Name", "Custom Notes", 1))
#for i in range(100):
   #if i%2 == 0:
      
     #timeline.GetItemListInTrack("audio", 1)[0].AddMarker(i*10, "Green", "Marker Name", "Custom Notes", 1)
