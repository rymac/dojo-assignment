class Task:
    def __init__(self, name = "", priority = 0):
        self.name = name
        self.priority = priority

    def set_priority(self, priority):
        self.priority = priority

    def print(self):
        print("%s\t%d" % (self.name, self.priority))


class TaskList:
    def __init__(self, tasks=[]):
        self.tasks = tasks

    def append(self, task):
        self.tasks.append(task)

    def extend(self, task_list):
        self.tasks.extend(task_list)

    def add_task(self, name, priority=0):
        self.append(Task(name, priority))

    # Get n-th task
    def get(self, n):
        if n < 0:
            print("Error.")  # To be fixed.

        return self.tasks[n]

    def get_top(self, n):
        return TaskList(sorted(self.tasks, key=lambda t: t.priority, reverse=True)[:n])

    def get_top3(self):
        return self.get_top(3)

    def print(self):
        for t in self.tasks:
            t.print()


def main():
    # test code

    task_list = TaskList()
    task_list.add_task("foo")
    task_list.add_task("bar", 10)
    task1 = Task("fizz")
    task2 = Task("buzz", 2)
    task_list.extend([task1, task2])
    task3 = Task("hoge", 3)
    task_list.append(task3)

    print("# 0-th task")
    task_list.get(0).print()
    print("# change 0-th task's priority")
    task_list.tasks[0].set_priority(5)
    task_list.get(0).print()

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

