class CalorieBurnCalculator:
    def __init__(self, height, weight, desired_calories):
        self.height = height
        self.weight = weight
        self.desired_calories = desired_calories
    
    def get_met_value(self, speed=None):
        if speed is None:
            return 3.5  # Moderate walking speed
        elif speed < 5:
            return 2.8  # Slow walking
        elif speed < 8:
            return 4.0  # Moderate walking
        else:
            return 8.0  # Running

    def calculate_time_required(self, speed):
        met_value = self.get_met_value(speed)
        calories_per_minute = (met_value * self.weight * 3.5) / 200
        return self.desired_calories / calories_per_minute

    def calculate_speed_required(self, time):
        # not quite done
        for speed in range(1, 20):  # Example range from 1 km/h to 20 km/h
            met_value = self.get_met_value(speed)
            calories_per_minute = (met_value * self.weight * 3.5) / 200
            time_needed = self.desired_calories / calories_per_minute
            if time_needed <= time:
                return speed
        return None  # If no speed found that meets the criteria within the time

def input_validation(height, weight, desired_calories, time=None, speed=None):
    if not all([height > 0, weight > 0, desired_calories > 0]):
        raise ValueError("Height, weight, and desired calories must be positive numbers.")
    if time is not None and time <= 0:
        raise ValueError("Time must be a positive number.")
    if speed is not None and speed <= 0:
        raise ValueError("Speed must be a positive number.")
    
def main():
    try:
        height = float(input("Enter your height in cm: "))
        weight = float(input("Enter your weight in kg: "))
        desired_calories = float(input("Enter the number of calories you want to burn: "))
        mode = input("Do you want to specify 'time' or 'speed'? ")
        
        calculator = CalorieBurnCalculator(height, weight, desired_calories)
        
        if mode.lower() == 'speed':
            speed = float(input("Enter the speed in km/h you plan to walk/run at: "))
            time_required = calculator.calculate_time_required(speed)
            print(f"You will need to be active for {time_required:.2f} minutes.")
        
        elif mode.lower() == 'time':
            time = float(input("Enter the amount of time in minutes you plan to be active: "))
            speed_required = calculator.calculate_speed_required(time)
            print(f"You will need to walk/run at a speed of {speed_required:.2f} km/h.")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
