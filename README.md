# Introduction

We are a group of students from “Tudor Vianu” National Highschool of Computer Science, Bucharest, deeply passionate about programming, robotics and physics. We are eager to learn new things about our world. Even if we are only at the beginning of our journey into the misteries of science, we are very enthusiastic to research and to conduct an experiment about the topic that we have chosen. We appreciate this chance and our team would like to thank you for giving us this great opportunity. 

Our idea was to investigate the magnetic field of Earth, using Astro Pi kit. 

Our objectives :
-	to follow the trajectory of ISS and find out if Earth’s magnetic poles have any influence on the instruments on board.
-	to investigate if there are areas on Earth where the magnetic field has reversed its poles.
-	to use sound and light warnings for the ISS crew when an increase in the intensity of Earth’s magnetic field is detected and activate a camera which photographs the auroras.
We are going to need the Inertial Measurement Unit:
•	Magnetometer sensor
•	Gyroscope sensor
•	Accelerometer sensor


# Primary mission
Main objective(s): To detect crew presence in the Columbus module using the ISS Astro Pi and its sensors
Procedure 
In order to detect the human presence in the Columbus module, we used the humidity sensor, because the crew affects the humidity level. Using the sensor readings from the ISS life support system, we were able to correlate human activity with humidity. The human body naturally radiates heat, and through breathing and perspiration they release moisture into the air that increases humidity. After the astronauts leave the module, the humidity starts decreasing, the Astro Pi being able to detect their absence. Thus, using the formula: 

             ∆h = h – h0

our robot provides data about the activity inside Columbus.
We also used the accelerometer. Because of the lack of gravity on ISS, the astronauts must grab the walls to move around. When they touch the wall, they generate vibrations that the Astro Pi receives, using them to detect human activity in the module. Because the variation of humidity is much slower than generating vibrations, the accelerometer could be more efficient in receiving and interpreting data. As such, with the help of the formulas

		∆ax = ax – ax0			∆ay = ay – ay0			∆az = az – az0

we can identify crew activity with the accelerometer.



# Secondary  mission

Main objective(s)

Our objective was to predict the formation of auroras, so that the astronauts would be able to photograph them and send the pictures to Earth.

Procedure

For this mission, we used the magnetometer. Values of the magnetic field induction are received on 3 axes. Using the formula:
      B2 = Bx2 + By2 + Bz2

we managed to correlate this value with the position of the ISS relative to Earth’s magnetic poles and the Equator. Because the induction is between 25-65 µT, we could compare the current value with those at higher latitudes, where the auroras are.


