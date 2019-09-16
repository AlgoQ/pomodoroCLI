from pomodoroCLI import CONSTS, alarmSound as als, paths as p
from pomodoroCLI.classes import JsonHandler as jh

from time import sleep
from datetime import datetime
import sys

class CycMan: # CycleManager
	def __init__(self, workCyc, relCyc, bigRelCyc):
		self.workCyc = workCyc
		self.relCyc = relCyc
		self.bigRelCyc = bigRelCyc
		self.cycCounter = 1
		self.statsHandler = self.getStatsHandler()
		self.currCycDate = "" # If you're working overnight
		self.currCycId = 0
		
	def cycle(self):
		if self.cycCounter == 1:
			self.workCycle()
		else:
			als.doubleAlarmSound()
			enter = input("Press enter to start a new cycle...")
			if enter == "":
				print("\n")
				self.workCycle()

		if self.cycCounter < 4:
			self.relaxCycle()
		else:
			self.bigRelaxCycle()
	
	def restart(self):
		print("Congratulations you've completed a hole set!")
		enter = input("Press enter to start new set (4 cycles)")
		if enter == "":
			self.workCycle()

	def workCycle(self):
		als.singleAlarmSound()
		self.addStat(self.statsHandler)

		print("A work cycle of {} minute(s) is started, let's work!".format(self.workCyc))
		
		try:
			sleep(self.workCyc * 60)
			self.relaxCycle()
		except KeyboardInterrupt:
			date = datetime.now()
			stop = date.strftime("%H:%M")

			stats = self.getStats(self.statsHandler)
			start = stats[self.currCycDate][str(self.currCycId)]["start"]

			subTime = self.subTimes(start, stop)
			subTimes = subTime.split(":")
			work = int(subTimes[0]) * 60 + int(subTimes[1])
			if work > 0:
				self.updClosedStat(self.statsHandler, stop, work, 0)
			else:
				self.remStat(self.statsHandler)
			
			stopInp = input("\nDo you want to shutdown pomodoroCLI? Or do you want to update the duration of the cycles? (y/n/u): ")
			if stopInp == "y":
				print("\npomodoroCLI is shutting down...")
				sys.exit()
			elif stopInp == "u":
				self.workCyc = int(input("New duration for the work cycle: "))
				self.relCyc = int(input("New duration for the relax cycle: "))
				self.bigRelCyc = int(input("New duration for the big relax cycle: "))
				self.cycle()
			else:
				self.cycle()
			

	def relaxCycle(self):
		als.doubleAlarmSound()
		self.cycCounter += 1

		print("Good job! Enjoy your relax cycle of {} minute(s)".format(self.relCyc))
		try:
			sleep(self.relCyc * 60)
			self.updStat(self.statsHandler)
			self.cycle()
		except KeyboardInterrupt:
			date = datetime.now()
			stop = date.strftime("%H:%M")

			stats = self.getStats(self.statsHandler)
			start = stats[self.currCycDate][str(self.currCycId)]["start"]

			subTime = self.subTimes(start, stop)
			subTimes = subTime.split(":")
			relax = int(subTimes[0]) * 60 + int(subTimes[1]) - self.workCyc

			self.updClosedStat(self.statsHandler, stop, self.workCyc, relax)

			
			stopInp = input("\nDo you want to shutdown pomodoroCLI? Or do you want to update the duration of the cycles? (y/n/u): ")
			if stopInp == "y":
				print("\npomodoroCLI is shutting down...")
				sys.exit()
			elif stopInp == "u":
				self.workCyc = int(input("New duration for the work cycle: "))
				self.relCyc = int(input("New duration for the relax cycle: "))
				self.bigRelCyc = int(input("New duration for the big relax cycle: "))
				self.cycle()
			else:
				self.cycle()
	
	def bigRelaxCycle(self):
		als.doubleAlarmSound()
		self.cycCounter = 1

		print("Enjoy your big relax cycle of {} minute(s).".format(self.bigRelCyc))
		try:
			sleep(self.bigRelCyc * 60)
			self.updStat(self.statsHandler)
			self.cycle()
		except KeyboardInterrupt:
			date = datetime.now()
			stop = date.strftime("%H:%M")

			stats = self.getStats(self.statsHandler)
			start = stats[self.currCycDate][str(self.currCycId)]["start"]

			subTime = self.subTimes(start, stop)
			subTimes = subTime.split(":")
			relax = subTimes[0] * 60 + subTimes[1] - self.workCyc

			self.updClosedStat(self.statsHandler, stop, self.workCyc, relax)
			
			stopInp = input("\nDo you want to shutdown pomodoroCLI? Or do you want to update the duration of the cycles? (y/n/u): ")
			if stopInp == "y":
				print("\npomodoroCLI is shutting down...")
				sys.exit()
			elif stopInp == "u":
				self.workCyc = int(input("New duration for the work cycle: "))
				self.relCyc = int(input("New duration for the relax cycle: "))
				self.bigRelCyc = int(input("New duration for the big relax cycle: "))
				self.cycle()
			else:
				self.cycle()
	
	# Additional funcs
	def subTimes(self, start, stop):
		formatTime = '%H:%M'

		subTime = str(datetime.strptime(stop, formatTime) - datetime.strptime(start, formatTime))
		return subTime
		
	# -> Stats
	def getStatsHandler(self):
		statsPath = p.getStatsPath()
		statsHandler = jh.JsonHandler(statsPath)

		return statsHandler
	
	def getStats(self, statsHandler):
		stats = statsHandler.jsonReader()

		return stats

	def addStat(self, statsHandler):
		stats = self.getStats(statsHandler)
		date = datetime.now()
		today = date.strftime("%d/%m/%Y")

		start = date.strftime("%H:%M")
		if today not in stats.keys():
			stats[today] = {}
		if len(stats[today]) != 0:
			for key, value in stats[today].items():
				lastKey = key
			currCycId = int(lastKey) + 1
		else:
			currCycId = 1
		
		stats[today][currCycId] = {
			"start": start,   		# When you start a new cycle
			"stop": "",           	# When the relax cycle is over
			"work": self.workCyc,	# Minutes of a work cycle
			"relax": self.relCyc,	# Minutes of a relax cycle
			"complete": 0			# Is the hole cycle been completed? (o -> no / 1 -> yes)
		}
		statsHandler.overwriteJson(stats)
		
		self.currCycDate = today
		self.currCycId = currCycId
		
	def updStat(self, statsHandler):
		stats = self.getStats(statsHandler)
		date = datetime.now()
		stop = date.strftime("%H:%M")
		stats[self.currCycDate][str(self.currCycId)]["stop"] = stop
		stats[self.currCycDate][str(self.currCycId)]["complete"] = 1

		statsHandler.overwriteJson(stats)
	
	def updClosedStat(self, statsHandler, stop, work, relax):
		stats = self.getStats(statsHandler)
		date = datetime.now()
		stop = date.strftime("%H:%M")
		stats[self.currCycDate][str(self.currCycId)]["stop"] = stop
		stats[self.currCycDate][str(self.currCycId)]["work"] = work
		stats[self.currCycDate][str(self.currCycId)]["relax"] = relax

		statsHandler.overwriteJson(stats)
	
	def remStat(self, statsHandler):
		stats = self.getStats(statsHandler)
		
		stats[self.currCycDate].pop(str(self.currCycId))

		statsHandler.overwriteJson(stats)