from patients import Patient

class PatientManager:
    def __init__(self):
        self.patients = []
        self.read_patients_file()

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
    
    def read_patients_file(self):
        try:
            with open("./info/patients.txt", "r") as file:
                for line in file:
                    data = line.strip().split("_")

                    # Skip header lines or malformed rows
                    if data[0].lower() in ["id", "patientid", "patient_id"]:
                        continue
                    if len(data) != 5:
                        continue

                    patient = Patient(data[0], data[1], data[2], data[3], data[4])
                    self.patients.append(patient)
        except FileNotFoundError:
            print("File patients.txt not found.")

    def search_patient_by_id(self):
        search_id = input("Enter Patient ID to search: ")
        for patient in self.patients:
            if patient.get_patient_id() == search_id:
                print(f"{'Id':<5} {'Name':<20} {'Disease':<15} {'Gender':<10} {'Age':<5}")
                print("-" * 60)
                print(self.display_patient_info(patient))
        print("Can't find the patient with the given ID")
        return None
    
    def search_patient_by_name(self):
        search_name = input("Enter Patient Name to search: ")
        for patient in self.patients:
            if patient.get_patient_name().lower() == search_name.lower():
                print(f"{'Id':<5} {'Name':<20} {'Disease':<15} {'Gender':<10} {'Age':<5}")
                print("-" * 60)
                print(self.display_patient_info(patient))
        print("Can't find the patient with the given Name")
        return None

    def display_patient_info(self, patient):
        print(f"{patient.get_patient_id():<5} "
          f"{patient.get_patient_name():<20} "
          f"{patient.get_patient_disease():<15} "
          f"{patient.get_patient_gender():<10} "
          f"{patient.get_patient_age():<5}")
        
    def edit_patient_info_by_id(self, filename="./info/patients.txt"):
        edit_id = input("Enter Patient ID to edit: ")
        for patient in self.patients:
            if patient.get_patient_id() == edit_id:
                print("Enter new details for the patient:")
                patient.set_patient_name(input("Enter Patient Name: "))
                patient.set_patient_disease(input("Enter Patient Disease: "))
                patient.set_patient_gender(input("Enter Patient Gender: "))
                patient.set_patient_age(input("Enter Patient Age: "))
                self.write_list_of_patients_to_file()
                print("Patient information has been updated.")
                return
        print("Patient not found.")

    def display_patients_list(self):
        print(f"{'ID':<5} {'Name':<20} {'Disease':<15} {'Gender':<10} {'Age':<5}")
        print("-" * 60)
        for patient in self.patients:
            self.display_patient_info(patient)
    
    def write_list_of_patients_to_file(self):
        with open("./info/patients.txt", 'w') as file:
            for patient in self.patients:
                file.write(self.format_patient_info_for_file(patient))

    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        with open("./info/patients.txt", 'a') as file:
            file.write(self.format_patient_info_for_file(new_patient))
        print(f"New patient with ID {new_patient.get_patient_id()} added successfully.")

    