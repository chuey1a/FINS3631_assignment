time_till_retirement = 31
PV = 75000
n = 0
r = 0.055
inflation = 0.021
year = 2021
time_till_death = 21

FV = PV * (1 + inflation)**time_till_retirement
FV = round(FV,2)
print(FV)

lumpSum = 0
for i in range(time_till_death):
    lumpSum += FV*(1+inflation)**i

lumpSum = round(lumpSum,2)
print(lumpSum)


