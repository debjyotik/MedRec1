from rest_framework import serializers

from django.contrib.auth.models import User

from patient.models import Patient

class PatientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patient
        #fields = ('patient_fname' , 'patient_lname' , 'age', 'gender', 'ailment', 'patient_report')
        fields = '__all__'


class RegisterUserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password' : {'write_only' : True},
            'password2' : {'write_only' : True},
        }

    def save(self):
        new_user = User(
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password' : 'Passwords do not match!!! '})
        new_user.set_password(password)
        new_user.save()
        return new_user