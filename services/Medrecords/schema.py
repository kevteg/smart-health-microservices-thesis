from graphene_django import DjangoObjectType
from Medrecords.models import Record, Patient
import graphene

class RecordType(DjangoObjectType):
    class Meta:
        model = Record


class PatientType(DjangoObjectType):
    class Meta:
        model = Patient


class Query(graphene.ObjectType):
    records = graphene.List(RecordType)
    patients = graphene.List(PatientType)

    def resolve_records(self, info):
        return Record.objects.all()

    def resolve_patients(self, info):
        return Patient.objects.all()

schema = graphene.Schema(query=Query)
