import math

# 1


def average_score(score_1, score_2, score_3, score_4):
    return (score_1 + score_2 + score_3 + score_4) / 4


# 2:


def meters_to_centimeters(meters):
    return meters * 100


# 3:


def circle_area(radius):
    return 2 * radius * math.pi


# 4:


def square_area(side):
    area = side ** 2
    print(2 * area)
    return area


# 5:


def monthly_pay(hourly_rate, hours):
    return hourly_rate * hours


# 6:


def fahrenheit_to_celsius(fahrenheit):
    return 5 * ((fahrenheit - 32) / 9)


# 7:


def celsius_to_fahrenheit(celsius):
    return (9 * (celsius / 5)) + 32


# 8:


def calculations(int1, int2, real):
    print((2 * int1) * (int2 / 2))
    print((3 * int1) + real)
    print(real ** 3)


# 9:


def male_ideal_weight(height):
    return (72.7 * height) - 58


# 10:


def female_ideal_weight(height):
    return (62.1 * height) - 44.7


# 11:


def fishy_fishing(weight):
    excess = weight - 50
    if excess < 0:
        excess = 0
    fine = excess * 4
    print(f'Excess Weight: {excess} Kg')
    print(f'Fine: R${"%.2f" % fine}')


# 12:


def pay_the_man(hourly_rate, hours):
    full_pay = hourly_rate * hours
    if full_pay > 2500:
        mafia = full_pay / 5
    elif full_pay > 1500:
        mafia = full_pay / 10
    elif full_pay > 900:
        mafia = full_pay / 20
    else:
        mafia = 0
    wasted = full_pay * 0.03
    sequestered = full_pay * 0.11
    print(f"Gross Pay:        R${"%.2f" % full_pay}")
    print(f"Income Tax:       R${"%.2f" % mafia}")
    print(f"Union:            R${"%.2f" % wasted}")
    print(f"FGTS:             R${"%.2f" % sequestered}")
    print(f"Total Discounted: R${"%.2f" % (mafia + wasted)}")
    print(f"Liquid Pay:       R${"%.2f" % (full_pay - mafia - wasted)}")


# 13:


def paint_ball(area):
    liters = area // 3
    if area % 3 > 0:
        liters += 1
    cans = liters // 18
    if liters % 18 > 0:
        cans += 1
    cost = cans * 80
    print(f"Ink Cans: {cans}")
    print(f"Price: R${"%.2f" % cost}")


# 14


def paint_can(liters):
    cans = liters // 18
    if liters % 18 > 0:
        cans += 1
    cost = cans * 80
    return (cost, cans)


def paint_gallon(liters):
    gallons = liters // 3.6
    if liters % 3.6 > 0:
        gallons += 1
    gallons = round(gallons)
    cost = gallons * 25
    return (cost, gallons)


def paint_mixed(liters):
    liters = math.ceil(liters * 1.1)
    cans = liters // 18
    remain = liters % 18
    cost_gallons, gallons = paint_gallon(remain)
    cost_cans = cans * 80
    cost = cost_gallons + cost_cans
    return (cost, gallons, cans)


def paint_options(area):
    liters = area // 6
    if area % 6 > 0:
        liters += 1
    can_option = paint_can(liters)
    gallon_option = paint_gallon(liters)
    mixed_option = paint_mixed(liters)
    print('*' * 50)
    print('BUYING CANS')
    print('*' * 50)
    print(f'Nº OF CANS:       {can_option[1]}')
    print(f'COST OF CANS:     R${"%.2f" % can_option[0]}')
    print('*' * 50)
    print('BUYING GALLONS')
    print('*' * 50)
    print(f'Nº OF GALLONS:    {gallon_option[1]}')
    print(f'COST OF GALLONS:  R${"%.2f" % gallon_option[0]}')
    print('*' * 50)
    print('BUYING MIXED')
    print('*' * 50)
    print(f'Nº OF CANS:       {mixed_option[2]}')
    print(f'Nº OF GALLONS:    {mixed_option[1]}')
    print(f'COST OF MIXED:    R${"%.2f" % mixed_option[0]}')
    print('*' * 50)


# 15


def download_time(file_size, download_speed):
    file_size *= 8
    time = (file_size / download_speed) / 60
    print(f'Download time: {"%.2f" % time} minutes')
    return time


# 16


def final_score(score_1, score_2):
    average = round(((score_1 + score_2) / 2), 1)
    if average >= 9:
        final = 'A'
    elif average >= 7.5:
        final = 'B'
    elif average >= 6:
        final = 'C'
    elif average >= 4:
        final = 'D'
    else:
        final = 'E'
    print(f'Final Score: {final}')
    return final


# 17


def is_a_triangle(side_a, side_b, side_c):
    a = side_a + side_b <= side_c
    b = side_a + side_c <= side_b
    c = side_b + side_c <= side_a
    if a or b or c:
        print("Not a Triangle")
        return False
    if side_a == side_b == side_c:
        print('Equilateral Triangle')
        return True
    a = side_a == side_b
    b = side_a == side_c
    c = side_b == side_c
    if a or b or c:
        print('Isosceles Triangle')
        return True
    print('Scalene Triangle')
    return True


#18


def meat_market(meat, weight, card=False):
    if meat == "Double Fillet":
        if weight <= 5:
            cost = weight * 4.9
        else:
            cost = weight * 5.8
    elif meat == "Top Sirloin":
        if weight <= 5:
            cost = weight * 5.9
        else:
            cost = weight * 6.8
    elif meat == "Picanha":
        if weight <= 5:
            cost = weight * 6.9
        else:
            cost = weight * 7.8
    else:
        print("Unknown meat cut")
        return None
    if card:
        payment = "Store Card"
        discount = cost * 0.05
    else:
        payment = "Cash"
        discount = 0
    final_price = cost - discount
    print('*' * 50)
    print('SALE REPORT')
    print('*' * 50)
    print(f'Meat Cut:      {meat}')
    print(f'Weight:        {weight} Kg')
    print(f'Cost:          R${"%.2f" % cost}')
    print(f'Payment Form:  {payment}')
    print(f'Discount:      R${"%.2f" % discount}')
    print(f'Total to Pay:  R${"%.2f" % final_price}')
    print('*' * 50)
    return final_price
