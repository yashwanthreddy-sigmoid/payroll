from datetime import *
import string
from django.shortcuts import render
from django.http import HttpResponse
from .models import Emprole,Role,Employee,Accountdetails,Leaves,Queries,Users
from django.db.models import Max
empid1=None
# Create your views here.

def index(request):


    return render(request,'login.html')
def start(request):
     
    global empid1 
    empid1 = int(request.POST['empid'])
    passw = str(request.POST['password'])

    p=Users.objects.filter(empid=empid1,password=passw)
    
    count=0
    for i in p:
        count=count+1
        admin=i.isadmin
    p=Employee.objects.filter(empid=empid1)
    for i in p:
        user=i.name
    if(count>0):
        if(admin==0):
            return render(request,'viewtable.html',{'name':user})
        else:
            return render(request,'admin.html',{'empid':empid1})
        '''
        else:
            response = HttpResponse(status=302)
            response['Location'] = '/update/'
            return response
        '''

    else:
        return HttpResponse('he is not employee')

def admin(request):
    global empid1
    empid1 = int(request.POST['empid'])
    if empid1!=None and empid1!='':
        p = Employee.objects.get(empid=empid1)
        user = p.name
        return render(request, 'viewtable.html', {'name': user})
    else:
        return render(request, 'login.html')

def tablesview(request):
    tablename = request.POST['view']
    if(tablename=='employee'):
        p=Employee.objects.all()
        return render(request,'employeetable.html',{'p':p})
    if(tablename=='emprole'):
        p=Emprole.objects.all()
        return render(request,'emproletable.html',{'p':p})
        
    if(tablename=='role'):
        p=Role.objects.all()
        return render(request,'roletable.html',{'p':p})
    if(tablename=='accountdetails'):
        global empid1
        p=Accountdetails.objects.filter(empid = empid1)
        return render(request,'accountdetailstable.html',{'p':p})
    if(tablename=='leaves'):
        p=Leaves.objects.filter(empid = empid1)
        return render(request,'leavedetailstable.html',{'p':p})
    if(tablename=='queries'):
        p=Queries.objects.filter(empid = empid1)
        return render(request,'querydetailstable.html',{'p':p})

    
def insert(request):
    tablename= request.POST['insert']

    if(tablename=='queries'):
        return render(request,'insertqueries.html',{'str':'insert'})
    if(tablename=='leaves'):
        return render(request,'insertleaves.html',{'str':'insert'})
    


def tablesupdate(request):
    tablename = request.POST['update']
    if(tablename=='accountdetails'):
        update= 'update'
        return render(request,'updateaccountdetails.html',{'str':update})
    if(tablename=='queries'):
        update= 'update'
        return render(request,'updatequeries.html',{'str':update})
    if(tablename=='leaves'):
        update= 'update'
        return render(request,'updateleaves.html',{'str':update})






def updateaccountdetails(request):
    global empid1
    #empid1 =  request.POST['empid']
    accno =  request.POST['bankaccountno']
    pan_no =  request.POST['pan_no']
    pf_number=  request.POST['pf_number']
    if(accno =='' and pan_no=='' and pf_number==''):
        return HttpResponse("something went wrong")
    p=Accountdetails.objects.filter(empid=empid1)
    count=0
    for i in p:
        i.bankaccountno = accno
        i.pan_no = pan_no
        i.pf_number = pf_number
        i.save()
        count=count+1
    if(count>0 ): 
        return HttpResponse("update sucessful")
    else:
        return HttpResponse("something went wrong")



def updatequeries(request):
    global empid1
    queryid= int(request.POST['idqueries'])
    query1 = request.POST['query']
    qdate = request.POST['date']
    #empid1 = request.POST['empid']
    p=Queries.objects.filter(empid = empid1,idqueries=queryid)
    count=0
    for i in p:

        
        i.query = query1
        i.date = qdate
        i.save()
        count=count+1
    
    if(count>0 ): 
        return HttpResponse("update sucessful")
    else:
        return HttpResponse("something went wrong")



def updateleaves(request):
    global empid1
    leaveid1= int(request.POST['leaveid'])

    qdate = request.POST['date']
    #empid1 = request.POST['empid']
    p=Leaves.objects.filter(empid = empid1,leaveid=leaveid1)
    count=0
    for i in p:

        

        i.date = qdate
        i.save()
        count=count+1
    
    if(count>0 ): 
        return HttpResponse("update sucessful")
    else:
        return HttpResponse("something went wrong")





    




