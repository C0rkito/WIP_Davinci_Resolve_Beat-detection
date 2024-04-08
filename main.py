#!/usr/bin/env python
from math import ceil

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
media_pool = project.GetMediaPool()
timeline = project.GetCurrentTimeline()
root_folder = media_pool.GetRootFolder()

fps = project.GetSetting("timelineFrameRate")

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





def GetMusicNameFromPath(music_path):
    music_name = ""
    for i in range(len(music_path)-1,0,-1):
        if (music_path[i] == '\\'):
            break
        music_name = music_path[i] + music_name 
    return music_name

def findMusic(music_name, folder=media_pool.GetRootFolder()):
    for clip in folder.GetClipList():
        if clip.GetName() == music_name:
            print("Process on "+clip.GetName()+" in "+folder.GetName())
            return clip
    
    for sub_folder in folder.GetSubFolderList():
        clip = findMusic(music_name, sub_folder)
        if clip:
            return clip 
    return None

with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "r") as file:
    lines = file.readlines()
    
music_name = GetMusicNameFromPath(path)
music_in_davinci = findMusic(music_name)
music_in_davinci.DeleteMarkersByColor("Green")

i = 0
for line in lines:
    i+=1
    if i == 16:
        break
    line = line.strip().split('.')
    line = line[0] +'.'+ line[1][0] + line[1][1] + line[1][2]+ line[1][3]+ line[1][4]
    line = float(''.join(line))
    line = line*fps
    print("beat on second : " + str(int(round(line))))
    music_in_davinci.AddMarker(int(round(line)), "Green", "Marker Name", "Custom Notes", 1)
  
print("Finish ! ")

