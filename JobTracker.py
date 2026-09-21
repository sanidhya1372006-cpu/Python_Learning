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



J1=JobApplication("Google","Software Engineer","Applied","26 August","22 Oct","Need Experience")
J2=JobApplication("TCS","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J4=JobApplication("Hcl","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J3=JobApplication("Salesforce","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
L=[J1,J2,J3,J4]

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


