from datetime import datetime
# Update 18 April 2020
print('-------------------------------------')
print
print("Enter your Input")
ExposureTimeSec =  input("Enter exposure time in sec: ")     # Seconds
ExposureTime = int(ExposureTimeSec) / 60
StartTime = input("Enter start Time: ")
EndTime =  input("Enter End   Time: ")

# Personal Settings
FocusTime = 4         # Minuten
StartedGuiding = 1    # Minuten
TimeforFlip = 6       # Minuten

ExposuretimeMin = ExposureTime / 60

#fmt = '%d-%m-%Y %H:%M'
fmt = '%d %H:%M'
tstamp1 = datetime.strptime(StartTime, fmt)
tstamp2 = datetime.strptime(EndTime, fmt)

if tstamp1 > tstamp2:
    td = tstamp1 - tstamp2
else:
    td = tstamp2 - tstamp1

td_mins      = int(round(td.total_seconds() / 60))
td_exposures = int(round(td_mins / ExposureTime))
NumberFocus  =  td_exposures / 12
print
print("Amount of Focus Actions        = " + str(round(NumberFocus)))
td_hours     = int((td_mins / 60))
td_other     = (NumberFocus*FocusTime) + StartedGuiding + TimeforFlip
td_mins      = td_mins - td_other
td_exposures = int(round(td_mins / ExposureTime))
print('The difference is approx       = %s minutes' % round(td_mins))
#print('The difference is approx       = %s hours' % td_hours)
print('Expected ' + str(ExposureTimeSec)+' Sec' + ' Exposures     = ' + str(td_exposures))
print
print('-------------------------------------')
