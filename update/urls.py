from django.urls import path
import update.views as view
#app_name= 'update'

urlpatterns = [
    path('', view.home, name='admin home'),
    path('password', view.password, name='password'),
    path('rpassword', view.rpassword, name='rpassword'),
    path('uemployee', view.uemployee, name='uemployee'),
    path('urole', view.urole, name='urole'),
    path('uemprole',view.uemprole,name='uemprole'),
    path('uaccount',view.uaccount,name='uaccount'),
    path('uemprole/<int:empid>/<int:rid>/',view.uemprole,name='uemprole'),
    path('test', view.test, name='test'),
    path('emprole',view.disemprole,name='emprole'),
    path('eemprole/<int:empid>/<int:rid>/',view.eemprole,name='eemprole'),
    path('getemprole',view.getemprole,name='getemprole'),
    path('iemployee',view.iemployee,name='iemployee'),
    path('irole',view.irole,name='irole'),
    path('iaccount',view.iaccount,name='iaccount'),
    path('iemprole',view.iemprole,name='iemprole'),
    path('vqueries',view.vqueries,name='vqueries'),
    path('vemployee',view.vemp,name='vemployee'),
    path('vemprole',view.vemprole,name='vemprole'),
    path('vrole',view.vrole,name='vrole'),
    path('vaccount',view.vaccount,name='vaccount'),
    path('drole',view.drole,name='drole'),
    path('demp',view.demp,name='demp'),
    path('daccount',view.daccount,name='daccount'),
    path('demprole/<int:empid>/<int:rid>',view.demprole,name='demprole'),

]

