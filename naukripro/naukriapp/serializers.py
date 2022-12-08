from naukriapp.models import Recruiter, Skill, Job, Applicant, Experience, Qualification
from rest_framework.serializers import ModelSerializer

from .models import Company


class CompanySerializers(ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'location', 'date_of_start', 'description')


class RecruiterSerializers(ModelSerializer):
    company = CompanySerializers(read_only=True)

    class Meta:
        model = Recruiter
        fields = "__all__"


class SkillSerializers(ModelSerializer):
    class Meta:
        model = Skill
        fields = ("__all__")


class JobSerializers(ModelSerializer):
    skills = SkillSerializers(read_only=True)
    company = CompanySerializers(read_only=True)

    class Meta:
        model = Job
        fields = ("__all__")
        # ('id','city','title','job_description',' max_salary','min_salary','employment_type',
        #       'max_experience','min_experience','company','location',' industry_type',
        #       'skills',' posted_by')


class ApplicantSerializers(ModelSerializer):
    job = JobSerializers(read_only=True)
    recruiter = RecruiterSerializers(read_only=True, many=True)

    class Meta:
        model = Applicant
        fields = ("__all__")


class ExperienceSerializers(ModelSerializer):
    applicant = ApplicantSerializers(read_only=True, many=True)

    class Meta:
        model = Experience
        fields = ("__all__")


class QualificationsSerializers(ModelSerializer):
    applicant = ApplicantSerializers(read_only=True)

    class Meta:
        model = Qualification
        fields = "__all__"
