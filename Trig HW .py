import math
import time

# Ask user what trig operation they would like to do
choice = int(input("What do you want to do today?\n 1. Find missing Leg or Hypotenuse\n 2. Find the six trigonometric functions\n Choice : "))
# Ask user to enter one of two choices available
while choice != 1 and choice != 2:
        print("Please enter either 1 or 2")
        time.sleep(1)
        choice = int(input("1. Find missing Leg or Hypotenuse\n2. Find the six trigonometric functions\n Choice: "))
        break

if choice == 1:
    # Wait time so it's not too fast and unorganized
    time.sleep(1)
    hyp_leg = input("Enter H to find Hypotenuse or L to find missing Leg\n Choice : ").lower()
    # Ask user to enter one of two choices available
    while hyp_leg != 'h' and hyp_leg != 'l':
        print("Please enter either H or L")
        time.sleep(1)
        hyp_leg = input("Enter H to find Hypotenuse or L to find missing Leg\n Choice : ").lower()
        break
    if hyp_leg == "h":
        # Ask user for 2 legs to be able to find Hypotenuse
        Leg1 = int(input("Enter Leg 1 length: "))
        # Wait time again
        time.sleep(1)
        Leg2 = int(input("Enter Leg 2 length: "))
        # Calculate the hypotenuse by adding the square of the first and second leg and square rooting the result
        hypotenuse = Leg1 ** 2 + Leg2 **2
        # print result + text to clarify result
        print("The length of your hypotenuse is : ", math.sqrt(hypotenuse))

    # if the user has the hypotenuse and one of the legs but needs the second
    elif hyp_leg == "l":
    # Ask user for Hypotenuse
        hypotenuse = int(input("Enter Hypotenuse length: "))
    # Wait time once more
        time.sleep(1)
    # Ask user for leg
        Leg = int(input("Enter Leg length: "))

    # Calculate the missing leg by subtracting the square of the existing leg from the square of the hypotenuse and then square rooting the result
        missing_leg = hypotenuse**2 - Leg **2
    # Print result + text to clarify result
        print("The length of your missing leg is : ", math.sqrt(missing_leg))

elif choice == 2:
    time.sleep(1)
    print("Please enter the following...")
    time.sleep(1)
    # take input for opposite leg
    opposite = int(input("Enter the length of the leg opposite to your angle: "))
    time.sleep(1)
    # take input for adjacent leg
    adjacent = int(input("Enter the length of the leg adjacent to your angle: "))
    time.sleep(1)
    # take input for hypotenuse
    hypotenuse = int(input("Enter the length of your hypotenuse: "))
    time.sleep(1)
    print("Forming trigonometric functions...\n"
          "please be patient")
    time.sleep(3)
    # print trig functions
    print("Your sin θ function is :", opposite,'/',hypotenuse)
    time.sleep(1)
    print("Your cos θ function is :", adjacent,'/',hypotenuse)
    time.sleep(1)
    print("Your tan θ function is :", opposite,'/',adjacent)
    time.sleep(1)
    print("Your csc θ function is :", hypotenuse,'/',opposite)
    time.sleep(1)
    print("Your sec θ function is :", hypotenuse,'/',adjacent)
    time.sleep(1)
    print("Your cot θ function is :", adjacent, '/', opposite)













