class Patients:
    def __init__(self, pid=None, name=None, disease=None, gender=None, age=None):
        self.pid=pid
        self.name=name
        self.disease=disease
        self.gender=gender
        self.age=age

    #getters
    def get_pid(self):
        return self.pid
    def get_name(self):
        return self.name
    def get_disease(self):
        return self.disease
    def get_gender(self):
        return self.gender 
    def get_age(self):
        return self.age 
    
    #setters
    def set_pid(self, new_pid):
        self.pid= new_pid
    def set_name(self, new_name):
        self.name = new_name
    def set_disease(self, new_disease):
        self.disease =new_disease
    def set_gender(self, new_gender):
        self.gender =new_gender
    def set_age(self, new_age):
        self.age=new_age 

    def __str__(self):
        """return patient prop"""
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"