from rest_framework import serializers
from .models import LoanRequest

class LoanRequestSerializer(serializers.ModelSerializer):

    loan_status = serializers.CharField(read_only=True)

    class Meta:
        model = LoanRequest
        fields = ['id', 'dni', 'full_name', 'gender', 'email', 'amount', 'created_at', 'loan_status']
        read_only_fields = ['created_at']

    def create(self, validated_data):
        loan_status = validated_data.pop('loan_status', None)
        instance = super().create(validated_data)

        if loan_status is not None:
            instance.loan_status = loan_status
            instance.save()
        
        return instance
