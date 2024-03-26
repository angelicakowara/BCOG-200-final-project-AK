class CalorieBurnCalculator:
    def __init__(self, height, weight, desired_calories):
        """
    input height, weight, desired calories to burn, speed? idk come back to this 
        """
        
    def get_met_value(self, speed=None):
        """
        Returns a MET value based on the walking/running speed.
        If speed is None, it assumes a moderate walking speed.
        
        :param speed: float, the speed in km/h (optional)
        :return: float, the assumed MET value
        """
        # Example of MET values
        if speed is None:
            return 3.5  # i'll assume moderate walking speed if none is provided
        elif speed < 5:
            return 2.8  # Slow walking
        elif speed < 8:
            return 4.0  # Moderate walking
        else:
            return 8.0  # Running

    def calculate_time_required(self, speed):
        """
        Calculates the time required to burn the desired amount of calories at the given speed.
        using same logic/math i used in the exmaple run in readme
        """
        met_value = self.get_met_value(speed)
        calories_per_minute = (met_value * self.weight * 3.5) / 200
        return self.desired_calories / calories_per_minute

    def calculate_speed_required(self, time):
        """
        Calculates the speed required to burn the desired amount of calories in the given time.
        this part i think will take a lot more work to tackle 
        """
        
def main():
    
if __name__ == "__main__":
    main()
