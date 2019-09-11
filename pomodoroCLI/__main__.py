import sys, os.path
from pomodoroCLI.classes import ArgParser, CycMan, StatMan
from pomodoroCLI import checkDir as cd, paths as p


def main():
	homePath = p.getHomePath()
	cd.checkDir(homePath)
	
	args = sys.argv[1:]
	parser = ArgParser.ArgParser(args)

	returnDict = parser.eventHandler()
	
	if returnDict["event"] == "r":
		cycMan = CycMan.CycMan(returnDict["workCyc"], returnDict["relCyc"], returnDict["bigRelCyc"])
		cycMan.cycle()
	elif returnDict["event"] == "st":
		statMan = StatMan.StatMan(returnDict["timePer"])
		statMan.periodHandler()

if __name__ == '__main__':
	main()