class Email:
    def __init__(self, sender, receiver, content, is_sent=False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

while True:
    command = input()

    if command == "Stop":
        break

    tokens = command.split()

    sender = tokens[0]
    receiver = tokens[1]
    content = tokens[2]

    email = Email(sender, receiver, content)
    emails.append(email)

sent_emails = [int(i) for i in input().split(", ")]

for current_index in sent_emails:
    emails[current_index].send()

for element in emails:
    print(element.get_info())



