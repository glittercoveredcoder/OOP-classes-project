from Patients import Patients

class PatientManager:
    def __init__(self):
        self.patients=[]
        self.read_patient_file()
    def format_patient_info_for_file(self,patient):
        return f"{patient.pid}_{patient.name}_{patient.disease}_{patient.gender}_{patient.age}"
    
    def enter_patient_info(self):
        pid=input("enter patient ID: ")
        name=input("enter patient name: ")
        disease=input("enter patient disease: ")
        gender=input("enter patient gender: ")
        age=input("enter patient age: ")

        return Patients(pid=pid, name=name, disease=disease, gender=gender, age=age)
    


    def read_patients_file_(self):
        if not os.path.exists("patients.txt"):
            return
        
        with open("patients.txt", "r") as file:
            for line in file:
                parts=line.strip().split("_")
                if len(parts)==5:
                    pid, name, disease, gender, age = parts
                    self.patients.append(Patients(pid, name, disease, gender, age))

    def search_patient_by_ID(self):
        patient_ID=input("enter patient ID: ")
        for patient in self.patients:
            if patient.pid==patient_ID:
                self.display_patient_info(patient)
        print("cannot find thee patient")

    def display_patient_info(self, patient):
        print("patient info")
        print(f"ID: {patient.pid}")
        print(f"name:{patient.name}")
        print(f"disease:{patient.disease}")
        print(f"gender:{patient.gender}")
        print(f"age: {patient.age}")
        print()

    def edit_patient_info_by_ID(self):
        edit_ID=input("enter patients ID to edit it: ")
        for patient in self.patients:
            if patient.pid==edit_ID:
                print("enter new patient information: ")
                patient.name=input("new patient name: ")
                patient.disease=input("new patient disease: ")
                patient.gender=input("new patient gender: ")
                patient.age=input("new patient age: ")
                
                self.write_list_of_patients_to_file()
                print("patient was edited.")
                return
        print("patient cannot be found")


    def show_patients_list(self):
        print("Patient list")
        for patients in self.patients:
            self.display_patient_info(patients)
    def write_list_of_patients_to_file(self):
        with open("patients.txt", "w") as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient)+"\n")
    def add_patients_file(self):
        new_patient=self.enter_patient_info()
        self.patients.append(new_patient)

        with open("patient.txt", "a") as file:
            file.write(self.format_patient_info_for_file(new_patient)+"\n")
        print("new patient has been added successfully")        