class Course():
	def __init__(self, id, name):
		self.id = id
		self.name = name

class Class():
	def __init__(self, id, name, course_ids):
		self.id = id
		self.name = name
		self.course_ids = course_ids


class Lecturer():
	def __init__(self, id, name, course_ids):
		self.id = id
		self.name = name
		self.course_ids = course_ids

course_dict = {}
with open("input.txt", "r") as f:
	lines = f.readlines()
	i = 0
	while(i<len(lines)):
		lines[i] = lines[i][:-1]
		print("i=",i)
		if lines[i] == "Courses":
			i+=1
			number_of_courses = int(lines[i][:-1])
			i+=1
			for j in range(i, i+number_of_courses):
				id, name = lines[j][:-1].split(" ", 1)
				course_dict[j] = Course(id, name)
			i += number_of_courses
		else:
			i+=1
		

		