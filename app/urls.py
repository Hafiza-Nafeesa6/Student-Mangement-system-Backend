from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app.api.views import TeacherViewSet, StudentViewSet, SubjectViewSet, ClassViewSet, FeeVoucherViewSet, \
    ClassRoomViewSet, \
    ResultViewSet

router = DefaultRouter()

router.register(r'teacher', TeacherViewSet)
router.register(r'student', StudentViewSet)
router.register(r'subject', SubjectViewSet)
router.register(r'class', ClassViewSet)
router.register(r'fee', FeeVoucherViewSet)
router.register(r'room', ClassRoomViewSet)
router.register(r'result', ResultViewSet)

urlpatterns = [
    path('app/', include(router.urls)),
    path(r'', include('djoser.urls.jwt')),
]
