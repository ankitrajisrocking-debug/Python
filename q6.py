with open("marks.txt", "r") as infile:
	students = infile.readlines()
	
with open("res.txt" , "w") as outfile:
	for line in students:
		data = line.split()
		
		name = data[0]
		marks = list(map(int , data[1:]))
		
		total = sum(marks)
		avg = total / len(marks)
		
		if avg >= 90:
			grade = "A"
		elif avg >= 80:
			grade = "B"
		elif avg >= 80:
			grade = "C"
		elif avg >= 70:
			grade = "D"
		else:
			grade = "FAIL"
		
		outfile.write(
			f"Name: {name} , Total: {total},"
			
			f"Average: {avg: .2f}, Grade: {grade}\n"
		)
	print("Results written to res.txt")
