from patients import Patient

class PatientManager:
    def __init__(self):
        self.patients = []

    def format_patient_info_for_file(self, patient):
        return f"{patient.get_patient_id()}_{patient.get_patient_name()}_{patient.get_patient_disease()}_{patient.get_patient_gender()}_{patient.get_patient_age()}\n"
    
    def enter_patient_info(self):
        pid = input("Enter Patient ID: ")
        name = input("Enter Patient Name: ")
        disease = input("Enter Patient Disease: ")
        gender = input("Enter Patient Gender: ")
        age = input("Enter Patient Age: ")
        new_patient = Patient(pid, name, disease, gender, age)
        return new_patient