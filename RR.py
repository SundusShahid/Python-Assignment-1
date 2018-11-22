count=0
j=0
time=0
remain=0
flag=0
time_quantum=0
wait_time=0
turnaround_time=0
at=[10]
bt=[10]
rt=[10]
print("Enter no of processes: ")
n=int(input())
remain=n

for i in range(0, count<n):
	print("Enter arrival time and burst time for process no: ")
	at.insert(i,at[i])
	bt.insert(i,bt[i])
	rt[i]=bt[i]

print("ENter quantum time:\t")
time_quantum=int(imput())
print("\n")
print("Processes\t Burst Time\t Turnaround TIme\t Waiting Time\t")

time=0
count=0
for i in range(0, remain!=0):
	if(rt[count]<=time_quantum):
		if(rt[count]>0):
			time+=rt[count]
			rt[count]=0
			flag=1
	else if(rt[count]>0):
		rt[count]-=time_quantum
		time+=time_quantum
	
	if(rt[count]==0):
		if(flag==1):
			remain--	
			print(count+1 "    ")
			print(time-at[count] "
			print(time-at[count]-bt[count])
			wait_time+=time-at[count]-bt[count]
			turnaround_time+=time-at[count]
			flag=0

	if(count==n-1):
		count=0
	else if(at[count]<=time):
		count++
	else:
		count=0

print("Average waiting time: "wait_time*1.0/n)
print("Average turnaround time: " turnaround_time*1.0/n)



	











