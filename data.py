from datetime import datetime, timedelta 


now_data=datetime.now()

create_data=now_data-timedelta(days=5)

print("TODAY: ",now_data.strftime("%Y-%m-%d"))
print("MINUS 5 DAY:",create_data.strftime("%Y-%m-%d"))
print(end="\n")




today=datetime.now()

yesterday=today-timedelta(days=1)
tomorrow=today+timedelta(days=1)

print("TODAY: ",today.strftime("%Y-%m-%d"))
print("YESTERDAY: ",yesterday.strftime("%Y-%m-%d"))
print("TOMORROW: ",tomorrow.strftime("%Y-%m-%d"))





def drop_microseconds(dt):

    dt_without_microseconds = dt.replace(microsecond=0)
    return dt_without_microseconds

if __name__ == "__main__":
    now = datetime.now()

    datetime_without_microseconds = drop_microseconds(now)

    print("Original datetime:", now)
    print("Datetime without microseconds:", datetime_without_microseconds)





def difference(date1,date2):
    difference=date2-date1

    difference_seconds=difference.total_seconds()
    return difference_seconds

if __name__ == "__main__":

    date1_in=input("DATE 1 (YYYY-MM-DD HH:MM:SS): ")
    date2_in=input("DATE 2 (YYYY-MM-DD HH:MM:SS): ")

    date1=datetime.strptime(date1_in, "%Y-%m-%d %H:%M:%S" )
    date2=datetime.strptime(date2_in, "%Y-%m-%d %H:%M:%S" )

    difference_sec=difference(date1,date2)

    print(int(abs(difference_sec)))
    
from datetime import datetime

date_string = "2024-02-07 15:30:00"
date_object = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print(date_object)