from doctors import Doctor

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_file("./info/doctors.txt")

    def format_dr_info(self, doctor):
        return f"{doctor.get_doctor_id()}_{doctor.get_doctor_name()}_{doctor.get_doctor_specialization()}_" \
               f"{doctor.get_doctor_working_time()}_{doctor.get_doctor_qualification()}_{doctor.get_doctor_room_number()}\n"
    
    def enter_dr_info(self):
        doctor_id = input("Enter doctor ID: ")
        name = input("Enter doctor name: ")
        specialization = input("Enter doctor specialization: ")
        working_time = input("Enter doctor working time: ")
        qualification = input("Enter doctor qualification: ")
        room_number = input("Enter doctor room number: ")
        return Doctor(doctor_id, name, specialization, working_time, qualification, room_number)
    
    def read_doctors_file(self, filename):
        try:
           with open(filename, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                # Skip header
                if line.lower().startswith("id_"):
                    continue

                data = line.split("_")
                # Only load if we have at least 6 fields
                if len(data) >= 6:
                    doctor = Doctor(data[0].strip(), data[1].strip(), data[2].strip(),
                                    data[3].strip(), data[4].strip(), data[5].strip())
                    self.doctors.append(doctor)
        except FileNotFoundError:
            print("doctors.txt not found. Starting with empty list.")

    def search_doctor_by_id(self, doctor_id=None):
        if doctor_id is None:
            doctor_id = input("Enter doctor ID to search: ")
        for doctor in self.doctors:
            if doctor.get_doctor_id().strip() == doctor_id:
                print(f"{'Id':<5} {'Name':<20} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room Number':<10}")
                print("-" * 80)
                self.display_doctor_info(doctor)
                return doctor
            
        print("Can't find the doctor with the given ID")
        return None
    
    def search_doctor_by_name(self, name=None):
        if name is None:
            name = input("Enter doctor name to search: ")
        for doctor in self.doctors:
            if doctor.get_doctor_name().lower() == name.lower():
                print(f"{'Id':<5} {'Name':<20} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room Number':<10}")
                print("-" * 80)
                self.display_doctor_info(doctor)
                return doctor
            
        print("Can't find the doctor with the given name")
        return None
    
    def display_doctor_info(self, doctor):
        print(f"{doctor.get_doctor_id():<5} "
              f"{doctor.get_doctor_name():<20} "
              f"{doctor.get_doctor_specialization():<15} "
              f"{doctor.get_doctor_working_time():<15} " 
              f"{doctor.get_doctor_qualification():<15} " 
              f"{doctor.get_doctor_room_number():<10}")
        
    def edit_doctor_info(self, doctor_id=None):
        if doctor_id is None:
            doctor_id = input("Enter doctor ID to edit: ")
        doctor = self.search_doctor_by_id(doctor_id)
        if doctor:
            doctor.set_doctor_name(input("Enter new name: "))
            doctor.set_doctor_specialization(input("Enter new specialization: "))
            doctor.set_doctor_working_time(input("Enter new working time: "))
            doctor.set_doctor_qualification(input("Enter new qualification: "))
            doctor.set_doctor_room_number(input("Enter new room number: "))
            self.write_list_of_doctors_to_file()
            print(f"Doctor with ID {doctor_id} has been edited.")
        else:
            print("Cannot find the doctor with the given ID.")

    def display_doctors_list(self):
        print(f"{'ID':<5} {'Name':<20} {'Speciality':<15} {'Timing':<15} {'Qualification':<15} {'Room Number':<10}")
        print("-" * 80)
        for doctor in self.doctors:
            self.display_doctor_info(doctor)

    def write_list_of_doctors_to_file(self):
        with open("./info/doctors.txt", "w") as file:
            for doctor in self.doctors:
                file.write(self.format_dr_info(doctor) + "\n")

    def add_dr_to_file(self):
        new_doctor = self.enter_dr_info()
        self.doctors.append(new_doctor)
        with open("./info/doctors.txt", "a") as file:
            file.write(self.format_dr_info(new_doctor) + '\n')
        print(f"Doctor with ID {new_doctor.get_doctor_id()} has been added.")