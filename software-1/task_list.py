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
    def __init__(self, tasks=None):
        if tasks == None:
            tasks = []
        self.tasks = tasks

    def append(self, task):
        self.tasks.append(task)

    # Not needed in homework.
    def extend(self, task_list):
        self.tasks.extend(task_list.tasks)

    def add_task(self, name, priority=0):
        self.append(Task(name, priority))

    # Return n-th task
    def get_by_index(self, index):
        if index < 1:
            print("Error.")  # To be fixed.
            sys.exit(1)

        return self.tasks[index - 1]

    # Return task whose name is 'name'
    def get_by_name(self, name):
        task_list = [t for t in self.tasks if t.name == name]

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
        for (i, task) in enumerate(self.tasks):
            print("%2d:\t%3d\t%s" % (i+1, task.priority, task.name))

    # Save task list to CSV file
    def save_csv(self, file):
        with open(file, "w") as f:
            for t in self.tasks:
                f.write(t.name + ',' + str(t.priority) + '\n')

    # Load task list from CSV file
    def load_csv(self, file):
        self.clear()
        with open(file, "r") as f:
            for line in f:
                (name, priority) = line.rstrip('\r\n').split(",")
                self.add_task(name, int(priority))

    # Empty task list
    def clear(self):
        self.tasks = []

    # Remove n-th task
    def rm_by_index(self, index):
        if index < 1:
            print("Error.")  # To be fixed.
            sys.exit(1)

        self.tasks.pop(index - 1)

    # Remove tasks whose name is 'name'
    def rm_by_name(self, name):
        task_list = [t for t in self.tasks if t.name != name]

        self.tasks = task_list


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


    print("# 1st task")
    task_list.get_by_index(1).print()
    print("# change priority")
    task_list.get_by_index(1).set_priority(5)
    task_list.get_by_index(1).print()

    print()
    print("# show a task named 'fizz'")
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

