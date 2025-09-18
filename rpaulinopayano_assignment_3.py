# Personal Information Storage (Strings)
full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

# Academic Data Organization (Lists)
current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = [3, 3, 3, 3]
gpa_history = [3.2, 3.6, 3.4, 3.7]

# Contact Information Storage (Tuples)
emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", 28202)
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", 5, 22, 2006)

#Interest Tracking (Sets)
current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

# Organizational Mapping (dictionary key-value pairs)
course_credits = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

#Required Calculations
total_current_credits = sum(credit_hours)
cumulative_gpa = round(sum(gpa_history) / (len(gpa_history)), 2)
count_completed_courses = len(completed_courses)
total_weekly_study = sum(study_hours_per_subject.values())
academic_load = sum(credit_hours) + total_weekly_study
monthly_budget_total = sum(monthly_budget.values())
daily_food_budget = round((monthly_budget["Food"] / 30), 2)
annual_budget = sum(monthly_budget.values()) * 12
study_cost_per_hour = round((monthly_budget["Books"] / total_weekly_study), 2)

#Analytics Calculations
total_followers = instagram_info[2] + twitter_info[2]
current_skills_count = len(current_skills)
learning_skills_count = len(skills_to_learn)
contact_directory_size = len(contact_directory)
entertainment_backlog_size = len(entertainment_backlog)
academic_assessment = 1

# formatted output
print("================================================================")
print("              PERSONAL ACADEMIC & LIFE PORTFOLIO                ")
print("================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}")
print()
print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_current_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_weekly_study} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour")
print()
print("Current Courses:")
print(f"{current_courses[0]} - {course_credits["COMP 163"]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_courses[1]} - {course_credits["MATH 150"]} credits - {course_professors["MATH 150"]} - {course_rooms["MATH 150"]}")
print(f"{current_courses[2]} - {course_credits["ENG 101"]} credits - {course_professors["ENG 101"]} - {course_rooms["ENG 101"]}")
print(f"{current_courses[3]} - {course_credits["HIS 105"]} credits - {course_professors["HIS 105"]} - {course_rooms["HIS 105"]}")
print()
print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {current_skills_count}")
print(f"Skills Want to Learn: {learning_skills_count}")
print()
print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${monthly_budget_total}")
print(f"Food: ${monthly_budget["Food"]} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget["Entertainment"]}")
print(f"Books: ${monthly_budget["Books"]}")
print(f"Transportation: ${monthly_budget["Transportation"]}")
print(f"Annual Projection: ${annual_budget}")
print()
print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]}, {home_address[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {contact_directory_size} people in directory")
print()
print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {count_completed_courses}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {entertainment_backlog_size} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")


