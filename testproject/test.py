import mysql.connector


class payroll:

    def __init__(self):
        try:
            self.mydb = mysql.connector.connect(host='localhost', user='root', password='Harsha@123',
                                                database='payroll')
            self.cursor = self.mydb.cursor()
        except:
            print("db connection failed")

    def get_emp(self, id):
        try:
            self.cursor.execute("select * from employee where empid = %(id)s", {'id': id})
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("query to emp failed")

    def get_role(self, id):
        try:
            self.cursor.execute("select * from role where rid = %(id)s", {'id': id})
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("query to role failed")

    def get_emprole(self, id):
        try:
            self.cursor.execute("SELECT * FROM emprole where empid = %(id)s", {'id': id})
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("query to emprole failed")

    def get_leaves(self, id):
        try:
            self.cursor.execute("SELECT * FROM leaves where empid = %(id)s", {'id': id})
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("query to leaves failed")

    def get_leaves_range(self, id, start, end):
        try:
            self.cursor.execute("SELECT * FROM leaves where empid = %(id)s and date>=%(str)s and date<= %(end)s",
                                {'id': id, 'str': start, 'end': end})
            result = self.cursor.fetchall()
            for i in result:
                print(i)
        except:
            print("query to leaves failed")

    def auth(self, email, pwd):
        try:
            self.cursor.execute("SELECT * FROM users where email = %(email)s and password=%(pwd)s",
                                {'email': email, 'pwd': pwd})
            if self.cursor.rowcount == 0:
                return False
            else:
                return True
        except:
            print("auth failed")

    def is_admin(self, email):
        try:
            self.cursor.execute("SELECT isAdmin FROM users where email = %(email)s ", {'email': email})
            result = self.cursor.fetchall()
            return result
        except:
            print("query to check admin failed")

    def display(self, table):
        try:
            # print("SELECT * FROM {}".format(table))
            self.cursor.execute("SELECT * FROM %s" % table)
            result = self.cursor.fetchall()

            for i in result:
                print(i)
        except:
            print("displaying {} failed".format(table))

    ########################
    # insert
    ########################

    def insert_leave(self):
        try:
            id = int(input("please enter the employee id: "))
            leave = input("enter the date in yyyy-mm-dd format: ")
            self.cursor.execute("SELECT count(*) FROM leaves")
            count = self.cursor.rowcount
            self.cursor.execute("insert into leaves values (%s,%s,%s)", (count + 1, id, leave))
            self.mydb.commit()
            print(" 1 row was inserted.")
        except:
            print("insert to leaves failed")

    def insert_emp(self):
        try:
            id = int(input("please enter the employee id: "))
            name = input("please enter the employee name: ")
            email = input("please enter the mail: ")
            phno = input("please enter the ph.no: ")
            dob = input("enter the date of birth in yyyy-mm-dd format: ")
            doj = input("enter the date of joining in yyyy-mm-dd format: ")
            address = input("Please enter the address: ")

            self.cursor.execute("insert into employee values (%s,%s,%s,%s,%s,%s,%s)",
                                (id, name, email, phno, dob, doj, address))
            self.mydb.commit()
            print(" 1 row was inserted.")
        except:
            print("insert to employee failed")

    def insert_role(self):
        try:
            id = int(input("please enter the role id: "))
            name = input("please enter the role name: ")
            basic = int(input("please enter the basic: "))
            allowances = int(input("please enter the allowances: "))
            bonus = int(input("please enter the bonus: "))
            pf = int(input("please enter the pf: "))

            self.cursor.execute("insert into role values (%s,%s,%s,%s,%s,%s)", (id, name, basic, allowances, bonus, pf))
            self.mydb.commit()
            print(" 1 row was inserted.")
        except:
            print("insert to role failed")

    def insert_emprole(self):
        # try:
        eid = int(input("please enter the employee id: "))
        rid = int(input("please enter the role id: "))
        start = input("enter the start date in yyyy-mm-dd format: ")
        end = input("enter the end date in yyyy-mm-dd format: ")
        self.cursor.execute("select email from employee where empid=%(id)s", {'id': eid})
        email = self.cursor.fetchone()
        email = ''.join(email)
        self.cursor.execute("select rolename from role where rid=%(id)s", {'id': rid})
        rname = self.cursor.fetchone()
        rname = ''.join(rname)
        password = "qwerty123"  # default password
        self.cursor.execute("insert into emprole values (%s,%s,%s,%s)", (eid, rid, start, end))
        self.mydb.commit()
        print("1 row inserted in emprole")
        if rname == "Admin":
            self.cursor.execute("insert into users values (%s,%s,%s)", (email, password, True))
        else:
            self.cursor.execute("insert into users (email,password) values (%s,%s)", (email, password))
        self.mydb.commit()
        print("1 row inserted in users")
        # except:
        print("insert to emprole failed")

    def insert_user(self):
        try:
            # not needed as makes entry when updating emprole and has syntax to be fixed
            email = input("please enter the email: ")
            password = input("please enter the password: ")
            self.cursor.execute("select eid from employee where email=%s", (email,))
            eid = self.cursor.fetchall()
            self.cursor.execute("select rid from emprole where empid=%s", (eid,))
            rid = self.cursor.fetchall()
            self.cursor.execute("select rolename from role where rid=%s", (rid,))
            rname = self.cursor.fetchall()
            if rname == "Admin":
                self.cursor.execute("insert into users values (%s,%s,%s)", (email, password, True))
            else:
                self.cursor.execute("insert into users values (%s,%s)", (email, password))
            self.mydb.commit()
            print(" 1 row was inserted.")
        except:
            print("insert to users failed")

    ########################
    # update
    ########################
    def update_emp(self):
        # id, name, email, phno, dob, doj, address
        try:
            id = int(input("please enter the employee id: "))
            choice = int(
                input("please select the field to update \n1.name\n2.email\n3.phno\n4.dob\n5.doj\n6.address\n:"))
            if choice == 1:
                name = input("please enter the employee name: ")
                self.cursor.execute("update employee set name =  %(name)s where empid= %(id)s)",
                                    {'name': name, 'id': id})
            elif choice == 2:
                email = input("please enter the mail: ")
                self.cursor.execute("update employee set email =  %(email)s where empid= %(id)s",
                                    {'email': email, 'id': id})
            elif choice == 3:
                phno = input("please enter the ph.no: ")
                self.cursor.execute("update employee set phno =  %(pno)s where empid= %(id)s", {'pno': phno, 'id': id})
            elif choice == 4:
                dob = input("enter the date of birth in yyyy-mm-dd format: ")
                self.cursor.execute("update employee set dob =  %(dob)s where empid= %(id)s", {'dob': dob, 'id': id})
            elif choice == 5:
                doj = input("enter the date of joining in yyyy-mm-dd format: ")
                self.cursor.execute("update employee set doj =  %(doj)s where empid= %(id)s", {'doj': doj, 'id': id})
            elif choice == 6:
                address = input("Please enter the address: ")
                self.cursor.execute("update employee set address =  %(adr)s where empid= %(id)s",
                                    {'adr': address, 'id': id})
            else:
                print("invalid choice")
            self.mydb.commit()
            print(" 1 row was Updated.")
        except:
            print("update to employee failed")

    def update_role(self):
        # rid	rolename	basic	allowances	bonus	pf
        try:
            id = int(input("please enter the role id: "))
            choice = int(
                input("please select the field to update \n1.rolename\n2.basic\n3.allowances\n4.bonus\n5.pf\n:"))
            if choice == 1:
                name = input("please enter the role name: ")
                self.cursor.execute("update role set rolename =  %(name)s where rid= %(id)s)", {'name': name, 'id': id})
            elif choice == 2:
                basic = input("please enter the basic: ")
                self.cursor.execute("update role set basic =  %(basic)s where rid= %(id)s", {'basic': basic, 'id': id})
            elif choice == 3:
                allowance = input("please enter the allowances: ")
                self.cursor.execute("update role set allowances =  %(allow)s where rid= %(id)s",
                                    {'allow': allowance, 'id': id})
            elif choice == 4:
                bonus = input("please enter the bonus: ")
                self.cursor.execute("update role set bonus =  %(bo)s where rid= %(id)s", {'bo': bonus, 'id': id})
            elif choice == 5:
                pf = input("please enter the pf: ")
                self.cursor.execute("update role set pf =  %(pf)s where rid= %(id)s", {'pf': pf, 'id': id})
            else:
                print("invalid choice")

            self.mydb.commit()
            print(" 1 row was Updated.")
        except:
            print("update to role failed")

    def update_leave(self):
        # leaveid	empid	date
        try:
            id = int(input("please enter the employee id: "))
            self.cursor.execute("SELECT leaveid,date FROM leaves where empid = %(id)s", {'id': id})
            result = self.cursor.fetchall()
            counter = 1
            temp = {}
            for i in result:
                x, y = i
                print("{}) {} (yyyy-mm-dd)".format(counter, y))
                temp[counter] = [x, y]
                counter += 1

            choice = int(input("please select the date to be updated: "))
            if (choice <= len(temp)):
                date = input("please enter the new date in yyyy-mm-dd format: ")
                # need to check if date is sunday
                self.cursor.execute("update leaves set date =  %(ndate)s where leaveid = %(id)s",
                                    {'ndate': date, 'id': temp[choice][0]})
            else:
                print("invalid choice")

            self.mydb.commit()
            print(" 1 row was Updated.")

        except:
            print("update leave failed")

    def update_emprole(self):
        # empid	roleid	start_date	end_date
        try:
            eid = input("please enter employee id: ")
            self.cursor.execute("SELECT rid FROM emprole where empid = %(id)s", {'id': eid})
            result = self.cursor.fetchall()
            print("available role id's: ")
            for i in result:
                print(i, end=', ')
            rid = input("\nplease enter role id: ")
            self.cursor.execute("SELECT start_date FROM emprole where empid = %(id)s and rid=%(rid)s",
                                {'id': eid, 'rid': rid})
            s = self.cursor.fetchall()
            self.cursor.execute("SELECT end_date FROM emprole where empid = %(id)s and rid=%(rid)s",
                                {'id': eid, 'rid': rid})
            e = self.cursor.fetchall()
            choice = int(input("please select date to be updated \n1.start date\n2.end date\n: "))
            if (choice == 1):
                date = input("current date is {}, please enter the new date: ".format(s))
                self.cursor.execute("update emprole set start_date = %(ndate)s where empid = %(id)s and rid = %(rid)s",
                                    {'ndate': date, 'id': eid, 'rid': rid})
            elif (choice == 2):
                date = input("current date is {}, please enter the new date: ".format(e))
                self.cursor.execute("update emprole set end_date = %(ndate)s where empid = %(id)s and rid = %(rid)s",
                                    {'ndate': date, 'id': eid, 'rid': rid})
            else:
                print("invalid choice")

            self.mydb.commit()
            print(" 1 row was Updated.")

        except:
            print("update emprole failed")

    def update_password(self, email, oldpass):
        try:
            # email	password	isAdmin
            password = input("please enter the password to be updated: ")
            if self.auth():
                self.cursor.execute("update users set password=%(pass)s where email=%(mail)s",
                                    {'mail': email, 'pass': password})
            else:
                print("email or password is incorrect")
            self.mydb.commit()
            print(" 1 row was updated.")
        except:
            print("update password failed")

    def close(self):
        self.mydb.close()


