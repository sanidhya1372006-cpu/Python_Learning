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


J1=JobApplication("Google","Software Engineer","Applied","26 August","22 Oct","Need Experience")
J1.display()
J2=JobApplication("TCS","QA","Applied","23 August","22 Sept","Need To Be Good In Automation")
J2.display()
