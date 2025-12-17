''' # Version 1
hour = 12#int(input("Starting time (hours): "))
mins = 17#int(input("Starting time (minutes): "))
dura = 59#int(input("Event duration (minutes): "))

seconds = (hour * 3600) + (mins * 60) + (dura * 60)
#print(seconds)
#minutes = int(((seconds / 3600) - int(seconds / 3600)) * 60)
#print(minutes)
minutes = int((seconds % 3600) / 60)
#print(minutes)
hours = int(seconds / 3600)

print(f"""
{hours}:{minutes}
""")
'''

''' # Version 2
hour = 12#int(input("Starting time (hours): "))
mins = 17#int(input("Starting time (minutes): "))
dura = 59#int(input("Event duration (minutes): "))
mins = mins + hour * 60 + dura
hour = int(mins / 60)
mins = mins % 60
print(hour, ":", mins, sep='')
'''

''' # Version 3
hour = 23#int(input("Starting time (hours): "))
mins = 58#int(input("Starting time (minutes): "))
dura = 642#int(input("Event duration (minutes): "))
mins = mins + hour * 60 + dura
hour = int(mins / 60) % 24
mins = mins % 60
print(hour, ":", mins, sep='')
'''

# Version 4
def evaluate_end_time(hour, mins, dura):
    """Evaluates the end time"""
    msg = None
    try:
        hour, mins, dura = int(hour), int(mins), int(dura)
        if not 0 <= hour <= 23:
            raise Exception("Hours must be between 0 and 23!")
        if not 0 <= mins <= 59:
            raise Exception("Minutes must be between 0 and 59!")
        if not dura >= 0:
            raise Exception("Duration must be positive!")
        mins = (hour * 60 + mins) + dura
        hour = int(mins / 60) % 24
        mins = mins % 60
    except ValueError:
        msg = "Only integers are allowed!"
    except Exception as e:
        msg = e
    except:
        msg = "The end time couldn't be calculated!"
    return f"{hour}:{mins}", msg

def receive_time():
    """Receives the user input"""
    hour, mins, dura = None, None, None
    try:
        while True:
            try:
                hour = int(input("Starting time (hours): "))
                if hour >= 0 and hour <= 23:
                    break
                else:
                    print("Hours must be between 0 and 23!")
            except ValueError:
                print("Only integers are allowed!")
        while True:
            try:
                mins = int(input("Starting time (minutes): "))
                if mins >= 0 and mins <= 59:
                    break
                else:
                    print("Minutes must be between 0 and 59!")
            except ValueError:
                print("Only integers are allowed!")
        while True:
            try:
                dura = int(input("Event duration (minutes): "))
                if dura >= 0:
                    break
                else:
                    print("Duration must be positive!")
            except ValueError:
                print("Only integers are allowed!")

    except KeyboardInterrupt:
        print("\nProgram terminated.")
        quit()
    except:
        print("Something went wrong! Try again.")
    return hour, mins, dura

def test_code():
    """Tests the code by using predefined values"""
    input_hour = [12, 23, 0, 23]
    input_mins = [17, 58, 1, 59]
    input_dura = [59, 642, 2939, 2]
    output = ['13:16', '10:40', '1:0', '0:1']
    for i in range(len(input_hour)):
        if evaluate_end_time(input_hour[i], input_mins[i], input_dura[i]) == output[i]:
            print(f"Success! {input_hour[i]}:{input_mins[i]} after {input_dura[i]} mins is {output[i]}")
        else:
            print(f"Error! {input_hour[i]}:{input_mins[i]} after {input_dura[i]} mins is NOT {output[i]}")

if __name__ == "__main__":
    hour, mins, dura = receive_time()
    end_time, msg = evaluate_end_time(hour, mins, dura)
    if msg is None:
        print(end_time)
    else:
        print(msg)
    #test_code()
