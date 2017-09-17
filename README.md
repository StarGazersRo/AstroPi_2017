# AstroPi_2017

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


