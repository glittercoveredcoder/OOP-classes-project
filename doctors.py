class Doctor:
    def __init__(self, doctor_id=None, name=None, specialization=None, working_time=None, qualification=None, room_number=None):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Getters

    def get_doctor_id(self):
        return self.doctor_id
    
    def get_doctor_name(self):
        return self.name
    
    def get_doctor_specialization(self):
        return self.specialization
    
    def get_doctor_working_time(self):
        return self.working_time
    
    def get_doctor_qualification(self):
        return self.qualification
    
    def get_doctor_room_number(self):
        return self.room_number
    