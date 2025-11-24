from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from django.conf import settings

def send_welcome_email(user):
    """
    Sends an HTML + plaintext welcome email to `user`.
    """
    if not user.email:
        return False

    subject = "Welcome to My Todo App 🎉"
    from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "noreply@yourdomain.com")
    to = [user.email]

    # context used in templates
    context = {
        "username": user.get_username(),
        "login_url": "http://127.0.0.1:8000/login/",  # change to production URL in prod
        "year": datetime.now().year,
    }

    html_body = render_to_string("emails/welcome_email.html", context)
    text_body = render_to_string("emails/welcome_email.txt", context)

    msg = EmailMultiAlternatives(subject, text_body, from_email, to)
    msg.attach_alternative(html_body, "text/html")
    msg.send(fail_silently=False)
    return True