def insertqueries(request):
    global empid1
    
    query1 = request.POST['query']
    current_time = datetime.now()
    qdate = current_time.strftime("%Y-%m-%d")
    #qdate = request.POST['date']
    #empid1 = int(request.POST['empid'])
    result = Queries.objects.all().aggregate(Max('idqueries'))
    print(result)
    queryid=result['idqueries__max']+1
    news_obj = Employee.objects.get(empid=empid1)
    count= Queries.objects.all().count()
    Queries.objects.create(idqueries=queryid ,empid=news_obj,query=query1,date=qdate)
    count1= Queries.objects.all().count()
    if(count1>count):
        return HttpResponse("update sucessful")
    else:
        return HttpResponse("something went wrong")






def insertleaves(request):
    global empid1
    

    qdate = request.POST['date']
    #empid1 = int(request.POST['empid'])
    result = Leaves.objects.all().aggregate(Max('leaveid'))
    leaveid1=result['leaveid__max']+1
    news_obj = Employee.objects.get(empid=empid1)
    count= Leaves.objects.all().count()
    Leaves.objects.create(leaveid=leaveid1 ,empid=news_obj,date=qdate)
    count1= Leaves.objects.all().count()
    if(count1>count):
        return HttpResponse("update sucessful")
    else:
        return HttpResponse("something went wrong")
  

def payslip(request):

    return render(request,'createpayslip.html')




def generatepayslip(request):
    global empid1
    month=request.POST['month']
    year=request.POST['year']
    p=Employee.objects.filter(empid=empid1)
    for i in p:
        name=i.name

    
    p1=Accountdetails.objects.filter(empid=empid1)
    count=0
    for i in p1:
        accountnumber=i.bankaccountno
        pannumber=i.pan_no
        pfnumber=i.pf_number
        count=count+1

    if(count==0):
        return HttpResponse('employee account number is not updated')
    
    
    p2=Emprole.objects.filter(empid=empid1)
    
    maxi = "1000-12-12" 
    d1 = maxi.split("-")

    for i in p2:
        startdate=str(i.start_date)
        #print(startdate)
        d2=startdate.split("-")
        if(d2[0]>d1[0]):
            maxi=startdate
            roleid=i.rid
            for j in range(3):
                d1[j]=d2[j]
        elif(d2[0]==d1[0] and d2[1]>d1[1]):
            maxi=startdate
            roleid=i.rid
            for j in range(3):
                d1[j]=d2[j]
        elif(d2[0]==d1[0] and d2[1]==d1[1] and d2[2]>d1[2]):
            maxi=startdate
            roleid=i.rid
            for j in range(3):
                d1[j]=d2[j]
        
     
            
    #roleid=Role.objects.get(rid=roleid)

    roleid=roleid.rid
    p2=Emprole.objects.filter(empid=empid1,rid=roleid)
    for i in p2:
        joblocation=i.joblocation
    p4=Role.objects.filter(rid=roleid)

    for i in p4:
        rn = i.rolename
        bs =i.basic
        house = i.houserentallowance
        pf= i.pfcontribution
        bonus = i.bonus
        travel = i.travelallowance
        medical =i.medicalallowance
        welfare = i.welfaretrust



    

    dicton={'January':'01','February':'02','March':'03','April':'04','May':'05','June':'06','July':'07','August':'08','September':'09',
    'October':'10','November':'11','December':'12'}   
    count=0
    mon=dicton[month]
    p5=Leaves.objects.filter(empid=empid1)
    #print(mon)
    #print(year)
    for i in p5:
        print(i.date)
        date1=str(i.date)
        d1=date1.split('-')
        print(d1[0],d1[1],d1[2])
        if(d1[0]==year and str(d1[1])==mon):
            count=count+1
    
    salaryperday=bs/21
    print(count)
    print(salaryperday)

    total_basic_salary= bs-(salaryperday*count)
    print(total_basic_salary)

    total_salary=total_basic_salary+house+bonus+travel+medical-welfare-pf
    total_add=total_basic_salary+house+bonus+travel+medical

    total_deductions=pf+welfare
    return render(request,'generatepayslip.html',{'name':name,'joblocation':joblocation,'acc':accountnumber,'panno':pannumber,'pf_no':pfnumber,'rid':roleid,'rolename':rn,
    'basic':bs ,'houserentallowance':house, 'pf':pf,'bonus':bonus,'travelallowance':travel, 
     'medicalallowance':medical ,'welfaretrust':welfare ,'total_add':total_add,'total_deductions':total_deductions,'total_base':total_basic_salary,'salary':total_salary,'month':month,'year':year,'empid':empid1,'leaves':count})

