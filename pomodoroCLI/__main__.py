import sys
from .ArgParser import ArgParse
from .CycMan import CycMan

def main():
    # parser = argparse.ArgumentParser()

    args = sys.argv[1:]
    parser = ArgParse(args)

    returnDict = parser.eventHandler()
    
    if returnDict["event"] == "r":
        timer = CycMan(returnDict["workCyc"], returnDict["relCyc"], returnDict["bigRelCyc"])
        timer.cycle()

    
    
if __name__ == '__main__':
    main()