chat_logger = []

while True:
    command = input()

    if command == "end":
        break

    command_as_list = command.split()
    action = command_as_list[0]
    message = command_as_list[1]

    if action == "Chat":
        chat_logger.append(message)
    elif action == "Delete":
        if message in chat_logger:
            chat_logger.remove(message)
        else:
            continue

    elif action == "Edit":
        edited_version = command_as_list[2]
        if message in chat_logger:
            chat_logger[chat_logger.index(message)] = edited_version
        else:
            continue

    elif action == "Pin":
        if message in chat_logger:
            chat_logger.append(message)
            chat_logger.remove(message)
        else:
            continue

    elif action == "Spam":
        chat_logger = [chat_logger.append(element) for element in command_as_list if element != "Spam"]

print(chat_logger)
