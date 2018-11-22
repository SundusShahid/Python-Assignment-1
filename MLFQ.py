burst_time=[]
print("Enter the number of processes: ")
n=int(input())
processes=[]
for i in range(0,n):
	processes.insert(i,i+1)

print("Enter burst time foe each process: \n")
burst_time=list(map(int, input().split()))


waiting_time=[]
avg_wait_time=0
turnaround_time=[]
avg_turnaround_time=0
waiting_time.insert(0,0)
turnaround_time.insert(0,0)


print("Enter slice time for 1st queue RR: ")
RR_queue1=int(input())
print("Enter slice time for 2nd queue RR: ")
RR_queue2=int(input())
print("Enter slice time for 3rd queue FCFS: ")
FCFS_queue3=int(input())
time=0;
remaining_time=[]


#queue 1 RR
for i in range(0,len(burst_time)):
	if(burst_time[i]<=RR_queue1):
		waiting_time.insert(i, time)
		time+=burst_time[i]
		turnaround_time.insert(i, time)
		
		remaining_time.insert(i,0)
		
	else:
		waiting_time.insert(i, time)
		time+=RR_queue1
		remaining_time.insert(i,burst_time[i]-RR_queue1)

#QUEUE 2 RR	
for i in range(0,n):
	
	if(remaining_time[i]!=0):
		
		if(remaining_time[i] <=RR_queue2):
			time+=remaining_time[i]
			turnaround_time.insert(i, time)		
			remaining_time.insert(i,0)
		
		else:
			time+=RR_queue2
			remaining_time.insert(i,remaining_time[i]-RR_queue2)

#QUEUE 3 FCFS
for i in range(0,len(burst_time)):
	if(remaining_time[i]!=0):
		time+=remaining_time[i]
		turnaround_time.insert(i, time)
		
	
# CALCUTAE AVG WAITING TIME AND TURNAROUND TIME		
for i in range(0,len(burst_time)):	
	avg_wait_time+=waiting_time[i]
	avg_turnaround_time+=turnaround_time[i]


avg_wait_time=float(avg_wait_time)/n
avg_turnaround_time=float(avg_turnaround_time)/n
print("\n")
print("Processes\t  Burst Time\t  Waiting TIme\t  TUrnaround Time\t")

for i in range(0,n):
	print(str(processes[i]) + "\t\t" + str(burst_time[i]) + "\t\t" + str(waiting_time[i]) + "\t\t" + str(turnaround_time[i]))
	print("\n")

print("Average waiting time: " +str(avg_wait_time))
print("Average turnaround time: " +str(avg_turnaround_time))

