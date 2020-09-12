# Instructions:
#Sal runs the biggest shipping company in the tri-county area, Sal's Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages. In this project, you'll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal's Shippers.

Sal's Shippers has several different options for a customer to ship their package. They have ground shipping, which is a small flat charge plus a rate based on the weight of your package. Premium ground shipping, which is a much higher flat charge, but you aren't charged for weight. They recently also implemented drone shipping, which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$1.50	$20.00
Over 2 lb but less than or equal to 6 lb	$3.00	$20.00
Over 6 lb but less than or equal to 10 lb	$4.00	$20.00
Over 10 lb	$4.75	$20.00
Drone Shipping

Weight of Package	Price per Pound	Flat Charge
2 lb or less	$4.50	$0.00
Over 2 lb but less than or equal to 6 lb	$9.00	$0.00
Over 6 lb but less than or equal to 10 lb	$12.00	$0.00
Over 10 lb	$14.25	$0.00
Premium Ground Shipping

Flat charge: $125.00

Write a program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal's Shippers.

If you get stuck during this project, check out the project walkthrough video which can be found at the bottom of the page after the final step of the project.


premium_ground_cost = 125

def ground_shipping(weight):
  cost = weight * 4.75 + 20
  if weight <=2:
    cost = weight * 1.5 + 20
  elif weight <=6:
    cost = weight * 3 + 20
  elif weight <=10:
    cost = weight * 4 + 20
  return cost

def drone_shipping(weight):
  cost = weight * 14.25
  if weight <=2:
    cost = weight * 4.5
  elif weight <=6:
    cost = weight * 9
  elif weight <=10:
    cost = weight * 12
  return cost

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = premium_ground_cost
  if ground < drone and ground < premium:
    cheapest = "ground shipping"
    cost = ground
  elif drone < ground and drone < premium:
    cheapest = "drone shipping"
    cost = drone
  elif premium < drone and premium < ground:
    cheapest = "premium shipping"
    cost = premium
  return "The cheapest shipping is " +str(cheapest)+ " and it will cost "+ str(cost)+"."



price_ground = ground_shipping(8.4)
price_drone = drone_shipping(1.5)
package_1 = cheapest_shipping(4.8)
package_2 = cheapest_shipping(41.5)

print(price_ground, price_drone, package_1, package_2)