if __name__ == '__main__':
    p = payroll()
    mail = input("please enter the Emailid : ")
    pwd = input("please enter the Password : ")
    auth = p.auth(mail, pwd)

    if auth:
        isadmin = p.is_admin(mail)
        choice = int(input(
            "please select any of th below option\n1.search\n2.insert\n3.display\n4.update\n5.update password\n: "))

        if choice == 1:
            choice = int(input("please select table to search\n1.employee\n2.role\n3.leave\n4.emprole\n: "))
            if choice == 1:
                id = input("please enter the employee id: ")
                p.get_emp(id)

            elif choice == 2:
                id = input("please enter the role id: ")
                p.get_role(id)

            elif choice == 3:
                id = input("please enter the employee id: ")
                p.get_leaves(id)

            elif choice == 4:
                id = input("please enter the employee id: ")
                p.get_emprole(id)

            else:
                print("wrong choice")
        elif choice == 2 and isadmin:

            choice = int(input("please select table to insert\n1.employee\n2.role\n3.leave\n4.emprole\n: "))
            if choice == 1:
                p.insert_emp()

            elif choice == 2:
                p.insert_role()

            elif choice == 3:
                p.insert_leaves()

            elif choice == 4:
                p.insert_emprole()

            else:
                print("wrong choice")
        elif choice == 3 and isadmin:
            choice = int(input("please select table to display\n1.employee\n2.role\n3.leave\n4.emprole\n: "))
            if choice == 1:
                p.display("employee")

            elif choice == 2:
                p.display("role")

            elif choice == 3:
                p.display("leaves")

            elif choice == 4:
                p.display("emprole")

            else:
                print("wrong choice")
        elif choice == 4 and isadmin:
            choice = int(input("please select table to update\n1.employee\n2.role\n3.leave\n4.emprole\n: "))
            if choice == 1:
                p.update_emp()

            elif choice == 2:
                p.update_role()

            elif choice == 3:
                p.update_leave()

            elif choice == 4:
                p.update_emprole()

            else:
                print("wrong choice")

        elif choice == 5:
            p.update_password()


        else:
            print("unauthorized")
    else:
        print("invald credentials")
    p.close()