import uuid
import pandas as pd

from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import EmailMessage

from .models import Applicant, Skill, Job, Experience, Qualification
from .serializers import SkillSerializers, JobSerializers, ApplicantSerializers, ExperienceSerializers, \
    QualificationsSerializers

from .models import Recruiter
from .serializers import RecruiterSerializers
from rest_framework.permissions import AllowAny
from .serializers import CompanySerializers

from .models import Company
from rest_framework.viewsets import ModelViewSet


# Create your views here.
class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    permission_classes = [AllowAny]


class RecruiterViewSet(ModelViewSet):
    queryset = Recruiter.objects.all()
    serializer_class = RecruiterSerializers
    permission_classes = [AllowAny]


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializers
    permission_classes = [AllowAny]


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializers
    permission_classes = [AllowAny]



    # def create(self, request, *args, **kwargs):
    #     User = request.User
    #     Job.object.create(posted_by=User)


class Excel(APIView):
    def get(self, request, *args, **kwargs):
        job_objs = Job.objects.all()
        sreializers = JobSerializers(job_objs, many=True)
        df = pd.DataFrame(sreializers.data)
        print(df)
        data1 = df.to_csv(f"static/{uuid.uuid4()}.csv", encoding="UTF-8")
        subject = "WELCOME"
        from_mail = "ramshankar413@gmail.com"
        to_mail = "tej578@gmail.com"
        mail = EmailMessage(subject,data1,from_mail,[to_mail])
        mail.attach_file('C:\\Users\\ADMIN\\Downloads\\Job-2022-11-26 (3).csv')
        mail.send()
        return Response(data1,status=status.HTTP_200_OK)


# from django.core.mail import send_mail, EmailMessage
#
# send_mail(
#     'Texting mail',
#     'Here is the message',
#     'ramshankar413@gmail.com',
#     ['ramshankar413@gmail.com'],
#     fail_silently=False,
# )


class ApplicantViewSet(ModelViewSet):
    queryset = Applicant.objects.all()
    serializer_class = ApplicantSerializers
    permission_classes = [AllowAny]


class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializers
    permission_classes = [AllowAny]


class QualificationViewSet(ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationsSerializers
    permission_classes = [AllowAny]
