import numpy as np
arr=np.array(np.datetime64('2021-06-15'))
print(arr)

#2.
arr=np.array(np.datetime64('2021-06','D'))
print(arr)


#get today, yesterday,tomorrow
yesterday = np.datetime64('today', 'D') - np.timedelta64(1, 'D')
print("Yestraday: ",yesterday)
today     = np.datetime64('today', 'D')
print("Today: ",today)
tomorrow  = np.datetime64('today', 'D') + np.timedelta64(1, 'D')
print("Tomorrow: ",tomorrow)

#count number of days
print("Number of days, May, 2021: ")
print(np.datetime64('2021-06-01') - np.datetime64('2021-05-01'))
print("Number of days, June, 2020: ")
print(np.datetime64('2020-07-01') - np.datetime64('2020-06-01'))
print("Number of days, July, 2019: ")
print(np.datetime64('2019-08-01') - np.datetime64('2019-07-01'))