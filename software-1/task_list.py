import sys

class Task:
    def __init__(self, name = "", priority = 0):
        self.name = name
        self.priority = priority

    def set_priority(self, priority):
        if priority <= 0:
            print("Error.")  # To be fixed.
            sys.exit(1)

        self.priority = priority

    def print(self):
        print("%s\t%d" % (self.name, self.priority))


class TaskList:
    def __init__(self):
        self.tasks = []

    def append(self, task):
        self.tasks.append(task)

    # Not needed in homework.
    def extend(self, task_list):
        self.tasks.extend(task_list.tasks)

    def add_task(self, name, priority=0):
        self.append(Task(name, priority))

    # Return n-th task
    def get_by_index(self, index):
        if index < 0:
            print("Error.")  # To be fixed.
            sys.exit(1)

        return self.tasks[index]

    # Return task whose name is 'name'
    def get_by_name(self, name):
        task_list = list(filter(lambda t:t.name == name, self.tasks))
        #task_list = [t for t in self.tasks if t.name == name]

        return task_list[0]

    # Return 'n' number of highest-priority tasks
    def get_top(self, n):
        if n < 1:
            print("Error.")  # To be fixed.
            sys.exit(1)

        top_tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=True)[:n]
        task_list = TaskList()
        for task in top_tasks:
            task_list.append(task)
        return task_list

    def get_top3(self):
        return self.get_top(3)

    def print(self):
        for t in self.tasks:
            t.print()


# Test code
def main():
    # Initialize
    task_list = TaskList()
    task_list.add_task("foo")
    task_list.add_task("bar", 10)

    task_list2 = TaskList()
    task_list2.append(Task("fizz"))
    task_list2.append(Task("buzz", 3))
    task_list.extend(task_list2)


    print("# 0-th task")
    task_list.get_by_index(0).print()
    print("# change priority")
    task_list.get_by_index(0).set_priority(5)
    task_list.get_by_index(0).print()

    task_list.get_by_name("fizz").print()
    print()
    print("# All tasks")
    task_list.print()

    print()
    print("# Top 2")
    task_list.get_top(2).print()

    print()
    print("# Top 3")
    task_list.get_top3().print()


if __name__ == "__main__":
    main()

