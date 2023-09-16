queue_list = []


def insert_element():
    element = int(input("Enter the element:"))
    queue_list.append(element)
    print(f"{element} is added to the queue")


def delete_element():
    if not queue_list:
        print("The queue is empty")
    else:
        e = queue_list.pop()
        print("The deleted element is", e)


def show_element():
    print(queue_list)


while True:
    print("Enter one of the following choices:\n")
    print("1.Insert\n2.Delete\n3.Show")
    choice = int(input("Enter the choice\n"))
    if choice == 1:
        insert_element()
    elif choice == 2:
        delete_element()
    elif choice == 3:
        show_element()
    else:
        exit(1)
