from Simulate import Simulator
import csv
import sys


path = sys.argv[1]
tq = int(sys.argv[2])


Simulation = Simulator(tq)

with open(path) as csvfile:
    process = csv.reader(csvfile, delimiter=',', quotechar='|')
    next(process)
    for row in process:
            pid = int(row[0])
            arrival = int(row[1])
            burst = int(row[2])
            Simulation.ProcessAdd(pid,arrival,burst)

print('---------------------------------------------\nAdding the process to the process List\n---------------------------------------------')
for process in Simulation.list:
        print(process)
print('---------------------------------------------\n Simulation \n-------------------------------------------------------------------------------------------------------------------------------------------')
Simulation.Scheduling()
print('----------------------------------------------------------------------------------------------------------------------------------------------')