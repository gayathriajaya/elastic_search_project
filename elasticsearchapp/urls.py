from django.conf.urls import include ,url,patterns
from .views import *

urlpatterns = [
	


	#http://localhost:8000/mobile/ES/pushdata/
    url(r'^ES/pushdata/?$', pushdata.as_view() ),
	
	#http://localhost:8000/mobile/ES/insertdata.html/
    url(r'^ES/insertdata.html/?$', insertdata ),
      

]
