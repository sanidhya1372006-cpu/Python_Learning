class JobApplication:
    def __init__(self,company,role,status,application_date,deadline,notes):
        self.company=company  
        self.role=role
        self.status=status
        self.application_date=application_date
        self.deadline=deadline
        self.notes=notes


    def display(self):
        print("Company Name:",self.company)
        print("Role:",self.role)
        print("Status:",self.status)
        print("Date:",self.application_date)
        print("Deadline:",self.deadline)
        print("Notes:",self.notes)
        print()



    def update_status(self,status):
        self.status=status

def show_by_status(L,statu):
    for i in L:
        if i.status==statu:
            i.display()


def show_by_company(L,company):
    for i in L:
        if i.company==company:
            i.display()    



def count_by_status(L,status):
    counter=0
    for i in L:
        if i.status==status:
            counter+=1
    print(status,":",counter)







J1=JobApplication("Google","Software Engineer","Shortlisted","26 August","22 Oct","Need Experience")
J2=JobApplication("TCS","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J4=JobApplication("Hcl","QA","Not Applied","23 August","22 Sept","Need To Be Good In Automation")
J3=JobApplication("Salesforce","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
L=[J1,J2,J3,J4]

for i in L:
    i.display()


def summary(L):
    print("Total Application:",len(L))
    print()
    count_by_status(L,"Applied")
    count_by_status(L,"Shortlisted")
    count_by_status(L,"Not Applied")
    count_by_status(L,"Rejected")


def show_all(L):
    for i in L:
        i.display()





J5=JobApplication("Microsoft","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J5.display()
J5.update_status("Pending")
J5.display()

J5=JobApplication("DronaHQ","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J5.display()
J5.update_status("ShortListed")
J5.display()


print()
print("Status check")

show_by_status(L,"Shortlisted")

print("According To Company Name:")
print()
show_by_company(L,"TCS")


print("Total Status:")
count_by_status(L,"Not Applied")
print()

print("===Summary===")
summary(L)

