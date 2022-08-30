from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.mail import send_mail  # using for sending email
# messages
from django.contrib import messages

from django.views import View
from .models import Block


# Create your views here.
class IndexView(View):
    template_name = 'card/index.html'

    # template for creating custom method
    def sendingEmail(self, name="", confirmation="", *args, **kwargs):

        to_email = settings.EMAIL_HOST_USER
        results = send_mail(
            "Xác nhận tham dự lễ cưới từ {}".format(name),
            "Bạn nhận được xác nhận tham dự lễ cưới của bạn từ {} với kết quả xác nhận là: {} ".format(
                name, confirmation),
            to_email,
            # sending mail to myself
            [to_email],
            fail_silently=False,
        )

        if results > 0:
            return True
        else:
            return False

    def get(self, request):
        queryset = Block.objects.filter(enabled=True)

        if len(queryset) == 0:
            return HttpResponse("Page is empty. Please contact administrator.", content_type="text/plain")

        blocks = {}

        for item in queryset:  # convert to dictionary
            blocks.update({str(item.name): {
                "title": item.title,
                "description": item.description,
                "short_text_1": item.short_text_1,
                "short_text_2": item.short_text_2,
                "short_text_3": item.short_text_3,
                "short_text_4": item.short_text_4,
                "image": item.image,
                "enabled": item.enabled
            }
            })

        context = {
            'blocks': blocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        # print(request.POST["name"])
        if self.sendingEmail(request.POST["name"], request.POST["confirmation"]):
            messages.success(
                request, "Xác nhận của quý khách đã được gởi. Chân thành cảm ơn !")
        else:
            messages.error(
                request, "Xác nhận của quý khách đã được gởi. Chân thành cảm ơn !")

        return HttpResponseRedirect("/")
