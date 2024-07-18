def show_message(message_list, sent_messages):
    while message_list:
        current_list = message_list.pop()
        print(f"{current_list}")
        sent_messages.append(current_list)


def send_message(sent_messages):
    print("已经发送的消息：")
    for sent_message in sent_messages:
        print(sent_message)


message_list = ['hello', 'nihao', 'wadaxi']
sent_messages = []

show_message(message_list[:], sent_messages)
send_message(sent_messages)
print(message_list)
