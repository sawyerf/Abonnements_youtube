import time

def lcl_time():
	tps = time.localtime()
	tm_year, tm_mon, tm_mday = tps.tm_year, tps.tm_mon, tps.tm_mday
	if tm_mon == 1:
		tm_mon = 12
		tm_year -= 1
	else:
		tm_mon -= 1
	tm_mday = str(tm_mday)
	tm_mon = str(tm_mon)
	tm_year = str(tm_year)
	if len(tm_mday) == 1:
		tm_mday = '0' + tm_mday
	elif len(tm_mon) == 1:
		tm_mon = '0' + tm_mon
	return int(tm_year + tm_mon + tm_mday + '000000')
	
