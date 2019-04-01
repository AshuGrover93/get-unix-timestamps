
import datetime
import calendar
import math


#pass date timestamp of month whose previous x months timestamps are required
def getdates(data_ts, agg_type, no_times):
            
    data_ts = data_ts/1000  #data_ts in milliseconds
    
    datePassed = datetime.datetime.fromtimestamp(data_ts)
    datePassed = datePassed.replace(minute=00, hour=00, second=00)
        
    start_dt = 0
    end_dt = 0
    
    dates_list = []
    
    for i in range(0, no_times):
            
        year_got = datePassed.year
        
        dates_json = {}
            
        if(agg_type=='month'):
            
            if datePassed.day < 30:
                datePassed -= datetime.timedelta(30)
            else:
                datePassed -= datetime.timedelta(31)
                        
            prev_month_first_date = datePassed.replace(day=1)
            start_dt = (prev_month_first_date - datetime.datetime(1970,1,1)).total_seconds()*1000
            
            current_month = datePassed.month          
    
            if(current_month in [1,3,5,7,8,10,12]):
                prev_month_last_date = datePassed.replace(day=31)
            
            elif(current_month in [4,6,9,11]):
                prev_month_last_date = datePassed.replace(day=30)
            
            else:
                if(calendar.isleap(year_got)):
                    prev_month_last_date = datePassed.replace(day=29)
                else:
                    prev_month_last_date = datePassed.replace(day=28)
            

            end_dt = ((prev_month_last_date - datetime.datetime(1970,1,1)).total_seconds()*1000)+(86400*1000 - 1)
            
            string1 = "start_dt"+str(no_times - i)
            string2 = "end_dt"+str(no_times - i)
            
            dates_json[string1] = int(start_dt)
            dates_json[string2] = int(end_dt)
            
            dates_list.append(dates_json)
            
            datePassed = datetime.datetime.fromtimestamp(start_dt/1000)
            datePassed = datePassed.replace(minute=00, hour=00, second=00)
            
            
        elif(agg_type in ['quarter', 'quarter_netbase']):
            
            firstdate = datePassed
            lastdate = datePassed            
            
            current_month = firstdate.month
            quarter=math.ceil(current_month/3.)

          
            if(i==0):
                if(quarter==1):
                    firstdate = datetime.datetime(year_got-1, 10, 1)
                    lastdate  = datetime.datetime(year_got-1, 12, 31)
                    
                elif(quarter==2):
                    firstdate = datetime.datetime(year_got, 1, 1)
                    lastdate  = datetime.datetime(year_got, 3, 31)                                
                
                elif(quarter==3):
                    firstdate = datetime.datetime(year_got, 4, 1)
                    lastdate  = datetime.datetime(year_got, 6, 30)         
                    
                elif(quarter==4):
                    firstdate = datetime.datetime(year_got, 7, 1)
                    lastdate  = datetime.datetime(year_got, 9, 30)
            
            else:
                if(quarter==1):
                    firstdate = datetime.datetime(year_got, 1, 1)
                    lastdate  = datetime.datetime(year_got, 3, 31)              
                
                elif(quarter==2):
                    firstdate = datetime.datetime(year_got, 4, 1)
                    lastdate  = datetime.datetime(year_got, 6, 30)                                
                
                elif(quarter==3):
                    firstdate = datetime.datetime(year_got, 7, 1)
                    lastdate  = datetime.datetime(year_got, 9, 30)         
                    
                else:
                    firstdate = datetime.datetime(year_got, 10, 1)
                    lastdate  = datetime.datetime(year_got, 12, 31)
                               
                
            start_dt = (firstdate - datetime.datetime(1970,1,1)).total_seconds()*1000
            end_dt = ((lastdate - datetime.datetime(1970,1,1)).total_seconds()*1000)+(86400*1000 - 1)            
            
            string1 = "start_dt"+str(no_times - i)
            string2 = "end_dt"+str(no_times - i)
            
            dates_json[string1] = int(start_dt)
            dates_json[string2] = int(end_dt)
            
            dates_list.append(dates_json)
            
            datePassed = datetime.datetime.fromtimestamp(start_dt/1000)
            datePassed -= datetime.timedelta(15)
            datePassed = datePassed.replace(minute=00, hour=00, second=00)
            
                                    
        elif(agg_type=='year'):            
            
            firstdate = datetime.datetime(year_got-1, 1, 1)
            lastdate  = datetime.datetime(year_got-1, 12, 31)
            
            start_dt = (firstdate - datetime.datetime(1970,1,1)).total_seconds()*1000
            end_dt = ((lastdate - datetime.datetime(1970,1,1)).total_seconds()*1000)+(86400*1000 - 1) 
                     
            
            string1 = "start_dt"+str(no_times - i)
            string2 = "end_dt"+str(no_times - i)
            
            dates_json[string1] = int(start_dt)
            dates_json[string2] = int(end_dt)
            
            dates_list.append(dates_json)
            
            datePassed = datetime.datetime.fromtimestamp(start_dt/1000)            
            
                                            
    return dates_list


print(getdates(1547548921000, 'month', 7))

print(getdates(1560595321000, 'quarter', 2))

print(getdates(1540439326000, 'year', 3))
