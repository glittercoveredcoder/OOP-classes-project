from doctors import Doctor

class DoctorManager:
    def __init__(self):
        self.doctors = []
        self.read_doctors_from_file()

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
    