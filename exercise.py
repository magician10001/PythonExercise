class Student:
    stu_num = 0
    stu_list = []

    def __init__(self, name, number, score_cn, score_os):
        self.name = name
        self.number = number
        self.score_cn = score_cn
        self.score_os = score_os
        self.rank = 0
        Student.stu_num = Student.stu_num+1
        Student.stu_list.append(self)

    @property
    def score_total(self):
        return self.score_cn+self.score_os

    def show_stu_info(self):
        print("Name:%s Number:%s CN Score:%d OS Score:%d Total Score:%d Rank:%d" % (self.name, self.number, self.score_cn, self.score_os, self.score_total, self.rank))

    def modname(self):
        self.name = input("Enter a new name:")

    def show_number(self):
        print(self.number)
        return self.number

    @classmethod
    def show_stu_num(cls):
        print("There are %d students" % Student.stu_num)

    @classmethod
    def sort(cls):
        i = 1
        Student.stu_list.sort(key=lambda x: x.score_total, reverse=True)
        for stu in Student.stu_list:
            stu.rank = i
            stu.show_stu_info()
            i = i+1


class Teacher:
    teacher_num = 0

    def __init__(self, name, number):
        self.name = name
        self.number = number
        Teacher.teacher_num = Teacher.teacher_num + 1

    @classmethod
    def show_num(cls):
        print("There are %d teachers" % cls.teacher_num)

    def show_info(self):
        print("Name:%s Number:%s" % (self.name, self.number))

    def modify(self, stu):
        stu.score_os = int(input("输入%s新的操作系统成绩：" % stu.name))
        stu.score_cn = int(input("输入%s新的计算机网络成绩：" % stu.name))


class Professor(Teacher):
    prof_num = 0

    def __init__(self, name, number, experience):
        super().__init__(name, number)
        self.experience = experience
        Professor.prof_num = Professor.prof_num+1

    @classmethod
    def show_num(cls):
        print("There are %d professors and %d teachers(including professors)" % (cls.prof_num, cls.teacher_num))

    def show_info(self):
        print("Name:%s Number:%s Experience:%d" % (self.name, self.number, self.experience))

    def modify(self, stu):
        stu.score_os = int(input("输入%s新的操作系统成绩：" % stu.name))
        stu.score_cn = int(input("输入%s新的计算机网络成绩：" % stu.name))


teacher1 = Teacher("Spike", "10021")
teacher2 = Teacher("Snoopy", "10034")
professor1 = Professor("Alex", "10045", 15)
professor2 = Professor("Bob", "10075", 20)
stu1 = Student("William", "2022132", 95, 86)
stu2 = Student("Jackie", "2022135", 85, 75)
stu3 = Student("Frank", "2022145", 98, 87)
Student.show_stu_num()
Teacher.show_num()
professor1.show_info()
Professor.show_num()
Student.sort()
teacher1.modify(stu1)
professor2.modify(stu2)
Student.sort()
