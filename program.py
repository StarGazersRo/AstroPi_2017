#### Libraries #####
from sense_hat import SenseHat
from datetime import datetime
from time import sleep
from math import sqrt

##### Logging Settings #####

FILENAME = ""
WRITE_FREQUENCY = 1

##### Variable #####
sense = SenseHat()

sense.clear()

g=[0,200,0]

initial = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g
]

r = [255,0,0]
w = [0,0,0]
y = [255,255,0]
aurora = [
    w,w,w,r,r,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,r,r,w,w,w,
    w,w,w,r,r,w,w,w
]

here = [
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y,
    y,y,y,y,y,y,y,y
]

sense.set_pixels(initial)

hi = 50   # trebuie modificata pentru valorile de pe ISS


##### Functions #####


def log_data():
    output_string = ",".join( str(value) for value in sense_data )
    batch_data.append(output_string)


def file_setup(filename):
    header = ["row_id","temp_h","temp_p",
          "humidity","pressure",
          "pitch","roll","yaw",
          "mag_x","mag_y","mag_z",
          "accel_x","accel_y","accel_z",
          "gyro_x","gyro_y","gyro_z",
          "timestamp"]

    with open(filename,"w") as f:
        f.write(",".join(str(value) for value in header)+ "\n")


def get_sense_data(numar):   # collecting data
    sense_data=[]

    sense_data.append(numar)
    sense_data.append(sense.get_temperature_from_humidity())
    sense_data.append(sense.get_temperature_from_pressure())
    sense_data.append(sense.get_humidity())
    sense_data.append(sense.get_pressure())

    o = sense.get_orientation()
    yaw = o["yaw"]
    pitch = o["pitch"]
    roll = o["roll"]
    sense_data.extend([pitch,roll,yaw])

    mag = sense.get_compass_raw()
    mag_x = mag["x"]
    mag_y = mag["y"]
    mag_z = mag["z"]
    sense_data.extend([mag_x,mag_y,mag_z])

    acc = sense.get_accelerometer_raw()
    x = acc["x"]
    y = acc["y"]
    z = acc["z"]
    sense_data.extend([x,y,z])

    gyro = sense.get_gyroscope_raw()
    gyro_x = gyro["x"]
    gyro_y = gyro["y"]
    gyro_z = gyro["z"]
    sense_data.extend([gyro_x,gyro_y,gyro_z])

    sense_data.append(datetime.now())

    return sense_data
    
##### Main Program #####

sense = SenseHat()

batch_data = []

numar = 1

if FILENAME == "":
    filename = "SenseLog-"+str(datetime.now())+".csv"
else:
    filename = FILENAME +"-"+str(datetime.now())+".csv"
file_setup(filename)

human=0

while True:
    acceleration = sense.get_accelerometer_raw()
    
    h = sense.get_humidity()
    h = round( h , 5 )

    print(h)
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']

    x = abs(x)
    y = abs(y)
    z = abs(z)

    x = round(x, 3)
    y = round(y, 3)
    z = round(z, 3)

    dh=h-hi

    if h == hi :
        sense.set_pixels(initial)
        human = 0
    if dh >= 2 and human == 0:
        sense.show_message("We got you!")
        sense.set_pixels(here)
        human = 1
    if x > 1 or y > 1 or z > 1 and human == 0:
        sense.show_message("We got you!")
        sense.set_pixels(here)
        human = 1
        
    mg = sense.get_compass_raw()
    x = mg['x']
    y = mg['y']
    z = mg['z']

    B = x*x + y*y + z*z
    B = sqrt(B)
    if B > 55:
        sense.set_pixels(aurora)
    else:
        if B<55 and human == 1:
            sense.set_pixels(here)

    sleep(1)
    sense_data = get_sense_data(numar)
    numar = numar + 1
    log_data()

    if len(batch_data) >= WRITE_FREQUENCY:
        print("Writing to file ... ")
        with open(filename,"a") as f:
            for line in batch_data:
                f.write(line + "\n")
            batch_data = []


