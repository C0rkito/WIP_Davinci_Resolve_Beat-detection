#!/usr/bin/env python

resolve = app.GetResolve()

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
