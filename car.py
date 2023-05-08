"""
Filename: car.py
Author: Abbigail Rath
Created: 4/30/23
Purpose: Create a program that can increase and decrease speed, stop, and exit the car
"""


# Define the car class
class Car():
    # Define init and include color, speed, capacity, and max speed
    def __init__(self, color, capacity, max_speed=100):
        self._color = color
        self._speed = 50
        self._capacity = capacity
        self._max_speed = max_speed

    def accelerate(self):
        # Add 5mph to the speed
        self._speed += 5
        # Print results
        print(f"The {self._color} car is going {self._speed} mph.")

    def brake(self):
        # Subtract 5mph from the speed
        self._speed -= 5
        # Print results
        print(f"The {self._color} car is going {self._speed} mph.")

    def stop(self):
        # If the speed = 0 print that the car has stopped
        self._speed == 0
        print(f"The {self._color} car has stopped!")

    def max_speed(self):
        # Print that you cant go any faster if user reaches max speed
        if self._speed == self._max_speed:
            print("You can't go any faster!")
        self._speed = self._max_speed
        print(f"You are going {self._speed} mph")

    def exit(self):
        # Print goodbye message
        print("""
        
                       ___
                   ,-'"   "`-.
                 ,'_          `.  
                / / \  ,-       \ 
          __   | \_0 ---        |
         /  |  |                |
         \  \  `--.______,-/    |
       ___)  \  ,--""    ,/     |
      /    _  \ \-_____,-      / 
      \__-/ \  | `.          ,'  
        \___/ <    �--------'    
         \__/\ |              
          \__//""")
        print("Thank you for choosing our services!")


    def get_speed(self):
        # Print how fast the car is going
        print(f"The {self._color} car is going {self._speed} mph.")

    def get_info(self):
        # Print out the information about the car
        print(f"The {self._color} car that holds {self._capacity} people has a max speed of {self._max_speed}MPH")