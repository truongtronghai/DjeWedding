import mimetypes
from .views import IndexView
from django.urls import path

app_name = "card"

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]

# add minetype for Js in case of browser prevent from a disallowed MIME type
mimetypes.add_type("application/javascript", ".js", True)
