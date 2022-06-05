import json

from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import never_cache

from update.models import Users, Employee,Role,Emprole,Accountdetails,Leaves,Queries
from .forms import EmployeeForm, UsersForm, RoleForm, AccountForm,EmpRoleForm
from django.contrib import messages

def home(request):
    return render(request,'adminhome.html')

def password(request):
    #checks email and dob and updates password
    if request.method == 'POST':
        id = request.POST.get("eid")
        dob = request.POST.get("dob")
        pwd = request.POST.get("pass")
        if id != None and id!='':
            try:
                form = UsersForm(request.POST)
                user = Users.objects.get(empid=id)
                emp = Employee.objects.get(empid=id)
                print("before checking",id,dob,pwd)
                if (str(emp.dob)==dob):
                    print("if",str(emp.dob), dob, user.password)
                    if(pwd!='' and pwd!=None):
                        user.password=pwd
                        user.save()
                        messages.success(request,"Updated Password Successfully!!")
                    else:
                        print("else", str(emp.dob), dob, user.password)
                        messages.warning(request,"invalid Password")
            except (Users.DoesNotExist ,Employee.DoesNotExist) as e:
                messages.warning(request,"Invalid id")

        return render(request, 'password.html')
    return render(request,'password.html')

def rpassword(request):
    if request.method == 'POST':
        id = request.POST.get("eid")
        if id != None and id!='':
            try:
                user = Users.objects.get(empid=id)
                user.password='Hello@123'
                user.save()
                messages.success(request,"Password reset Successfull!!")
            except Users.DoesNotExist :
                messages.warning(request,"Invalid id")

        return render(request, 'rpassword.html')
    return render(request,'rpassword.html')

def uemployee(request):
    id= request.POST.get("eid")
    if id!='' and id != None:
        form = EmployeeForm()
        try:
            emp = Employee.objects.get(empid=id)
            if request.method == 'POST':
                form = RoleForm(request.POST)
                change=False
                name = request.POST.get('name')
                email = request.POST.get('email')
                phno = request.POST.get('phno')
                dob = request.POST.get('dob')
                doj = request.POST.get('doj')
                address = request.POST.get('address')
                if emp.name != name and name!='' and name!=None:
                    emp.name=name
                    emp.save()
                    change=True

                if emp.email != email and email!='' and email!=None:
                    emp.email = email
                    emp.save()
                    change=True

                if emp.phno!=phno and phno!='' and phno!=None:
                    emp.phno=phno
                    emp.save()
                    change = True
                if str(emp.dob)!=dob and dob!='' and dob!=None:
                    emp.dob=dob
                    emp.save()
                    change = True

                if str(emp.doj)!=doj and doj!='' and doj!=None:
                    emp.doj=doj
                    emp.save()
                    change = True

                if emp.address!=address and address!='' and address!= None:
                    emp.address=address
                    emp.save()
                    change = True
                if change:
                    print("Employee with empid:{} updated!!".format(id))
                    messages.success(request, "Updated Successfully !!")
                else:
                    print("No change in data!")
                    messages.warning(request, "No change in data!")
                '''
                if form.is_valid():
                    print("form is valid")
                    #if emp.empid !=
                    form.save()
                    messages.success(request, "Updated Successfully !!")
                print(form.errors)
                '''
            return render(request, 'uemployee.html', {'emp':emp,'valid':True})
        except Employee.DoesNotExist:
            messages.warning(request, "Invalid Employee ID, please try again")
            return render(request, 'uemployee.html', {'valid': False})
    else:
        return render(request, 'uemployee.html', {'valid': False})

