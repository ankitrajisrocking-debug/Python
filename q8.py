import numpy as np

students = np.array(["S1", "S2", "S3", "S4", "S5"])


mid = np.array([
	[65, 70, 68, 72],
	[78, 75, 80, 77],
	[55, 60, 58, 62],
	[82, 85, 80, 88],
	[70, 68, 72, 74]
])


end = np.array([
	[72, 78, 75, 80],
	[84, 82, 86, 83],
	[65, 68, 66, 70],
	[88, 90, 85, 92],
	[78, 75, 80, 82]
])

mid_total = np.sum(mid, axis = 1)
end_total = np.sum(end, axis = 1)

mid_average = np.mean(mid, axis= 1)
end_average = np.mean(end, axis = 1)

improvement = ( (end_total - mid_total) / mid_total ) * 100

print("Student Mid Total End Total Mid Average End Average Improvement(%)")
print("-" * 75)

for i in range(len(students)):
	print(f"{students[i]:<8} {mid_total[i]:<10} {end_total[i]: <10}" f"{mid_average[i]:<12.2f} {end_average[i]:<12.2f}" f"{improvement[i]:.2f}")
	
