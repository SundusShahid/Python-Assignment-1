burst_time=[]
print("Enter the number of processes: ")
n=int(input())
print("Enter burst time foe each process: \n")
burst_time=list(map(int, input().split()))
waiting_time=[]
avg_wait_time=0
turnaround_time=[]
avg_turnaround_time=0
waiting_time.insert(0,0)
turnaround_time.insert(0,burst_time[0])

for i in range(1, len(burst_time)):	
	waiting_time.insert(i, waiting_time[i-1] + burst_time[i-1])
	turnaround_time.insert(i, waiting_time[i] + burst_time[i])
	avg_wait_time+=waiting_time[i]
	avg_turnaround_time+=turnaround_time[i]
avg_wait_time=float(avg_wait_time)/n
avg_turnaround_time=float(avg_turnaround_time)/n

print("\n")
print("Processes\t  Burst Time\t  Waiting TIme\t  TUrnaround Time\t")

for i in range(0,n):
	print(str(i) + "\t\t" + str(burst_time[i]) + "\t\t" + str(waiting_time[i]) + "\t\t" + str(turnaround_time[i]))
	print("\n")

print("Average waiting time: " +str(avg_wait_time))
print("Average turnaround time: " +str(avg_turnaround_time))
