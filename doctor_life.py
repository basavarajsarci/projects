import datetime


class Day:

    def __init__(self):
        pass

    weekday_schedule = {
        'night sleeping': '00:00-6:00',
        'getting fresh at the morning': '6:00-6:30',
        'doing exercise': '6:30-8:00',
        'having breakfast': '8:00-9:00',
        'travelling from home to office': '9:00-10:00',
        'working in the first half': '10:00-13:00',
        'having lunch': '13:00-14:00',
        'working at the second half': '14:00-18:00',
        'travelling from office to home': '18:00-19:00',
        'having relax': '19:00-20:00',
        'television': '20:00-21:00',
        'having dinner': '21:00-22:00'
    }

    weekend_schedule = {
        'night sleeping': '00:00-8:00',
        'getting fresh at the morning': '8:00-8:30',
        'doing exercise': '8:30-9:00',
        'having breakfast': '9:00-9:30',
        'travelling from home to office': '9:30-10:00',
        'working in the first half': '10:00-13:00',
        'having lunch': '13:00-14:00',
        'working at the second half': '14:00-18:00',
        'travelling from office to home': '18:00-19:00',
        'having relax': '19:00-20:00',
        'television': '20:00-21:00',
        'having dinner': '21:00-22:00'
    }

    present = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def checkday_fun(time, weekday, weekend, routine_fun):
        # weekday = present.today().weekday()
        # Return the day of the week as an integer, where Monday is 0 and Sunday is 6
        time = datetime.datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S")
        print(time.weekday())
        if time.weekday() == 6:
            print("Sunday")
            routine_fun(weekend, time)
        elif time.weekday() == 5:
            print("Saturday")
            routine_fun(weekend, time)
        else:
            print("Weekday")
            print(time.weekday(), time)
            routine_fun(weekday, time)

    def routine_fun(routine_time, time):
        time = datetime.datetime.strptime(str(time), "%Y-%m-%d %H:%M:%S")
        for task, timeslot in routine_time.items():

            date_start = time.date()
            hour_start = routine_time[task].split('-')[0].split(':')[0]
            min_start = routine_time[task].split('-')[0].split(':')[1]
            sec_start = '00'

            date_end = time.date()
            hour_end = routine_time[task].split('-')[1].split(':')[0]
            min_end = routine_time[task].split('-')[1].split(':')[1]
            sec_end = '00'

            start_time = str(date_start) + ' ' + str(hour_start) + ':' + str(min_start) + ':' + str(sec_start)
            start_time = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")

            end_time = str(date_end) + ' ' + str(hour_end) + ':' + str(min_end) + ':' + str(sec_end)
            end_time = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
            # print(start_time, end_time)

            if time >= start_time and time <= end_time:
                print("Task %s" % task)

    # checkday_fun(present, weekday_schedule, weekend_schedule, routine_fun)
    checkday_fun('2020-06-06 09:00:01', weekday_schedule, weekend_schedule, routine_fun)
    # routine_fun(weekday_schedule, present)
    # routine_fun(weekday_schedule, '2020-06-08 05:00:01')
