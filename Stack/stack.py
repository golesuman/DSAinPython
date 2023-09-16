stack = []


def push():
    element = int(input("Enter the number:\n"))
    stack.append(element)
    print(stack)


def pop_element():
    if not stack:
        print("The stack is empty")
    else:
        e = stack.pop()
        print(f"The deleted item is {e}")
        print(stack)


while True:
    print("1.Push\n2.Pop\n3.Quit\n")
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print("You entered the wrong choice.")