def urole(request):
    id = request.POST.get("rid")
    if id != '' and id != None:

        try:
            role = Role.objects.get(rid=id)
            if request.method == 'POST':
                form = EmployeeForm(request.POST)
                change = False
                name = request.POST.get('name')
                basic = request.POST.get('basic')
                hra = request.POST.get('hra')
                bonus = request.POST.get('bonus')
                ta = request.POST.get('ta')
                ma = request.POST.get('ma')
                pfc = request.POST.get('pfc')
                wf = request.POST.get('wf')
                if role.rolename != name and name != '' and name != None:
                    role.rolename = name
                    role.save()
                    change = True

                if role.basic != basic and basic != '' and basic != None:
                    role.basic = basic
                    role.save()
                    change = True

                if role.houserentallowance != hra and hra != '' and hra != None:
                    role.houserentallowance = hra
                    role.save()
                    change = True

                if role.bonus != bonus and bonus != '' and bonus != None:
                    role.bonus = bonus
                    role.save()
                    change = True

                if role.houserentallowance != hra and hra != '' and hra != None:
                    role.houserentallowance = hra
                    role.save()
                    change = True
                if role.travelallowance != ta and ta != '' and ta != None:
                    role.travelallowance = ta
                    role.save()
                    change = True

                if role.medicalallowance != ma and ma != '' and ma != None:
                    role.medicalallowance = ma
                    role.save()
                    change = True

                if role.pfcontribution != pfc and pfc != '' and pfc != None:
                    role.pfcontribution = pfc
                    role.save()
                    change = True
                if role.welfaretrust != wf and wf != '' and wf != None:
                    role.welfaretrust = wf
                    role.save()
                    change = True
                if change:
                    print("Role with rid:{} updated!!",id)
                    messages.success(request, "Updated Successfully !!")
                else:
                    print("No change in data!")
                    messages.warning(request, "No change in data!")
                '''
                if form.is_valid():
                    print("form is valid")
                    #if role.rid !=
                    form.save()
                    messages.success(request, "Updated Successfully !!")
                print(form.errors)
                '''
            return render(request, 'urole.html', {'role': role, 'valid': True})
        except Role.DoesNotExist:
            messages.warning(request, "Invalid Role ID, please try again")
            return render(request, 'urole.html', {'valid': False})
    else:
        return render(request, 'urole.html', {'valid': False})


def uaccount(request):
    empid = request.POST.get('empid')
    if empid!=None and empid !='':
        try:
            acc = Accountdetails.objects.get(empid=empid)
            form=AccountForm(request.POST)
            if request.method == "POST":
                bankac = request.POST.get('bankaccountno')
                pan = request.POST.get('pan no')
                pf = request.POST.get('pf number')
                change = False
                if bankac != '' and bankac != None and acc.bankaccountno != bankac:
                    acc.bankaccountno = bankac
                    change = True
                    acc.save()
                if pan != '' and pan != None and acc.pan_no != pan:
                    acc.pan_no = pan
                    change = True
                    acc.save()
                if pf != '' and pf != None and acc.pf_number != pf:
                    acc.pf_number = pf
                    change = True
                    acc.save()
                if change:
                    print("Accountdetails with empid:{} updated!!", id)
                    messages.success(request, "Updated Successfully !!")
                else:
                    print("No change in data!")
                    messages.warning(request, "No change in data!")
                print(form.errors)
                return render(request, 'uaccount.html', {'valid': True,'account':acc})
        except Accountdetails.DoesNotExist:
            messages.warning(request, "EMP ID doesnt have account, please try again")
    return render(request, 'uaccount.html', {'valid': False})

def disemprole(request):
    emprole=Emprole.objects.all()
    return render(request,'emprole.html',{'emprole':emprole})

def getemprole(request):
    try:
        emp=Employee.objects.all()
        empid=request.POST.get("empid")
        if empid!=None and empid!='':
            emprole=Emprole.objects.filter(empid=empid)
            rid=request.POST.get('rid')
            if rid != None and rid != '':
                t='uemprole.html/'.append(empid)
                return render(request,t.append(rid),{'valid':True,'emp':emp,'emprole':emprole})
            return render(request,'getemprole.html',{'valid':True,'emp':emp,'emprole':emprole})
    except Emprole.DoesNotExist:
        messages.warning(request,"emprole doesnt exist for employee {}".format(empid))
    return render(request, 'getemprole.html', {'valid': False, 'emp': emp})

