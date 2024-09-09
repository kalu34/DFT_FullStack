# forms.py
from django import forms

class QualificationField(forms.CharField):
    def to_representation(self, value):
        # Split the input string into individual qualifications
        qualifications = value.splitlines()
        
        # Format each qualification as a bullet point
        formatted_qualifications = [f"- {q.strip()}" for q in qualifications]
        
        # Join the formatted qualifications with newline characters
        return "\n".join(formatted_qualifications)