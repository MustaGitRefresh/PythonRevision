# calculate the rent with the net amount

net_amt = 800000
total_rent = 0
months = 11
rent = 15000
rents = 0
incremented_rent = rent*0.1
while True:
    total_rent += (rent + (incremented_rent)) * months
    if total_rent > net_amt:
        rents += 1
        rent += incremented_rent
        incremented_rent = rent * 0.1
        print('{} year system'.format(rents))
        print(rent)
        print(total_rent)
    else:
        break

print(rents)
