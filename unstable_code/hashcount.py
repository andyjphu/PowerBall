import csv, collections
from matplotlib import pyplot as plt

hashcount = collections.defaultdict(int)
powerball = collections.defaultdict(int)

with open("lot.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        if row == ["Draw Date","Winning Numbers","Multiplier"]:
            continue


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
                e = val.split(" ")
                for key, item in enumerate(e):
                    if (key) < 5:
                        hashcount[item] += 1
                    else:
                        print(e)
                        powerball[item] += 1

print(hashcount)

hashcount = dict(sorted(hashcount.items(), key=lambda x:x[0]))
powerball = dict(sorted(powerball.items(), key=lambda x:x[0]))


plt.plot(list(hashcount.keys()), list(hashcount.values()))

#print(hashcount.keys())


plt.xlabel('number')
plt.ylabel('times called)')
plt.title('times number called')
plt.show()


plt.plot(list(powerball.keys()), list(powerball.values()))

#print(hashcount.keys())


plt.xlabel('number')
plt.ylabel('times called)')
plt.title('times number called (PB)')
plt.show()