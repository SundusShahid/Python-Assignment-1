

burst_time=[]
print("Enter the number of processes: ")
n=int(input())
processes=[]
priority=[]
for i in range(0,n):
	processes.insert(i,i+1)

print("Enter burst time for each process: \n")
burst_time=list(map(int, input().split()))

print("Enter priority of each process: \n")
priority=list(map(int, input().split()))

waiting_time=[]
turnaround_time=[]
waiting_time.insert(0,0)
turnaround_time.insert(0,burst_time[0])
avg_wait_time=0
avg_turnaround_time=0

#sorting on basis of priority
for i in range(0, len(priority)-1):
	for j in range(0, len(priority)-i-1):
		if(priority[j]>priority[j+1]):
			swap=priority[j]
			priority[j]=priority[j+1]	
			priority[j+1]=swap
	
			swap=burst_time[j]
			burst_time[j]=burst_time[j+1]
			burst_time[j+1]=swap

			swap=processes[j]
			processes[j]=processes[j+1]
			processes[j+1]=swap
#................

for i in range(1, len(processes)):
	waiting_time.insert(i,waiting_time[i-1]+burst_time[i-1])
	turnaround_time.insert(i,waiting_time[i]+burst_time[i])

#calculating avergae waiting and turnaround time
for i in range(0, len(processes)):
	avg_wait_time+=waiting_time[i]
	avg_turnaround_time+=turnaround_time[i]

avg_wait_time=float(avg_wait_time)/n
avg_turnaround_time=float(avg_turnaround_time)/n
print("\n")
print("Processes\t Burst Time\t Waiting TIme\t TUrnaround Time\t")

for i in range(0,n):
	print(str(processes[i]) + "\t\t\t" + str(burst_time[i]) + "\t\t" + str(waiting_time[i]) + "\t\t" + str(turnaround_time[i]))
	print("\n")

print("Average waiting time: " +str(avg_wait_time))
print("Average turnaround time: " +str(avg_turnaround_time))

