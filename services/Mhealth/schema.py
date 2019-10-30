from graphene_django import DjangoObjectType
from Mhealth.models import SmartPhoneMeta, Patient
import graphene

class SmartPhoneMetaType(DjangoObjectType):
    class Meta:
        model = SmartPhoneMeta


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient


class Query(graphene.ObjectType):
    smartphonemeta = graphene.List(SmartPhoneMetaType)
    patients = graphene.List(PatientType)

    def resolve_smart_phone_meta(self, info):
        return SmartPhoneMetaType.objects.all()

    def resolve_patients(self, info):
        return Patient.objects.all()

schema = graphene.Schema(query=Query)
