from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    registration_no = models.CharField(max_length=100, unique=True)
    cnic = models.CharField(max_length=100, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['registration_no', 'cnic']),
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Class(models.Model):
    semester = models.IntegerField()
    year = models.IntegerField()
    shift = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['year', 'semester']),
        ]

    def __str__(self):
        return f"{self.year} - Semester {self.semester}"


class Subject(models.Model):
    sub_name = models.CharField(max_length=100)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.teacher_name


class FeeVoucher(models.Model):
    amount = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['amount']),
        ]

    def __str__(self):
        return f"Fee Voucher: {self.amount}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    related_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    GPA = models.CharField(max_length=100)

    class Meta:
        indexes = [
            models.Index(fields=['GPA']),
        ]

    def __str__(self):
        return f"Result for {self.student}"


class ClassRoom(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_room = models.ForeignKey(Class, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['class_room']),
        ]

    def __str__(self):
        return f"Classroom for {self.student}"