def eemprole(request,empid,rid):
    try:
        emprole=Emprole.objects.get(empid=empid,rid=rid)
        return render(request,'uemprole.html',{'emprole':emprole})
    except Emprole.DoesNotExist:
        messages.warning(request,"employee role doesnt exist")
    return render(request, 'uemprole.html', {'emprole': emprole})

def uemprole(request,empid,rid):
    try:
        '''
        ids=request.POST.get("ids")
        if ids!=None and ids!='':
            ids=ids.split('|')
            empid=int(ids[0].empid)
            rid=int(ids[1].rid)
        '''
        if empid!='' and empid!=None and rid!='' and rid!=None:
            emprole=Emprole.objects.get(empid=empid,rid=rid)
            if request.method == "POST":
                joblocation = request.POST.get("joblocation")
                start_date = request.POST.get("start_date")
                end_date = request.POST.get("end_date")
                change=False
                if joblocation != '' and joblocation != None and emprole.joblocation != joblocation:
                    emprole.joblocation = joblocation
                    change = True
                    emprole.save()
                if start_date != '' and start_date != None and emprole.start_date != start_date:
                    emprole.start_date = start_date
                    change = True
                    emprole.save()
                if emprole.end_date != end_date and end_date!='':
                    emprole.end_date = end_date
                    change = True
                    emprole.save()
                if change:
                    print("Accountdetails with empid:{} updated!!", id)
                    messages.success(request, "Updated Successfully !!")
                else:
                    print("No change in data!")
                    messages.warning(request, "No change in data!")
            return render(request,'uemprole.html',{'emprole':emprole})

    except Emprole.DoesNotExist:
        messages.warning(request,"employee role doesnt exist")
    return render(request, 'uemprole.html', {'emprole': emprole})

def test(request):
    form = EmployeeForm()
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            messages.success(request,"Updated Successfully !!")
    return render(request,'slip.html',{'form':form})

def vemp(request):
    try:
        emp=Employee.objects.all()
        if request.method == 'POST':
            empid=request.POST.get('empid')
            name = request.POST.get('name')
            email = request.POST.get('email')
            phno = request.POST.get('phno')
            #dob = request.POST.get('dob')
            #doj = request.POST.get('doj')
            address = request.POST.get('address')
            ep=empid!='' and empid!=None
            n=name!='' and name!=None
            em=email!='' and email!=None
            p=phno!='' and phno!=None
            a=address!='' and address!=None
            if n and address:
                emp = Employee.objects.filter(name__icontains=name,address__icontains=address)
            elif ep:
                emp=Employee.objects.filter(empid=empid)
            elif em:
                emp = Employee.objects.filter(email__icontains=email)
            elif phno:
                emp = Employee.objects.filter(phno__icontains=phno)
            elif name:
                emp= Employee.objects.filter(name__icontains=name)
            elif address:
                emp = Employee.objects.filter(address__icontains=address)
            else:
                pass
            #write filters
        return render(request,'vemployee.html',{'emp':emp})
    except Employee.DoesNotExist:
        return render(request, 'vemployee.html', {'emp': emp})

def vaccount(request):
    try:
        acc=Accountdetails.objects.all()
        if request.method == 'POST':
            empid=request.POST.get('empid')
            bno = request.POST.get('bno')
            pan = request.POST.get('pan')
            pf = request.POST.get('pf')
            e = empid != '' and empid != None
            b=bno!='' and bno!=None
            pa=pan!='' and pan!=None
            p=pf!='' and pf!=None

            if e:
                acc = Accountdetails.objects.filter(empid=empid)
            elif b:
                acc = Accountdetails.objects.filter(bankaccountno__icontains=bno)
            elif pa:
                acc = Accountdetails.objects.filter(pan_no__icontains=pan)
            elif p:
                acc = Accountdetails.objects.filter(pf_number__icontains=pf)
            else:
                pass
            #write filters
        return render(request,'vaccount.html',{'acc':acc})
    except Employee.DoesNotExist:
        return render(request, 'vaccount.html', {'acc': acc})

