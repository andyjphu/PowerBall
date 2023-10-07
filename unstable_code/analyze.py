import csv

with open("lot.csv", "r") as f:
    reader = csv.reader(f)
    
    for row in reader:

        for ctr, val in enumerate(row):
            # print("ctr", ctr)
            # if ctr == 0:
            #     pass
            # elif ctr < 5: 
            #     print(val)
            # else:
            #     print("multiplier")

            if ctr == 0:
                pass
            if ctr== 1:
                print(val.split(" "))
            
            if ctr==2:
                print("mult", val)