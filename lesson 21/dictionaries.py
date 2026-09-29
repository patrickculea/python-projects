student_data = {
    "id1":{"name":"Hannah","class":"V","subject":"english,maths,science"},
    "id2":{"name":"John","class":"V","subject":"english,maths,science"},
    "id3":{"name":"Hannah","class":"V","subject":"english,maths,science"},
    "id4":{"name":"Dave","class":"V","subject":"english,maths,science"}
}

result = {}
seen_keys = []

for s_id,details in student_data.items():
    unique_key = (details["name"],details["class"],details["subject"])

    if unique_key not in seen_keys:
        uniques_key = (details["name"], details["class"], details["subject"])

for k,v in result.items():
    print(k, ":", v)