def vrole(request):
    try:
        role=Role.objects.all()
        if request.method == 'POST':
            rid=request.POST.get('rid')
            name = request.POST.get('name')
            r = rid != '' and rid != None
            n=name!='' and name!=None

            if r:
                role = Role.objects.filter(rid=rid)
            elif n:
                role = Role.objects.filter(rolename__icontains=name)
            else:
                pass
        #print(role.values())
        return render(request,'vrole.html',{'role':role})
    except Employee.DoesNotExist:
        return render(request, 'vrole.html', {'role': role})

def vemprole(request):
    try:
        emp=Emprole.objects.all()
        if request.method == 'POST':
            empid=request.POST.get('empid')
            rid = request.POST.get('rid')
            joblocation = request.POST.get('joblocation')
            e=empid!='' and empid!=None
            r=rid!='' and rid!=None
            j=joblocation!='' and joblocation!=None

            if e:
                emp = Employee.objects.filter(empid=empid)
            elif r:
                emp=Employee.objects.filter(rid=rid)
            elif j:
                emp = Employee.objects.filter(joblocation__icontains=joblocation)
            else:
                pass
            #write filters
        return render(request,'vemprole.html',{'emprole':emp})
    except Employee.DoesNotExist:
        return render(request, 'vemprole.html', {'emprole': emp})

def vqueries(request):
    try:
        queries=Queries.objects.all()
        if request.method == 'POST':
            empid=request.POST.get('empid')
            qu=request.POST.get('query')
            e=empid!='' and empid != None
            q=qu!=''and qu!=None
            if e and q :
                queries = Queries.objects.filter(empid=empid,query__icontains=qu)
            elif e:
                queries=Queries.objects.filter(empid=empid)
            elif q:
                queries=Queries.objects.filter(query__icontains=qu)
            else:
                pass

        return render(request,'vqueries.html',{'queries':list(queries.values())})
    except Queries.DoesNotExist:
        messages.warning(request,"invalid data")
        return render(request,'vqueries.html',{'queries':list(queries.values())})


###################
#insert functions #
###################
def iemployee(request):
    if request.method == 'POST':
        #id = request.POST.get("empid")
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            print("employee inserted")
            messages.success(request,"Employee Inserted!!")
        if form.errors:
            return render(request,'iemployee.html',{'errors':form.errors})
    return render(request, 'iemployee.html')

