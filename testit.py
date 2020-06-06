#For first House
print('Enter your your initial cost for first house : ')
first_house_cost = input()
'check if the number input is number or convert input to numbers'
first_house_cost_num = int(first_house_cost)

print('What is the annual fuel cost of the first house : ')
annual_fuel_cost = input()
int_annual_fuel_cost = int(annual_fuel_cost)

year = 5
print('Tax rate of the first house : ')
tax_rate = input()

int_tax_rate = float(tax_rate)

fuel_cost = int_annual_fuel_cost * year

tax = int_tax_rate * first_house_cost_num

tax_for_fiveYrs = tax * year

total_cost = first_house_cost_num + fuel_cost + tax_for_fiveYrs

print(total_cost)



#For second House
print('Enter your your initial cost for second house : ')
second_house_cost = input()
'check if the number input is number or convert input to numbers'
second_house_cost_num = int(second_house_cost)

print('What is the annual fuel cost of the first house: ')
annual_fuel_cost = input()
int_annual_fuel_cost = int(annual_fuel_cost)

year = 5
print('Tax rate of the first house: ')
tax_rate = input()

int_tax_rate = float(tax_rate)

fuel_cost = int_annual_fuel_cost * year

tax = int_tax_rate * second_house_cost_num

tax_for_fiveYrs = tax * year

total_cost = second_house_cost_num + fuel_cost + tax_for_fiveYrs

print(total_cost)



#For third House
print('Enter your your initial cost for third house : ')
third_house_cost = input()
'check if the number input is number or convert input to numbers'
third_house_cost_num = int(third_house_cost)

print('What is the annual fuel cost of the  third house : ')
annual_fuel_cost = input()
int_annual_fuel_cost = int(annual_fuel_cost)

year = 5
print('Tax rate of the second house : ')
tax_rate = input()

int_tax_rate = float(tax_rate)

fuel_cost = int_annual_fuel_cost * year

tax = int_tax_rate * third_house_cost_num

tax_for_fiveYrs = tax * year

total_cost = third_house_cost_num + fuel_cost + tax_for_fiveYrs

print(total_cost)

