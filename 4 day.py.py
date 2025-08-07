#1.Lambda, Map, and Filter

order_ids = [101, 102, 103, 104, 105]

#Filter only odd order IDs
odd_orders = list(filter(lambda x: x % 2 != 0, order_ids))

#Double the points for these odd order IDs
doubled_points = list(map(lambda x: x * 2, odd_orders))

print("Odd Order IDs:", odd_orders)
print("Doubled Points for Odd Orders:", doubled_points)

#2.Zip & Unzip Lists

students = ["shiva", "Dharun", "Mahi", "Jai"]
scores = [85, 92, 78, 88]

#Combine using zip
combined = list(zip(students, scores))

#Enumerate to index each student
for index, (name, score) in enumerate(combined, start=1):
    print(f"{index}. {name} - {score} points")

#Sort by scores (2nd item of tuple)
sorted_students = sorted(combined, key=lambda x: x[1], reverse=True)
print("\n🎓 Sorted by Score (High to Low):")
for name, score in sorted_students:
    print(f"{name}: {score}")

#2.Sorting

students = ["Ragu", "Meena", "Ranjini", "Madhan"]
scores = [85, 92, 78, 88]

#Combine using zip
combined = list(zip(students, scores))

#Enumerate to index each student
for index, (name, score) in enumerate(combined, start=1):
    print(f"{index}. {name} - {score} points")

#Sort by scores (2nd item of tuple)
sorted_students = sorted(combined, key=lambda x: x[1], reverse=True)
print("\n🎓 Sorted by Score (High to Low):")
for name, score in sorted_students:
    print(f"{name}: {score}")

