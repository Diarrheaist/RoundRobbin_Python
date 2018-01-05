import csv
import Queue

MaxTime = 300
ContextSwitch = 0

class Process: # Definining Process
    def __init__(self, pid, arrival, burst):
        self.pid = pid
        self.arrival = arrival
        self.burst = burst
    def __str__(self):
        return '|ID:{:3d}| Arrival Time:{:3d}| Burst Time:{:3d}|'.format(self.pid,self.arrival,self.burst)


class Simulator:
    def __init__(self, tq):
        self.quantum = tq
        self.clock = 0
        
        self.list = []
        self.ProcessQueue = Queue.Queue()
        self.RunQueue = Queue.Queue()

    def ProcessAdd(self, pid, arrival, burst):
        process = Process(pid, arrival, burst)
        self.list.append(process)

    def Check(self, clock):
        for process in self.list:
                if process.arrival == self.clock:
                    self.ProcessQueue.put(process)
                    break

    def Scheduling(self):
        self.timer = 0
        turn = []
        wait = []
        resp = []
        tid = []
        for process in self.list:
                if process.arrival == self.clock:
                    self.ProcessQueue.put(process)
                    break
        while self.clock < MaxTime:
            self.clock = self.clock + 1
            self.Check(self.clock)
            if not self.ProcessQueue.empty():
                process = self.ProcessQueue.get()
                burtemp = process.burst
               
                if(process.burst < self.quantum):
                    self.timer = self.timer + process.burst
                    bur = process.burst
                    process.burst = 0
                    
                    print('|ID:{:3d}| Start:{:3d}| End:{:3d}| Time Left:{:3d}| Turn Around Time:{:3d}| Waiting Time:{:3d}| Response Time:{:3d}'.format(process.pid, self.timer - bur, self.timer, process.burst,self.timer-process.arrival,(self.timer-process.arrival)-burtemp,(self.timer - bur)-process.arrival))
                    turn.append(self.timer-process.arrival)
                    wait.append((self.timer-process.arrival)-burtemp)
                    resp.append((self.timer - bur)-process.arrival)
                    tid.append(process.pid)
                else:
                    process.burst = process.burst - self.quantum
                    print('|ID:{:3d}| Start:{:3d}| End:{:3d}| Time Left:{:3d}| Turn Around Time:{:3d}| Waiting Time:{:3d}| Response Time:{:3d}'.format(process.pid, self.timer, self.timer + self.quantum, process.burst,(self.timer+self.quantum)-process.arrival,((self.timer+self.quantum)-process.arrival)-burtemp,self.timer-process.arrival))
                    turn.append((self.timer+self.quantum)-process.arrival)
                    wait.append(((self.timer+self.quantum)-process.arrival)-burtemp)
                    resp.append(self.timer-process.arrival)
                    tid.append(process.pid)
                    self.timer = self.timer + self.quantum
                    
            self.clock = self.clock + 1
            self.Check(self.clock)

            
            if not process.burst <= 0:
                self.ProcessQueue.put(process)
        print("----------------------------------------------------------------------------------------------------------------------------------------------")
        print('| Average Turn Around Time:{:.2f} | Average Waiting Time:{:.2f} | Average Response Time:{:.2f} | Utilization:{:.2f} | Throughput:{:.2f}'.format(sum(turn)/len(turn),sum(wait)/len(wait),sum(resp)/len(resp),self.timer/(self.timer + ((len(turn)-1)*0.1)),len(set(tid))/(self.timer + ((len(turn)-1)*0.1))))
