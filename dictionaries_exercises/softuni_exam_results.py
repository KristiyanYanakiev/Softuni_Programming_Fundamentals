def ban(some_username, some_exam_results):
    del some_exam_results[some_username]

exam_results = {}
total_submissions_per_language = {}


while True:
    command = input()

    if command == "exam finished":
        break

    command_as_list = command.split("-")

    username = command_as_list[0]

    if command_as_list[1] == "banned":
        ban(username, exam_results)
        continue
    language = command_as_list[1]
    points = int(command_as_list[2])

    if language not in total_submissions_per_language.keys():
        total_submissions_per_language[language] = 0
    total_submissions_per_language[language] += 1


    if username in exam_results.keys():
        if language in exam_results[username]:
            if points > exam_results[username][1]:
                exam_results[username] = [language, points]
    else:
        exam_results[username] = [language, points]

print("Results:")
for key, value in exam_results.items():
    print(f"{key} | {value[1]}")
print("Submissions:")
for language, submissions in total_submissions_per_language.items():
    print(f"{language} - {submissions}")








