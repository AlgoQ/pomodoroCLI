from os.path import expanduser

def getHomePath():
    return expanduser("~")

def getJsonsPath():
    jsonPath = getHomePath() + "/pomodoroCLI/jsons"
    return jsonPath

def getStatsPath():
    statsPath = getHomePath() + "/pomodoroCLI/jsons/stats.json"
    return statsPath
