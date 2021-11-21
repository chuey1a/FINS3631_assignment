# FF

import csv

#income
eric_income = 250000
eric_income_list = []
eric_after_income_list = []
emily_income = 150000
emily_income_list = []
emily_after_income_list = []
total_income_list = []

wage_inflation = 1.024

#expenditure
yearly_expenditure = 85000
total_expenditure_list = []
fee_index = 1.021
single_child = 27000
double_child = 54000
schoolCount = 2

loan_repayment = 9500*12
loan_count = 0
inflation = 1.021

#Surplus
yearly_surplus = []

#Super
eric_super = 140000
eric_super_list = []
emily_super = 85000
emily_super_list = []
r = 0.055
SGC_list = [0.1, 0.105, 0.11, 0.115, 0.12]
for i in range(26):
    SGC_list.append(0.12)

SGC_cuttoff = 235680

#Net wealth
misc_assets = 17500+85000+220000+80000+40000
house = 1850000
mortgage = 1150000
vr = 0.032/12
total_assets_list = []
total_liabilities_list = []
net_wealth_list = []

#info
eric_age = 36
emily_age = 35
retirement_age_eric = 67
retirement_age_emily = retirement_age_eric - 1

year_list = []
for i in range(2022,2053):
    year_list.append(i)

for i in range(retirement_age_eric-eric_age):
    #########
    # Cash flow projection
    eric_income *= wage_inflation
    emily_income *= wage_inflation
    #increase with AWOTE
    eric_income_list.append(round(eric_income,2))
    emily_income_list.append(round(emily_income,2))

    #take away tax
    after_tax_eric = eric_income - 51667 - (eric_income - 180000)*0.45
    eric_after_income_list.append(round(after_tax_eric,2))
    if emily_income <= 180000:
        after_tax_emily = emily_income - 29467 - (emily_income - 120000)*0.37
        emily_after_income_list.append(round(after_tax_emily,2))
    else:
        after_tax_emily = emily_income - 51667 - (emily_income - 180000)*0.45
        emily_after_income_list.append(round(after_tax_emily,2))

    #total income
    total_income = after_tax_eric + after_tax_emily
    total_income_list.append(round(total_income,2))

    #total expenditure
    yearly_expenditure *= inflation
    if loan_count < 12:
        total_expenditure = yearly_expenditure + loan_repayment
    if loan_count == 12:
        total_expenditure = yearly_expenditure + 3512.58
    if loan_count > 12:
        total_expenditure = yearly_expenditure

    total_expenditure_list.append(round(total_expenditure,2))

    surplus = total_income - total_expenditure

    yearly_surplus.append(round(surplus,2))
    ########

    ########
    # super calcs
    if emily_income < SGC_cuttoff:
        emily_SGC = emily_income*SGC_list[i]
    else:
        emily_SGC = SGC_cuttoff*SGC_list[i]

    eric_SGC = SGC_cuttoff*SGC_list[i]

    eric_super += (r*eric_super + eric_SGC)*0.85
    eric_super_list.append(round(eric_super,2))
    emily_super += (r*emily_super + emily_SGC)*0.85
    emily_super_list.append(round(emily_super,2))
    SGC_cuttoff *= wage_inflation


    ########

    ########
    #net wealth projection
    house *= 1 + r
    total_assets = house + misc_assets + eric_super + emily_super
    total_assets_list.append(round(total_assets,2))

    interest = 0
    if loan_count < 12:
        for i in range(12):
           interest += vr*mortgage
           mortgage = mortgage - (9500-interest)
           interest = 0
        total_liabilities = mortgage
    if loan_count >= 12:
        total_liabilities = 0
    loan_count += 1

    total_liabilities_list.append(round(total_liabilities,2))

    net_wealth = total_assets - total_liabilities
    net_wealth_list.append(round(net_wealth,2))
    ########

total_super_list = []
for i in range(len(eric_super_list)):
    total_super_list.append(round(emily_super_list[i],2) + round(eric_super_list[i],2))

print(total_income_list)
print()
print(total_expenditure_list)
print()
print(yearly_surplus)
print()
print(emily_super_list)
print()
print(eric_super_list)
print()
print(total_super_list)
print()
print(total_assets_list)
print()
print(total_liabilities_list)
print()
print(net_wealth_list)
print()

log_filename = "Projection_no_schoool_calcs.csv"

with open(log_filename, 'a') as f:
    f.write("Years," + str(year_list).replace('[','').replace(']','') + "\n")
    f.write("Yearly Surplus," + str(yearly_surplus).replace('[','').replace(']','') + "\n")
    f.write("Eric Yearly Super," + str(eric_super_list).replace('[','').replace(']','') + "\n")
    f.write("Emily Yearly Super," + str(emily_super_list).replace('[','').replace(']','') + "\n")
    f.write("Combined Super," + str(total_super_list).replace('[','').replace(']','') + "\n")
    f.write("Total Assets," + str(total_assets_list).replace('[','').replace(']','') + "\n")
    f.write("Total Liabilities," + str(total_liabilities_list).replace('[','').replace(']','') + "\n")
    f.write("Net Wealth," + str(net_wealth_list).replace('[','').replace(']',''))
