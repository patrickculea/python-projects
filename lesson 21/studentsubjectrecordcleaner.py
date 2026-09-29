student_data={
    "id1" : {"name":"Isabell","class":"9","subject":"english, math ,science"},
    "id2" : {"name":"Bella","class":"8","subject":"english ,math, coding"},
    "id3" : {"name":"anabell","class":"10","subject":"science, maths, coding"},
    "id4" : {"name":"Jack","class":"9","subject":"english, spanish, music"}}

print("")
print("Details of id1:")
print(student_data.get("id1","Not Found"))

print("")
print(student_data.get("id5","Not Found"))

student_data["id5"]={"name":"Anya","class":"V","subject":"english, art ,science"}

print("")
print("After adding id5:")
print(student_data)

student_data["id2"]["subject"]=["english, math, coding"]

print("")
print("After updating is2 subject:")
print(student_data["id2"])


cleaned_data = {}
seen_records= []

for student_id, details in student_data.items():
    unique_key =(details["name"],details["class"],details["subject"])

if unique_key not in seen_records:
    seen_records.append(unique_key)

cleaned_data[student_id] = details

student_data = cleaned_data

print("")
print("After removing duplicate records:")
print("student_data")

removed_student =student_data.pop("id4","Student not found")

print("")
print("removed_student")

print("")
print("Total student records left:",len(student_data))

print("")
print("=====FINAL STUDENT SUBJECT RECORDS =====")

for student_id,details in student_data.items():
    print(student_id,":",details)

print("======================================================================================================================================================")







              
    