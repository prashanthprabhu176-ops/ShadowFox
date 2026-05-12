friends = ["Archana Nayak", "Mahesh Nayak", "Ashwini Nayak", "Praveen Shenoy","Vidya Pai"]

friends_with_length = []

for name in friends:
    friends_with_length.append(((name, len(name)))) #tuple with name and length of name
print(friends_with_length)