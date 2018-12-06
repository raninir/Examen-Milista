from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib.auth import views as auth_views

urlpatterns=[
    url(r'^$',views.index),
    url(r'^index/$',views.index,name="inicio"),
    url(r'^Ingresar/$',views.ingresar,name="login"),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^admin/$',views.admin,name="admin"),
    url(r'^Registro',views.registro,name="registrarse"),
    url(r'^AgregarProducto/',views.agregarproductos,name="AgregarProducto"),
    url(r'^AgregarTienda/',views.agregartiendas,name="agregartiendas"),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    


    #RECUPERAR CONTRASEÑA 

    url(r'^password_reset', PasswordResetView.as_view(), 
        {'template_name':'password_reset_form.html',
        'email_template_name': 'password_reset_email.html'}, 
        name='password_reset'), 
    url(r'^password_reset_done', PasswordResetDoneView.as_view(), 
        {'template_name': 'password_reset_done.html'}, 
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$', PasswordResetConfirmView.as_view(), 
        {'template_name': 'password_reset_confirm.html'},
        name='password_reset_confirm'
        ),
    url(r'^reset/done', PasswordResetCompleteView.as_view(), {'template_name': 'password_reset_complete.html'},
        name='password_reset_complete'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   

