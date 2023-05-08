from car import Car # Importing our car file that we created
import print_title



def main():
    print(print_title.title("Taxi Service"))
    print("""
           _______
          //  ||\ \ 
    _____//___||_\ \___
    )  _          _    \ 
    |_/ \________/ \___|
    __\_/________\_/______
        """)
    input("Enter Driver's Name: ")
    color = input("What color is your car? ")
    capacity = input("Enter seating capacity: ")
    max_speed = int(input("Enter max speed: "))
    car = Car(color, capacity, max_speed)
    car.get_info()

    speed_choice = input("(a)ccelerate, (b)rake, or (e)xit : ")

    while True:




                
        if speed_choice == "b":
            car.brake()

        elif speed_choice == "s":
            car.stop()

        elif speed_choice == "x":
            car.exit()
            break
      
        elif car._speed >= max_speed:
            car.max_speed()
        
        elif speed_choice == "a":
            car.accelerate()

        else:
            break

        speed_choice = input("(a)ccelerate, (b)rake, (s)top, or e(x)it : ")


if __name__ == "__main__":
    main()