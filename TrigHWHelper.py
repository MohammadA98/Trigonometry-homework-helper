import math


while True:

    # Ask user to choose one of two operations using either 1 or 2
    choice = 0
    while choice not in range(1, 3):
        print("Please select:")
        print("1. Find missing Leg or Hypotenuse")
        print("2. Find the six trigonometric functions")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("That is not a valid choice.")

    if choice == 1:

        hyp_leg = input("Enter H to find Hypotenuse or L to find missing Leg\n Choice : ").lower()
        # Ask user to enter one of two choices available
        while hyp_leg not in ["h", "l"]:
            print("Please select:")
            print("Enter H to find Hypotenuse")
            print("Enter L to find missing Leg")
            try:
                hyp_leg = input("Choice: ").lower()
            except ValueError:
                print("That is not a valid choice.")

        if hyp_leg == "h":
            while True:
                try:
                    # Ask user for 2 legs to be able to find Hypotenuse
                    Leg1 = float(input("Enter Leg 1 length: "))
                    Leg2 = float(input("Enter Leg 2 length: "))
                    break
                except ValueError:
                    print('Input must be number')
            # Calculate the hypotenuse by adding the square of the first and second leg and square rooting the result
            hypotenuse = Leg1 ** 2 + Leg2 **2
            # print result + text to clarify result
            print("The length of your hypotenuse is : ", math.sqrt(hypotenuse))

        # if the user has the hypotenuse and one of the legs but needs the second
        elif hyp_leg == "l":
        # Ask user for Hypotenuse
            hypotenuse = float(input("Enter Hypotenuse length: "))
        # Ask user for leg
            Leg = float(input("Enter Leg length: "))

        # Calculate the missing leg by subtracting the square of the existing leg from the square of the hypotenuse and then square rooting the result
            missing_leg = hypotenuse**2 - Leg **2
        # Print result + text to clarify result
            print("The length of your missing leg is : ", math.sqrt(missing_leg))

    elif choice == 2:
        print("Please enter the following...")
        while True:
            try:
                # take input for opposite leg
                opposite = float(input("Enter the length of the leg opposite to your angle: "))
                # take input for adjacent leg
                adjacent = float(input("Enter the length of the leg adjacent to your angle: "))
                # take input for hypotenuse
                hypotenuse = float(input("Enter the length of your hypotenuse: "))
                break
            except ValueError:
                print('Input must be a number')
        # print trig functions
        print("Your sin θ function is :", opposite,'/',hypotenuse)
        print("Your cos θ function is :", adjacent,'/',hypotenuse)
        print("Your tan θ function is :", opposite,'/',adjacent)
        print("Your csc θ function is :", hypotenuse,'/',opposite)
        print("Your sec θ function is :", hypotenuse,'/',adjacent)
        print("Your cot θ function is :", adjacent, '/', opposite)

    # Ask user if they would like to repeat the program hence the first while loop
    if input('Would you like to do another operation? (y/n)') == 'n':
        break













