import datetime

timeList = ['00:05:00', '00:05:15', '00:50:50',"09:25:45"]

def sum_timestamp(timestamplist,timeDeltaObj=False):
    mysum = datetime.timedelta()
    for i in timeList:
        (h, m, s) = i.split(':')
        d = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        mysum += d
    if timeDeltaObj:
        return mysum
    return str(mysum)