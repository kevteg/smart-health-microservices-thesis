from graphene_django import DjangoObjectType
from Metadata.models import Doctor, Center, Ambulance
import graphene

class DoctorType(DjangoObjectType):
    class Meta:
        model = Doctor


class CenterType(DjangoObjectType):
    class Meta:
        model = Center


class AmbulanceType(DjangoObjectType):
    class Meta:
        model = Ambulance


class Query(graphene.ObjectType):
    doctors = graphene.List(DoctorType)
    centers = graphene.List(CenterType)
    ambulances = graphene.List(AmbulanceType)

    def resolve_doctors(self, info):
        return Doctor.objects.all()

    def resolve_centers(self, info):
        return Center.objects.all()

    def resolve_ambulances(self, info):
        return Ambulance.objects.all()

schema = graphene.Schema(query=Query)
