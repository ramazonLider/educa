from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('register/', cache_page(60 * 15)(views.StudentRegistrationView.as_view()), name='student_registration'),
    path('enroll-course/', cache_page(60 * 15)(views.StudentEnrollCourseView.as_view()), name='student_enroll_course'),
]
