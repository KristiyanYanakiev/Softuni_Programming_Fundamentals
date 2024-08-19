list_of_people = [int(s) for s in input().split(" ")]
k_person = int(input())
index_of_k_person = list_of_people.index(k_person)

initial_length = len(list_of_people)
index_of_executed_person = index_of_k_person
number_of_skipped_people = len(list_of_people[:index_of_k_person])


starting_index = index_of_executed_person

executed_people = []

while len(executed_people) < initial_length:
    executed_people.append(list_of_people[starting_index % len(list_of_people)])
    list_of_people.remove(list_of_people[starting_index % len(list_of_people)])
    list_of_people.insert(starting_index % len(list_of_people), 5)
    starting_index += number_of_skipped_people

print(executed_people)









































