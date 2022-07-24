from django.db import models

# MVT - Model--->>View--url--->>Template

# Employee ---> name,age,address,salary,contact number,joining date,work_profile,timestamp
# Task -->> task,attendance

class Employee(models.Model):
    designation_choises = (
        ("Software Engineer","Software Engineer"),
        ("Quality Analyst","Quality Analyst"),
        ("Product Manager","Product Manager")
    )
    fname =  models.CharField(max_length=60,verbose_name="First Name",blank=True,null=True)
    lname = models.CharField(max_length=60,verbose_name="Last Name",blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True,verbose_name="Age")
    salary = models.DecimalField(decimal_places=2,max_digits=10,blank=True,null=True)
    email = models.EmailField(verbose_name="Email",blank=True,null=True)
    joining_date = models.DateField(verbose_name="Joining Date",blank=True,null=True)
    designation = models.CharField(max_length=100,verbose_name="Designation",choices=designation_choises,blank=True,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self) -> str:
        return str(self.fname +" "+self.lname)
    
class Task(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE) # many to one 
    attendance = models.BooleanField(default=False,verbose_name="Task Attended")
    title = models.CharField(max_length=100,verbose_name="Title",blank=True,null=True)
    task = models.TextField(blank=True,null=True,verbose_name="Task")
    death_line = models.DateField(blank=True,null=True,verbose_name="Last Date For Submiting")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-timestamp"]
    
    def __str__(self) -> str:
        return str(self.employee.fname +"-"+"Task Title-"+self.title)