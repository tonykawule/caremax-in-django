from django.urls import path
from . import views

urlpatterns = [
    ## Patient routes ##
    path('', views.home, name='home'),
    path('newpatient', views.newpatient, name='newpatient'),
    path('patientlist', views.patientlist, name='patientlist'),
    path('patient/<str:pk>/editpatient', views.editpatient, name='editpatient'),
    path('patient/<str:pk>/deletepatient',
         views.deletepatient, name='deletepatient'),
    path('patient/<int:patient_id>/visits/newpatientvisit',
         views.newpatientvisit, name='newpatientvisit'),
    path('patient/<int:patient_id>/visits/visitlist',
         views.visitlist, name='visitlist'),
    path('patient/<int:patient_id>/visits/<int:id>/editpatientvisit',
         views.editpatientvisit, name='editpatientvisit'),
    path('patient/<int:patient_id>/profile', views.profile, name='profile'),
    path('patient/<int:patient_id>/tests/newpatienttest',
         views.newpatienttest, name='newpatienttest'),
    path('patient/<int:patient_id>/tests/testlist',
         views.testlist, name='testlist'),
    path('patient/<int:patient_id>/treatments/newpatienttreatment',
         views.newpatienttreatment, name='newpatienttreatment'),
    path('patient/<int:patient_id>/treatment/treatmentlist',
         views.treatmentlist, name='treatmentlist'),
    path('patient/<int:patient_id>/bill/bill_list',
         views.bill_list, name='bill_list'),
    path('patient/<int:patient_id>/bill/newpatientbill',
         views.newpatientbill, name='newpatientbill'),

    ## Stock category routes ##
    path('stockcategorylist', views.stockcategorylist, name='stockcategorylist'),
    path('newstockcategory', views.newstockcategory, name='newstockcategory'),
    path('stockcategory/<str:pk>/editstockcategory',
         views.editstockcategory, name='editstockcategory'),
    path('stockcategory/<str:pk>/deletestockcategory',
         views.deletestockcategory, name='deletestockcategory'),

    ## stock routes ##
    path('stocklist', views.stocklist, name='stocklist'),
    path('newstock', views.newstock, name='newstock'),
    path('stock/<str:pk>/editstock', views.editstock, name='editstock'),
    path('stock/<str:pk>/deletestock', views.deletestock, name='deletestock'),
    path('stock/<str:pk>/stock_detail', views.stock_detail, name='stock_detail'),
    path('stock/<str:pk>/issue_item', views.issue_item, name='issue_item'),
    path('stock/<str:pk>/receive_item', views.receive_item, name='receive_item'),
    path('stock/<str:pk>/reorder_level',
         views.reorder_level, name='reorder_level'),

    ## LOgin and Register

    path('login', views.loginPage, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logoutUser, name='logout'),

]
