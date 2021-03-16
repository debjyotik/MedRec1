from rest_framework import serializers

from patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        #fields = ('patient_fname' , 'patient_lname' , 'age', 'gender', 'ailment', 'patient_report')
        fields = '__all__'