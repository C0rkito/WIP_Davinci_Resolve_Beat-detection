import subprocess
import os
from time import sleep


projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
media_pool = project.GetMediaPool()
media_storage = resolve.GetMediaStorage()
timeline = project.GetCurrentTimeline()
root_folder = media_pool.GetRootFolder()
fps = project.GetSetting("timelineFrameRate")


width,height = 800,400
posX,posY = 750,325
path = ""
run = False

def findMusic(music_name, folder=media_pool.GetRootFolder()):
    for clip in folder.GetClipList():
        if clip.GetName() == music_name:
            return clip
        
    for sub_folder in folder.GetSubFolderList():
        clip = findMusic(music_name, sub_folder)
        if clip:
            return clip 
    return 0


def GetMusicNameFromPath(music_path):
    music_name = ""
    for i in range(len(music_path)-1,0,-1):
        if (music_path[i] == '\\'):
            break
        music_name = music_path[i] + music_name 
    return music_name

def window(posX,posY,width,height):

    css_style = f"""
    color: rgb(205, 205, 245);
    font-family: Garamond;
    font-weight: bold;
    font-size: 16px;
    """
    error_style = f"""
    color: rgb(255, 0, 0);
    font-family: Garamond;
    font-size: 10px;

    """

    ui = fusion.UIManager
    dispatcher = bmd.UIDispatcher(ui)

    window = dispatcher.AddWindow({ 'ID': 'myWindow',  'WindowTitle': 'My Window','Events': {'Resize': False, 'Clicked': True, 'Close': True},'Geometry': [posX,posY,width,height]},
                               [ ui.Label({'ID' : 'PathText','Text': 'Path :','StyleSheet': css_style,'Geometry': [width/2,height/2,width/4,height/4]}),
                                 ui.Label({'ID' : 'Error','StyleSheet': error_style,'WordWrap': True ,'FixedSize': [width, height],'Geometry': [0,-height/3.,width/4,height/4]}),
                                 ui.Button({'ID' : 'Browse','Text':'Execute','Geometry': [width/3,height/1.4,width/4,height/4]}),
                                 ui.Button({'ID' : 'Delete','Text':'Delete','Geometry': [width/1.5,height/1.4,width/6,height/6]}),
                                 ui.LineEdit({'ID':'le_1','PlaceholderText':'Path of the file','Events': {'TextEdited': True},'Geometry': [width/7,height/2.5,width/1.5,height/5]})])

    win_itms = window.GetItems()
    

    def OnClose(ev):
        dispatcher.ExitLoop()
        window.Hide()
        
    
    def OnButtonClickedProcess(ev):
        if (os.path.exists(path) and path != ""):
            global run
            run = True
            dispatcher.ExitLoop()
        else:
            win_itms["Error"].SetText("unreachable path : "+ path)


    def OnButtonClickedDelete(ev):
        if (os.path.exists(path) and path != ""):
            track = findMusic(GetMusicNameFromPath(path))
            print(track.GetMarkerCustomData(48))
            track.DeleteMarkersByColor("Red")
            

            for i in range(1,timeline.GetTrackCount("audio")+1):
                music = timeline.GetItemListInTrack("audio",i)
                for elt in music:
                    if(elt.GetName() == GetMusicNameFromPath(path)):
                        elt.DeleteMarkersByColor("Red")
                
                
        


        
    def OnLineEditTextEdited(ev):
        global path
        path = os.path.normpath(ev["Text"])
        
    



    window.On.myWindow.Close = OnClose
    window.On['le_1'].TextEdited = OnLineEditTextEdited
    window.On['Browse'].Clicked = OnButtonClickedProcess
    window.On['Delete'].Clicked = OnButtonClickedDelete
    window.Show()
    dispatcher.RunLoop()
    dispatcher.ExitLoop()
    window.Hide()
    




#C:\Users\HUGO\Videos\4K Video Downloader\Sweetest Pie.mp3
window(posX,posY,width,height)


if (run):

    
    #C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Edit
    with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\path.txt","w") as file:
        file.write(path)



    music_name = GetMusicNameFromPath(path)

    music_in_davinci = findMusic(music_name)
    if (music_in_davinci == 0):
        music_in_davinci = media_pool.ImportMedia(os.path.normpath(path))

        

    music_in_davinci.DeleteMarkersByColor("Red")

    print("process on "+ str(music_in_davinci.GetName()))


    subprocess.run('C:\\Users\\HUGO\\AppData\\Local\\Programs\\Python\\Python310\\python.exe "C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\hello.py"')



    with open("C:\\Users\\HUGO\\AppData\\Roaming\\Blackmagic Design\\DaVinci Resolve\\Support\\Fusion\\Scripts\\Comp\\Beat_Script\\Davinci-Resolve-Beat-detection\\beats.txt", "r") as file:
        lines = file.readlines()
        


    beatNb = 0
    for line in lines:
        beatNb += 1

        
        line = line.strip().split('.')
        line = line[0] +'.'+ line[1]
        line = float(''.join(line))
        line = line*fps
        music_in_davinci.AddMarker(int(round(line)), "Red", "Beat N° "+str(beatNb),"Generated by Beat Detector Script for more info https://github.com/C0rkito/Davinci-Resolve-Beat-detection/tree/main",1)
    print("Finish ! ")

