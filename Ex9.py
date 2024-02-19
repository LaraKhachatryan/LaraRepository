import random
#  List of names
names = ["Alice", "Bob", "Charlie", "David", "Eva"]
#  Initialize an empty group
group = []
#  Simulate the name selection process for each person in the group
for person in range(5):
#      Get the person's name
    person_name = input(f"Person {person + 1}, enter your name: ")
#      Remove the selected name from the list
    names.remove(person_name)
#      Randomly select a name for the person
    selected_name = random.choice(names)
#      Print the result
    print(f"{person_name} selected {selected_name}")
#      Remove the selected name from the list
    names.remove(selected_name)
#      Update the group with the selected names
    group.append((person_name, selected_name))
# Display the final group assignments
print("\nFinal group assignments:")
for assignment in group:
    print(f"{assignment[0]} - {assignment[1]}")