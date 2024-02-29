Description: 
The aim of this project is to provide the user with a quantitative number, either an amount of time or a walking/running speed, that needs to be met to burn a certain number of calories. The idea right now is that the 
user will input their height, weight, desired number of calories to be burned, and then one of the following: a) an amount of time they would like to be active or b) a speed they would like to walk/run at, and then
the application would return an amount of time if the person provided a speed, or a speed if the user provided an amount of time.

Functions: 
1) inputValidation: This function will ensure that the user is inputing valid values for the weight, height, desired calories to burn, and either speed or time. If they do not put a value for a category or put an
                    invalid value, the program should throw a reader-friendly error tellingg the user what is missing/invalid.
2) calculateTimeRequired: If the user decided to input a speed at which they would like to moving, then this function should be called and carry out appropriate calculations and return an amount of time 
                          the user should be active at the speed they provided to burn their desired amount of calories.
3) calculateSpeedRequired: If the user decided to input a time of which they would like to moving, then this function should be called and carry out appropriate calculations and return a speed the user should 
                           be walking/running at for the amount of time they input to burn their desired amount of calories.
