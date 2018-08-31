import sys
import os

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
        self.file = ""
        self.modified = False

    def append(self, task):
        self.tasks.append(task)
        self.modified = True

    # Not needed in homework.
    def extend(self, task_list):
        self.tasks.extend(task_list.tasks)
        self.modified = True

    def add_task(self, name, priority=0):
        self.append(Task(name, priority))
        self.modified = True

    # Return n-th task
    def get_by_index(self, index):
        if index < 1:
            print("Error.")  # To be fixed.
            sys.exit(1)
        return self.tasks[index - 1]

    # Return task whose name is 'name'
    def get_by_name(self, name):
        filtered_tasks = [t for t in self.tasks if t.name == name]
        return filtered_tasks[0]

    def get_sorted(self):
        sorted_tasks = sorted(self.tasks, key=lambda t: t.priority, reverse=True)
        return TaskList(sorted_tasks)

    # Return 'n' number of highest-priority tasks
    def get_top(self, n):
        if n < 1:
            print("Error.")  # To be fixed.
            sys.exit(1)
        top_tasks = self.get_sorted().tasks[:n]
        return TaskList(top_tasks)

    def get_top3(self):
        return self.get_top(3)

    def print(self):
        for (i, task) in enumerate(self.tasks):
            print("%2d:\t%3d\t%s" % (i+1, task.priority, task.name))

    # Save task list to CSV file
    def save_csv(self, file="", force=False):
        if os.path.exists(file) and file != self.file:
            if not force:
                print("File already exits. To overwrite it, `save_csv('%s', force=True)`" % file)
                return
        else:
            if file == "":
                file = self.file
            print("Save data to '%s'" % file)

        with open(file, "w") as f:
            for t in self.tasks:
                f.write(t.name + ',' + str(t.priority) + '\n')
        self.file = file
        self.modified = False

    # Load task list from CSV file
    def load_csv(self, file, force=False):
        if not os.path.exists(file):
            print("'%s' does not exit." % file)
            return

        if self.modified and not force:
            print("Task list has been modified. To discard the change, `load_csv('%s', force=True)`" % file)
            return

        print("Load data from '%s'" % file)
        self.clear()
        with open(file, "r") as f:
            for line in f:
                (name, priority) = line.rstrip('\r\n').split(",")
                self.add_task(name, int(priority))
        self.file = file
        self.modified = False

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
        filtered_tasks = [t for t in self.tasks if t.name != name]
        self.tasks = filtered_tasks


# Test code
def main():
    # Initialize
    task_list = TaskList()
    task_list.add_task("foo")
    task_list.add_task("bar", 10)
    print("# task_list")
    task_list.print()
    print()

    task_list2 = TaskList()
    task_list2.append(Task("fizz"))
    task_list2.append(Task("buzz", 3))
    print("# task_list2")
    task_list2.print()
    print()

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
    print("# Sorted tasks")
    task_list.get_sorted().print()

    print()
    print("# Top 2")
    task_list.get_top(2).print()

    print()
    print("# Top 3")
    task_list.get_top3().print()


if __name__ == "__main__":
    main()

