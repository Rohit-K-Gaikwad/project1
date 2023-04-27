"""URL mapping for user API

/api/user/
/api/user/create
/api/user/me/
"""

from django.urls import path
from . import views


urlpatterns = [
    path("jobtitle/", views.JobTitleViewSet.as_view({"get": "list"}),
         name="jobtitle"),
]
