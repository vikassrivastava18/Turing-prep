# Valid anagram

def valid_anagram(a: str, b: str):
    return sorted(a) == sorted(b)

print(valid_anagram("aab", "baa"))
print(valid_anagram("papa", "appa"))
print(valid_anagram("aab", "bba"))

students = []

with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})
        
students = sorted(students, key=lambda student: (student["name"], student["house"]))

print("Result: ", students)