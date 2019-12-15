import subprocess

#threshold = 200

#binary = []

#count = 0

def read_sensor():
    #returns output as byte string
    sensor_reading = subprocess.check_output('cat /dev/rtlightsensor0', shell=True)

    #using decode() function to convert byte string to string
    sensor_reading_string = sensor_reading.decode('utf-8')

    #convert string into a list of integers
    sensor_reading_list = list(map(int, sensor_reading_string.split()))
    
    print(sensor_reading_list)
    #for i in sensor_reading_list:
    #    if i > threshold:
    #        binary[count] = 1
    #    else:
    #        binary[count] = 0
    #    count += count
    #    
    #return binary
    return sensor_reading_list
