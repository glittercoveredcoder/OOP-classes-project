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