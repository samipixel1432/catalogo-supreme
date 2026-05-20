from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # Públicas
    path('', views.landing, name='landing'),
    path('acceso/', views.acceso, name='acceso'),
    path('coleccion/', views.coleccion, name='coleccion'),
    path('producto/<slug:slug>/', views.detalle, name='detalle'),

    # Panel admin
    path('panel/login/', views.panel_login, name='panel_login'),
    path('panel/logout/', views.panel_logout, name='panel_logout'),
    path('panel/', views.panel_dashboard, name='panel_dashboard'),
    path('panel/producto/nuevo/', views.panel_producto_nuevo, name='panel_producto_nuevo'),
    path('panel/producto/<int:pk>/editar/', views.panel_producto_editar, name='panel_producto_editar'),
    path('panel/producto/<int:pk>/eliminar/', views.panel_producto_eliminar, name='panel_producto_eliminar'),
    path('panel/categoria/nueva/', views.panel_categoria_nueva, name='panel_categoria_nueva'),
    path('panel/producto/<int:pk>/imagen/<int:img_pk>/eliminar/', views.panel_imagen_eliminar, name='panel_imagen_eliminar'),
]
