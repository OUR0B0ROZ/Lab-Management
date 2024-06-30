from django.urls import path
from django.contrib.auth import views as auth_views
from .views import  (
    ModelListView, ModelDetailView,ModelCreateView,ModelUpdateView,ModelDeleteView,
    AreaCreateView,AreaUpdateView,AreaDetailView,AreaDeleteView,AreaListView,
    ClassUpdateView,ClassListView, ClassDetailView,ClassCreateView,ClassDeleteView,
    GroupListView,GroupDetailView,GroupCreateView,GroupUpdateView,GroupDeleteView,
    UsersPerAreaView,
    RecordListView,
)

app_name = 'django_module_basic'

urlpatterns = [
    path('', ModelListView.as_view(), name='model-list'),  # List all models
    path('category/<slug:category_slug>/', ModelListView.as_view(), name='model-list-by-category'),  # Filter models by category
    path('<int:pk>/', ModelDetailView.as_view(), name='detail'),  # Detail view of a specific model
    path('create/', ModelCreateView.as_view(), name='model-create'),
    path('<int:pk>/update/', ModelUpdateView.as_view(), name='model-update'),
    path('<int:pk>/delete/', ModelDeleteView.as_view(), name='model-delete'),
    #Area Urls 
    path('areas/', AreaListView.as_view(), name='area-list'),
    path('area/<int:pk>/', AreaDetailView.as_view(), name='area-detail'),
    path('area/create/', AreaCreateView.as_view(), name='area-create'),
    path('area/update/<int:pk>/', AreaUpdateView.as_view(), name='area-update'),
    path('area/delete/<int:pk>/', AreaDeleteView.as_view(), name='area-delete'),
    #Class urls
    path('classes/', ClassListView.as_view(), name='class-list'),
    path('class/<int:pk>/', ClassDetailView.as_view(), name='class-detail'),
    path('class/create/', ClassCreateView.as_view(), name='class-create'),
    path('class/update/<int:pk>/', ClassUpdateView.as_view(), name='class-update'),
    path('class/delete/<int:pk>/', ClassDeleteView.as_view(), name='class-delete'),
    #Group urls  
    path('groups/', GroupListView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group-detail'),
    path('groups/create/', GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group-delete'),
    #Report urls
    path('area/<int:pk>/users/', UsersPerAreaView.as_view(), name='users_per_area'),
    #Login views 
    path('login/', auth_views.LoginView.as_view(template_name='django_module_basic/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    #Registred view
    path('records/', RecordListView.as_view(), name='records'),
]