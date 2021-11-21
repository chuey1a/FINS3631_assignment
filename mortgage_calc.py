owing = 1150000
vr = 0.032/26
n = 0
owing_list = [1150000]
payment = 5600

while owing > 0:
    n+=1
    interest_amount = owing * vr
    owing -=  (payment - interest_amount)
    owing_list.append(owing)
    print(owing)

print("Months: ")
print(n)
print("Total paid: ")
print(n*payment)