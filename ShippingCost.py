weight_input = input("Please input the weight of your item: ")
weight = int(weight_input)


def ground_shipping(weight):
    if weight <= 2.0:
        cost = (weight * 4.00) + 20.00
        return cost
    elif 2 < weight <= 6.0:
        cost = (weight * 3.00) + 20.00
        return cost
    elif 6 < weight <= 10.0:
        cost = (weight * 4.00) + 20.00
        return cost
    elif weight > 10.0:
        cost = (weight * 4.75) + 20.00
        return cost


premium_ground_shipping = 125.00


def drone_shipping(weight):
    if weight <= 2.0:
        cost = (weight * 4.50)
        return cost
    elif 2 < weight <= 6.0:
        cost = (weight * 9.00)
        return cost
    elif 6 < weight <= 10.0:
        cost = (weight * 12.00)
        return cost
    elif weight > 10.0:
        cost = (weight * 14.25)
        return cost


def cheapest_shipping(weight):
    if premium_ground_shipping <= ground_shipping(weight) or premium_ground_shipping <= drone_shipping(weight):
        return "You should ship using Premium Ground Shipping, it will cost $" + str(premium_ground_shipping)
    elif drone_shipping(weight) < ground_shipping(weight):
        return "You should ship using Drone Shipping, it will cost $" + str(drone_shipping(weight))
    elif ground_shipping(weight) < drone_shipping(weight):
        return "You should ship using Ground Shipping, it will cost $" + str(ground_shipping(weight))


print(cheapest_shipping(weight))
