from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


class EmailBackend:
    def authenticate(self , request , username , password):
        try:
            user = User.objects.get(email = username)
            if user.check_password(password):
                if request.method == 'POST':
                    message = request.POST.get('message')
                    email   = request.POST.get('email')
                    name    = request.POST.get('name')
                    send_mail(name , message , 'settings.EMAIL_HOST_USER' , [email] , fail_silently=False)
                return user
            return None
        except User.DoesNotExist:
            return None
        

            
        
