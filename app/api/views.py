from rest_framework import viewsets
from app.models import Student, Class, Subject, Teacher, FeeVoucher, Result, ClassRoom
from app.api.serializer import ResultSerializer, ClassRoomSerializer, FeeVoucherSerializer, TeacherSerializer, \
    SubjectSerializer, ClassSerializer, StudentSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


class FeeVoucherViewSet(viewsets.ModelViewSet):
    queryset = FeeVoucher.objects.all()
    serializer_class = FeeVoucherSerializer


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer


class ResultViewSet(viewsets.ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
