import machine
import utime
import ujson
import network
import urequests as requests
import json

# Replace with your Wi-Fi SSID and password
WIFI_SSID = "Redmi"
WIFI_PASSWORD = "12345678"

# Set your Firebase project URL and authentication token
firebase_url = "https://timetable-acfda-default-rtdb.firebaseio.com/"
auth_token = "UN36eQeV3zI2HUZCkWPsAGxj9N2hGXzVfVbNLO5a"

# Replace with your Firebase project URL and auth token
FIREBASE_URL = "https://new-attendance-78c23-default-rtdb.firebaseio.com/"
FIREBASE_AUTH_TOKEN = "6fzMnlDV1UHQg1N49HmopAEJZpXcpvNhbWE2bFbo"

# Get the current time
current_time = utime.localtime()
print(current_time)

# Set the path to the data you want to retrieve
data_path = "/TimeTable"

# Build the request URL
url = firebase_url + data_path + ".json" + "?auth=" + auth_token

# Send the GET request to Firebase
response = requests.get(url)

# Load the JSON data into a dictionary
data = ujson.loads(response.text)
print(data)

# Get the current time
#current_time = utime.localtime()
#print(current_time)
#hour_string = ''.join(current_time[3])
#print(time_string)
#timestamp = 'Joinet at' + current_time[3] + ':' + current_time[4] + ':' + current_time[5]
#print(current_time)

# Get the day of the week as an integer (0 = Monday, 6 = Sunday)
day_of_week = current_time[6]

# Map the integer day of the week to the corresponding day name
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = days[day_of_week]

# Get the current hour and minute
hour = current_time[3]
minute = current_time[4]
hour_string = str(hour)
print(hour_string)
timestamp = 'Joined at ' + str(current_time[3]) + ':' + str(current_time[4]) + ':' + str(current_time[5]) + ', ' + str(current_time[2]) + '/' + str(current_time[1]) + '/' +  str(current_time[0])
print(current_time)
print(timestamp)

timelist = []
daylist = []
for subject, table in data.items():
  for time, subject in table.items():
    timelist.append(int(time[0:2]))

# Build a string representing the current time in the format "HH:MM"
current_time_str = "{:02d}:{:02d}".format(hour, minute)

for keys,values in data.items():
    #print(keys)
    #print(day)
    #print(data)
# Check if there is a subject scheduled at the current time on the current day
    if day == keys:
    # Print the current subject
        for time, subject in values.items():
            if(hour ):
                print(hour)
                Current_Subject = data[day][str(hour)]              
                print(Current_Subject)

#_____________________________________________________________________________
# Replace the MAC addresses with their associated names
AP_NAMES = {
    "80:ad:16:85:1a:bf": "Omkar Mondkar",
    "f4:f2:6d:7f:b9:f0": "Sandeep Mondkar",
    "00:17:7c:36:d7:89": "Manoj Nikam",
    "0e:e0:dc:98:60:93": "Anushka Sonawale",
    "aa:48:fa:ff:85:97": "NodeMCU"
}

# Connect to Wi-Fi network
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(WIFI_SSID, WIFI_PASSWORD)

# Wait until connected to Wi-Fi network
while not wlan.isconnected():
    pass

# Scan for nearby access points and get their names
ap_list = wlan.scan()
name_list = []
for ap in ap_list:
    mac = ":".join("{:02x}".format(b) for b in ap[1])
    name = AP_NAMES.get(mac)
    if name is not None:
        name_list.append(name)
print(name_list)

String_timestamp = ''.join(timestamp)
print(String_timestamp)

# Convert list to dictionary
name_list_dict = {x: String_timestamp for x in name_list}

# Print each key-value pair
for key, value in name_list_dict.items():
    name_dict = {key: value}
    print(name_dict)
    

#'Attendance'[Current_Subject] = {}
#print(Current_Subject)
    
#my_list = name_list
#my_name_string = ''.join(my_list)
#print(my_name_string)

#String_Subject = ''.join(Current_Subject)
#print(String_Subject)

#a = { my_name_string : {'Attendance' : { String_Subject : { "Present days" : String_timestamp }}}}  
#print(a)

# Send names to Firebase
data = json.dumps(name_dict)
class_name = "Class-A"
URL = FIREBASE_URL + "Class-A.json?auth=" + FIREBASE_AUTH_TOKEN
response = requests.put(URL, data=data)

#Print response status code and content
print("Response status code:", response.status_code)
print("Response content:", response.content)
