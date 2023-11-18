class List:
    def __init__(self):
        self.tasks = []

    def addtask(self, task):
        self.tasks.append(task)

    def remtask(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        else:
            print("Task not in list!")

    def showtask(self):
        if self.tasks:
            print("List:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Empty list!")

def main():
    WorkList = List()

    while True:
        print("\nOptions:\n1) Add a task\n2) Remove a task\n3) Show tasks\n4) Quit")

        select = input("Enter the option you want to do: ")

        if select == "1":
            task = input("Enter task: ")
            WorkList.addtask(task)
            print("Task added!")

        elif select == "2":
            task = input("Enter the task to remove: ")
            WorkList.remtask(task)

        elif select == "3":
            WorkList.showtask()

        elif select == "4":
            print("Exiting!")
            break
        else:
            print("Invalid!")

if __name__ == "__main__":
    main()