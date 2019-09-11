import pandas as pd
import json, datetime

from pomodoroCLI import paths as p
from pomodoroCLI.classes import JsonHandler as jh

class StatMan:
	def __init__(self, timePer):
		self.timePer = timePer
		self.statHandler = self.getStatsHandler()
	
	def periodHandler(self): 
		# TODO: Add func to view stats of a specific date
		stats = self.getStats(self.statHandler)
		if self.timePer in ["t", "tod", "today"]:
			self.statsDay(stats, self.calcDate(0))
		elif self.timePer in ["y", "yes", "yesterday"]:
			self.statsDay(stats, self.calcDate(1))
		elif self.timePer in ["w", "wee", "week"]:
			self.statsWee(stats)
		elif self.timePer in ["m", "mon", "month"]:
			self.statsMon(stats)
		elif self.timePer in ["a", "all", "all-time"]:
			self.statsAll(stats)
	
	def getOverview(self, stats, date):
		overview = "Overview of {}\n----------------------\n\n".format(date) # TODO: Add day -> For example "Monday 10/09/2019"
		times = [0,0,0] # 0 -> work, 1 -> relax, 2 -> total
		timesStr = ["","",""]
		uncomCycs = 0 # Uncompleted cycles
		# TODO: If "timePer" > week: add avg, avg on a weekday, avg by day and the median
		for cycle in stats[date]:
			for key, value in stats[date][cycle].items():
				if key == "work":
					times[0] += value
					times[2] += value
				elif key == "relax":
					times[1] += value
					times[2] += value
				
				elif key == "complete":
					if value == 0:
						uncomCycs += 1

		for i in range(3):
			if len(str(times[i] % 60)) > 1:
				timesStr[i] = str(int(times[i] / 60)) + "h" + str(times[i] % 60)
			else:
				timesStr[i] = str(int(times[i] / 60)) + "h0" + str(times[i] % 60)

		overview += "Total time: {}\n".format(timesStr[2])
		overview += "Work time:  {}\n".format(timesStr[0])
		overview += "Relax time: {}\n\n".format(timesStr[1])

		overview += "Total cycles:       {}\n".format(len(stats[date]))
		overview += "Completed cycles:   {}\n".format(len(stats[date])- uncomCycs)
		overview += "Uncompleted cycles: {}\n".format(uncomCycs)

		return overview
	
	def getDataFrame(self, stats, date):
		df = pd.DataFrame(stats[date]) # Load data frame out of stats of given date
		df = df.T # Switch columns and index 
		df = df.drop(columns=["complete", "stop"]) # Remove the columns "complete" and "stop"
		df = df.rename(columns={"relax": "Relax", "work": "Work", "start" : "Start"}) # Rename the columns
		df = df.set_index("Start") # Set "start" as index
		df = df.rename_axis(None)
		swapList = ["Work", "Relax"]
		df = df.reindex(columns=swapList) # Change the order of the columns
		df = df.assign(Total=lambda x: x.Work + x.Relax) # Add "Total" column

		return df

	def statsDay(self, stats, day):
		try:
			overview = self.getOverview(stats, day)
			print(overview)

			df = self.getDataFrame(stats, day)
			print(df)
		except KeyError:
			print("Overview of {}\n----------------------\n\nNo data to show...".format(day))
			# TODO: Add day -> For example "Monday 10/09/2019"
		
		

	def statsWee(self, stats):
		pass

	def statsMon(self, stats):
		pass

	def statsAll(self, stats):
		pass

	# Additional funcs
	def dateToday(self):
		today = datetime.datetime.now()
		today = today.strftime("%d/%m/%Y")

		return today
	
	def calcDate(self, days):
		calcDate = datetime.datetime.today() - datetime.timedelta(days=days)
		calcDate = calcDate.strftime("%d/%m/%Y")

		return calcDate
	
	# -> Stats

	def getStatsHandler(self):
		statsPath = p.getStatsPath()
		statsHandler = jh.JsonHandler(statsPath)

		return statsHandler
	
	def getStats(self, statsHandler):
		stats = statsHandler.jsonReader()

		return stats
		