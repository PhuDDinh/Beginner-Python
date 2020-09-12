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



print(cheapest_shipping(8))