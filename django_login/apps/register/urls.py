from django.conf.urls import url
from .views import index,register,login,success,userinfocollect,FactorAnalysis #,t
urlpatterns = [

    url(r'^$', index),
    url(r'^userinfocollect$', userinfocollect),
    url(r'^register$', register),
    url(r'^success$', success),
    url(r'^login$', login),
    url(r'^FactorAnalysis$', FactorAnalysis)
]