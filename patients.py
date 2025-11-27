class Patient:
    def __init__(self, pid, name, disease, gender, age):
        self.pid = pid
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age
    
    # Getters

    def get_patient_id(self):
        return self.pid
    
    def get_patient_name(self):
        return self.name
    
    def get_patient_disease(self):
        return self.disease
    
    def get_patient_gender(self):
        return self.gender
    
    def get_patient_age(self):
        return self.age
    
    # Setters

    def set_patient_id(self, new_id):
        self.pid = new_id

    def set_patient_name(self, new_name):
        self.name = new_name
    
    def set_patient_disease(self, new_disease):
        self.disease = new_disease

    def set_patient_gender(self, new_gender):
        self.gender = new_gender

    def set_patient_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.pid}_{self.name}_{self.disease}_{self.gender}_{self.age}"