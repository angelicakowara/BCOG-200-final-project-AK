Documentation file: An overview/outline/draft of the material that you will provide to users to guide them through using your program. Examples of elements to include are: names of functions/methods and the argument options that go with them, example use cases, introduction to the logic ("sales pitch") for your program

Description: 
The aim of this project is to provide the user with a quantitative number, either an amount of time or a walking/running speed, that needs to be met to burn a certain number of calories. The idea right now is that the 
user will input their height, weight, desired number of calories to be burned, and then one of the following: a) an amount of time they would like to be active or b) a speed they would like to walk/run at, and then
the application would return an amount of time if the person provided a speed, or a speed if the user provided an amount of time.

Input
The program requires the following inputs from the user:
  Weight (in kilograms): Enter your weight to the nearest kilogram.
  Desired Calories to Burn: Enter the number of calories you wish to burn during your activity.
  Activity Time (optional): If you have a specific time frame for your activity, enter the duration in minutes.
  Speed (optional): If you have a target speed, enter it in kilometers per hour (km/h).

Output
Depending on the inputs provided, the program will output one of the following:
  Required Time: The duration (in minutes) you need to walk or run at your specified speed to achieve your calorie burn goal.
  Required Speed: The speed (in km/h) you need to maintain for your specified time to reach your calorie burn goal.


Functions: 
1) inputValidation (weight, calories, time=none, speed=none) :
    This function will ensure that the user is inputing valid values for the weight, height, desired calories to burn, and either speed or time. If they do not put a value for a category or put an
    invalid value, the program should throw a reader-friendly error tellingg the user what is missing/invalid.
2) calculateTimeRequired (weight, calories, speed) : 
    If the user decided to input a speed at which they would like to moving, then this function should be called and carry out appropriate calculations and return an amount of time 
    the user should be active at the speed they provided to burn their desired amount of calories.
3) calculateSpeedRequired (weight, calories, time) : 
    If the user decided to input a time of which they would like to moving, then this function should be called and carry out appropriate calculations and return a speed the user should 
    be walking/running at for the amount of time they input to burn their desired amount of calories.

Example case + math/logic included
-user input: 
  Weight: 75 kg
  Desired Calories to Burn: 300
  Speed: 8 km/h

-assume MET value of 8 for 8km/hr

-calculate calories burned per minute
  Calories per minute=(8 METs×75 kg×3.5)/200
  Calories per minute=(2100/200) =10.5 calories/minute

-calculate time required 
time required = 300 calories / (10.5 calories/minute) = 28.6 minutes 

-return time required to the user 



