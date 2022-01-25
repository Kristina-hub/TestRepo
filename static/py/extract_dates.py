# --------------------------------------- #
#       Authors: Kristina Kacmarova       #
#                Miranda Postma       	  #
#                Ridwan Bari              #
#                Winston Herold           #
#       Python Version: 3.7.4             #
#       Created on: 2022-01-18            #
# --------------------------------------- #


from datetime import datetime
from dateutil.parser import parse
from dateparser.search import search_dates
from sutime import SUTime
import json
import re

class ExtractDates():

	def dates_func(text):
		print("Enter: deadlines_func.py")
		
		# everything except 10/6 and words: Assignment
		message = ""
		sutime = SUTime(mark_time_ranges=True, include_range=True)
		json_dump = json.dumps(sutime.parse(text), sort_keys=True, indent=4)
		json_loads = json.loads(json_dump)
		for obj in json_loads:
			if re.search(r'\d{4}-\d{2}-\d{2}', obj["value"]):
				format_str = datetime.strptime(obj["value"], '%Y-%m-%d').strftime('%b %d, %Y')
				message += format_str
				message += "<br/>"
		
		print()
		print(message)
		print()
		print("Exit: deadlines_func.py")
		return message

		
		

		
		