"""
Develop a program that allows a taxi company to calculate how much taxi fare should be.
The program should:
- Prompt the user to enter the journey distance in km
    *The distance entered must be greater than 0.
    *The user should be made to re-enter the distance until it's valid.
- Prompt the user to enter the number of passengers (No validation needed)
- Calculate taxi fare by:
    *Charging £2 per passenger regardless of distance.
    *Charging a further £1.50 per kilometer regardless of how many passengers there are
-Output the final taxi fare.
"""

numberOfPassengers = int(input("Please enter a number of passengers: "))
lengthOfJourney = int(input("Please enter the journey distance: "))
while lengthOfJourney < 1:
    lengthOfJourney = int(input("Please enter the journey distance greater than 0km: "))
