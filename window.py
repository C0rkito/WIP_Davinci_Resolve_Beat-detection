#!/usr/bin/env python
import subprocess
import os





projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
media_pool = project.GetMediaPool()
timeline = project.GetCurrentTimeline()
root_folder = media_pool.GetRootFolder()

fps = project.GetSetting("timelineFrameRate")

posX,posY = 750,325
width,height = 450,250
path = ""


def window(posX,posY,width,height):
    ui = fusion.UIManager
    dispatcher = bmd.UIDispatcher(ui)

    win = dispatcher.AddWindow({ 'ID': 'myWindow',  'WindowTitle': 'My Window','Geometry': [posX,posY,width,height]},
                               [ ui.Label({ 'Text': 'Path :',}),
                                 ui.Button({'ID' : 'Browse','Text':'Execute','Geometry': [width/3,height/1.4,width/4,height/4]}),
                                 ui.LineEdit({'ID':'le_1','PlaceholderText':'Path of the file','Events': {'TextEdited': True},'Geometry': [width/7,height/2.5,width/1.5,height/5]})])



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
    dispatcher.ExitLoop()
    win.Hide()

    

window(posX,posY,width,height)





 

#C:\\Users\\HUGO\\Videos\\4K Video Downloader\\SLCHLD  -  wednesday girl (prod. by MXXWLL).mp3
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






with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\path.txt","w") as file:
    file.write(path)
    
music_name = GetMusicNameFromPath(path)
music_in_davinci = findMusic(music_name)
music_in_davinci.DeleteMarkersByColor("Red")



subprocess.run('C:\\Users\\HUGO\\AppData\\Local\\Programs\\Python\\Python310\\python.exe "C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\hello.py"')



with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "r") as file:
    lines = file.readlines()
print("beat on frame : ")

beatNb = 0
for line in lines:
    beatNb+=1
    line = line.strip().split('.')
    line = line[0] +'.'+ line[1]
    line = float(''.join(line))
    line = line*fps
    music_in_davinci.AddMarker(int(round(line)), "Red", "Beat N° "+str(beatNb),1)
  
print("Finish ! ")
