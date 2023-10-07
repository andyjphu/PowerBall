import quantumrandom, time
# print()
# for i in range(5):
#     int(print(quantumrandom.randint(1,69), end=""))
#     time.sleep(1)    
    
# print(int(quantumrandom.randint(1,26), end=""))
# print()\
print("need to wait 60 seconds between requests")
time.sleep(60)
print("wait complete")
print()
f = quantumrandom.get_data(data_type='uint16', array_length=6*5)

print(f) 

ctr = 0
for item in f:
    if ctr < 5:
        print(item%70, end=" ")
        ctr+=1
    else:
        print(item%27) #if 26, will get zero,. now 27 and 0 = 0 
        ctr = 0

print()