
# views.py
from django.core.mail import send_mail, EmailMultiAlternatives
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import ContactMessage, Player
from django.conf import settings
import logging


logger = logging.getLogger(__name__)

def send_registration_email(sender_email):
    subject = 'Registration Successful'
    message = f'A user has registered with the email address: {sender_email}. Please check the dashboard for more information.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [sender_email]  # Admin email address to notify
    try:
        send_mail(subject, message, from_email, recipient_list)
        logger.info('Registration email sent successfully')
    except Exception as e:
        logger.error('Error sending registration email: ' + str(e))


@api_view(['POST'])
def save_contact_form(request):
    name = request.data.get('name')
    email = request.data.get('email')
    phone = request.data.get('phone')
    message = request.data.get('message')

    # Save form data into the database
    contact_form = ContactMessage(name=name, email=email, phone=phone, message=message)
    contact_form.save()

    send_registration_email(email)
    logger.info('Contact form saved successfully')

    return Response({'message': 'Form data saved successfully'})


@api_view(['POST'])
def save_player_data(request):
    email = request.data.get('email')
    data = request.data
    player = Player(**data)
    player.save()

    save_contact_form(request)

    return Response({'message': 'Form data saved successfully'})





