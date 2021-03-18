from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from patient.models import Patient

from .serializer import PatientSerializer, RegisterUserSerializer


#Display all patient records or create a new patient record
'''
class PatientList(APIView):

    def get(self, request):
        patient = Patient.objects.all()
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)
'''

#view all
@api_view(['GET',])
def api_patient_list(request):
    try:
        patient = Patient.objects.all()
    except Patient.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        serializer = PatientSerializer(patient, many=True)
        return Response(serializer.data)

#updare one
@api_view(['PUT',])
def api_patient_update(request, patient_id):
    try:
        patient = Patient.objects.get(pk = patient_id)
    except Patient.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND) 

    if request.method == 'PUT':
        serializer = PatientSerializer(patient, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "updated successfully!!!"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#delete one
@api_view(['DELETE',])
def api_patient_delete(request, patient_id):
    try:
        patient = Patient.objects.get(pk = patient_id)
    except Patient.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND) 

    if request.method == 'DELETE':
        operation = patient.delete()
        data = {}
        if operation:
            data["success"] = "deleted successfully!!!"
        else:
            data["error"] = "delete failed!!!"
        return Response(data=data)

#create one
@api_view(['POST',])
def api_patient_create(request):
    #user = User.objects.get(pk=1)

    patient = Patient()

    if request.method == 'POST':
        serializer = PatientSerializer(patient, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST',])
def api_register_user(request):

    if request.method == 'POST':
        serializer = RegisterUserSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "New patient registered! "
        else:
            data = serializer.errors
        return Response(data)