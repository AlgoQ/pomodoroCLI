import os

def checkDir(homePath):
    '''
    If the directory 'pomodoroCLI' doesn't exists, create the folder with the subdirectory 'jsons' 
    with in there the file 'stats.json'
    '''

    pomoDir = homePath + "/pomodoroCLI"
    # TODO: Change pathName
    jsonDir = pomoDir + "/jsons"

    try: # If the stats file already exist (probably if you're reinstalled pomodoro)
        open(jsonDir + "/stats.json", "r")

    except: # If the stats file doesn't already exist (probably if it's the first time you install pomodoro)
        
        os.mkdir(pomoDir)
        os.mkdir(jsonDir)

        os.chdir(jsonDir)

        f = open("stats.json", "w+")

        f.write("{}")
        f.close()