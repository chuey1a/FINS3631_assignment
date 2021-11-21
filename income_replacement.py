#replacement of income

emily_income = 150000
eric_income = 250000
inflation = 1.021
wage_inflation = 1.024
ytr = 29
percent_of_income = 0.60

#ADD
PV_emily_income = 0
PV_eric_income = 0
for i in range(ytr):
    PV_emily_income += percent_of_income*emily_income*(wage_inflation**(i+1))/(inflation**(i+1))
    PV_eric_income += percent_of_income*eric_income*(wage_inflation**(i+1))/(inflation**(i+1))

PV_emily_super = 1767571.46/(inflation**ytr) - 125000
PV_eric_super = 2820940.41/(inflation**ytr) - 220000

#Remove
mortgage = 1150000

count = 2
PV_school_fees = 0
for i in range(15):
    if i + 2022 == 2024 or i + 2022 == 2023 or i + 2022 >= 2036 or i + 2022 == 2037:
        PV_school_fees += 27000/inflation*count
    if i + 2022 > 2024 and i + 2022 < 2036:
        PV_school_fees += 54000/inflation**count
    count += 1


total_emily = PV_emily_income + PV_emily_super - mortgage - PV_school_fees
total_eric = PV_eric_income + PV_eric_super - mortgage - PV_school_fees

print(round(PV_eric_income,2))
print(round(PV_emily_income,2))