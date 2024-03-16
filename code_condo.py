# basics
address = input("Address: ")
rooms = int(input("Rooms for rent: "))

# costs
cost = int(input("Cost: "))
cost_per_month = int(input("Cost/month: "))
mbps_per_mon = 25 #xfinity
utilities = 100 #random guess

# revenue
rent = int(input("Rent: "))

# calculations
net_per_month = (rent*rooms)-(cost_per_month+mbps_per_mon+utilities) 
print(f"net/mon: ${round(net_per_month,2)}")
mons_to_own = cost/cost_per_month
yrs_to_own = mons_to_own/12
print(f"own in {round(yrs_to_own,2)} years")

# Creates spreadsheet
# Python internal csv
import csv
headers = ["Address", "Cost", "Cost/mon", "Rent", "Net/mon", "Yrs to own"]
columns = ['addr', 'cost', 'cost_per_mon', 'rent', 'net_per_mon', 'yrs_to_own']
data = [address, cost, cost_per_month, rent, net_per_month, yrs_to_own]

old = []
with open('./condos.csv', newline='') 	as f:
	for row in f:
		old.append(row)
	if len(old) <= 0:
		with open('./condos.csv', 'w', encoding="UTF8") as f:
			writer = csv.writer(f)
			writer.writerow(headers)
			writer.writerow(data)
	else:
		with open('./condos.csv', 'a', encoding="UTF8") as f:
			writer = csv.writer(f)
			writer.writerow(data)
