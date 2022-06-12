bazar_er_list = ["Rice", "Beef", "Rice"]
location = 'Chankharpool'


def total_charge_ashbe(bz, loc='Dhanmondi'):
    price = {
        'Rice': 105,
        'Potato': 20,
        'Chicken': 250,
        'Beef': 510,
        'Oil': 85
    }
    charge = 0
    for x in bz:
        charge = charge + price[x]
    if loc == 'Dhanmondi':
        charge = charge + 30
    else:
        charge = charge + 70
    return charge

print(total_charge_ashbe(bazar_er_list, 'Mohakhali'))
print(total_charge_ashbe(bazar_er_list))