def irole(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            print("Role inserted")
            messages.success(request,"Role Inserted!!")
        if form.errors:
            return render(request,'irole.html',{'errors':form.errors})
    return render(request, 'irole.html')

def iaccount(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            print("Account details inserted")
            messages.success(request, "Account details inserted!!")
        if form.errors:
            return render(request, 'iaccount.html', {'errors': form.errors})
    return render(request, 'iaccount.html')

def iemprole(request):
    emp = Employee.objects.all()
    role = Role.objects.all()
    try:

        if request.method=='POST':
            form=EmpRoleForm(request.POST)
            if form.is_valid():
                empid = request.POST.get('empid')
                rid = request.POST.get('rid')
                r = Role.objects.get(rid=rid)
                if empid != '---' and rid != '---':
                    u=Users.objects.filter(empid=empid).first()
                    if u==None:
                        if r.rolename == 'Admin':
                            Users.objects.create(empid=empid,password="admin@123",isadmin=1)
                        else:
                            Users.objects.create(empid=empid,password="user@123",isadmin=0)
                    else:
                        if r.rolename == 'Admin':
                            u=Users.objects.get(empid=empid)
                            u.isadmin=1
                form.save()
                print("User inserted!")
                print("Emprole inserted")
                messages.success(request, "Emp Role inserted!!")
            if form.errors:
                return render(request, 'iemprole.html', {'errors': form.errors})

    except (Emprole.DoesNotExist, Role.DoesNotExist) as e:
        messages.warning(request,"Invalid ID")
    except Emprole.IntegrityError:
        messages.warning(request,"Employee Role already exists")
    except Users.IntegrityError:
        messages.warning(request,"User entry already exists")
    return render(request,'iemprole.html',{'emp':list(emp.values()),'role':list(role.values())})


def drole(request):
    role = Role.objects.all()
    try:
        if request.method == "POST":
            rid = request.POST.get('rid')
            if rid!='' and rid !=None:
                role=Role.objects.filter(rid=rid)
                emprole=Emprole.objects.filter(rid=rid)
                emes=emprole.delete()
                erole=role.delete()
                print(emes,erole)
                if(emes[0]!=0):
                    messages.success(request,'{} rows deleted from employee role'.format(emes[0]))
                if(erole[0]!=0):
                    messages.success(request, '{} rows deleted from role'.format(erole[0]))
        return render(request,'drole.html', {'role': role.values()})
    except (Emprole.DoesNotExist, Role.DoesNotExist) as e:
        messages.warning(request, "Invalid ID")
    return render (request, 'drole.html',{'role':role})

def demp(request):
    emp=Employee.objects.all()
    try:
        empid = request.POST.get("empid")
        if request.method=='POST' and empid !='':
            u=Users.objects.filter(empid=empid).first()
            if u!=None:
                u=u.delete()
                print("u",u)
                if (u[0] != 0):
                    messages.success(request, "{} rows deleted from users".format(u[0]))
            q=Queries.objects.filter(empid=empid).first()
            if q!=None:
                q=q.delete()
                print("q",q)
                if (q[0] != 0):
                    messages.success(request, "{} rows deleted from queries".format(q[0]))
            l=Leaves.objects.filter(empid=empid).first()
            if l!=None:
                l=l.delete()
                print("l",l)
                if (l[0] != 0):
                    messages.success(request, "{} rows deleted from leaves".format(l[0]))
            a=Accountdetails.objects.filter(empid=empid).first()
            if a!=None:
                a=a.delete()
                print("a",a)
                if (a[0] != 0):
                    messages.success(request, "{} rows deleted from accounts".format(a[0]))
            er=Emprole.objects.filter(empid=empid)
            ercount=0
            for i in er:
                print(i)
                if i:
                    x=i.delete()
                    if x[0]!=0:
                        ercount+=1
            e=Employee.objects.get(empid=empid).delete()

            if(ercount>0):
                messages.success(request,"{} rows deleted from employee role".format(ercount))
            if (e[0] != 0):
                messages.success(request, "{} rows deleted from employee".format(e[0]))
    except(Emprole.DoesNotExist, Queries.DoesNotExist,Users.DoesNotExist,Leaves.DoesNotExist,Accountdetails.DoesNotExist) as e:
        messages.warning(request,"error")
    return render(request,'demp.html',{'emp':emp})

def daccount(request):
    emp = Employee.objects.all()
    try:
        empid = request.POST.get("empid")
        if request.method == 'POST' and empid != '':
            a=Accountdetails.objects.get(empid=empid)
            a=a.delete()
            print("a",a)
            if (a[0] != 0):
                messages.success(request, "{} rows deleted from accounts".format(a[0]))

    except Accountdetails.DoesNotExist:
        messages.warning(request, "Account doesnt exist")
    return render(request, 'daccount.html', {'emp': emp})

def demprole(request,empid,rid):
    try:
        '''
        ids=request.POST.get("ids")
        if ids!=None and ids!='':
            ids=ids.split('|')
            empid=int(ids[0].empid)
            rid=int(ids[1].rid)
        '''
        if empid!='' and empid!=None and rid!='' and rid!=None:
            emprole=Emprole.objects.filter(empid=empid,rid=rid)
            count=0
            for i in emprole:
                x=i.delete()
                count+=1
            if(count>0):
                print("{} rows employee roles deleted".format(count))
                messages.success(request, "{} rows employee roles deleted".format(count))
        emprole=Emprole.objects.all()
    except Emprole.DoesNotExist:
        messages.warning(request,"employee role doesnt exist")
    return render(request, 'emprole.html', {'emprole': emprole})
