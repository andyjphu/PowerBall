import csv, random; 

with open("lot.csv", "r") as f:
    reader = csv.reader(f)
    non_powerball_values = []
    powerball_values = []
    
    first_row = True
    
    for row in reader:
        if first_row: 
            first_row = False
            continue


        for col, values in enumerate(row):
            if col == 1:
                values_array = values.split(" "); 
                non_powerball_values += values_array[0:5]
                powerball_values.append(values_array[5])
    

random_ticket = [random.choice(non_powerball_values) for i in range(5)] + [random.choice(powerball_values)]

print(random_ticket);