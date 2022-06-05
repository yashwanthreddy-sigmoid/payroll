from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('viewtable',views.start,name='start'),
    path('view',views.tablesview,name='tablesview'),
    path('update',views.tablesupdate,name='tablesupdate'),
    path('updateaccountdetails',views.updateaccountdetails,name='updateaccountdetails'),
    path('updatequeries',views.updatequeries,name='updatequeries'),
    path('updateleaves',views.updateleaves,name='updateleaves'),
    path('insert',views.insert,name='insert'),
    path('admin',views.admin,name='admin'),
    path('insertqueries',views.insertqueries,name='insertqueries'),
    path('insertleaves',views.insertleaves,name='insertleaves'),
    path('payslip',views.payslip,name='payslip'),
    path('generatepayslip',views.generatepayslip,name='generatepayslip')

]
