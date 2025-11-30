from doctor_manager import DoctorManager
from patient_manager import PatientManager

class Management:
    def __init__(self):
        self.doctor_manager = DoctorManager()
        self.patient_manager = PatientManager()

    def display_menu(self):
        while True:
            print("\n=== Main Menu ===")
            print("1. Doctors Menu")
            print("2. Patients Menu")
            print("3. Exit Program")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.display_doctors_menu()
            elif choice =='2':
                self.display_patients_menu()
            elif choice == '3':
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def display_doctors_menu(self):
        while True:
            print("\n=== Doctos Menu ===")
            print("1. Display Doctors List")
            print("2. Search Doctor by ID")
            print("3. Search Doctor By Name")
            print("4. Add New Doctor")
            print("5. Edit Doctor Information")
            print("6. Return to Main Menu")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.doctor_manager.display_doctors_list()
            elif choice == '2':
                self.doctor_manager.search_doctor_by_id()
            elif choice == '3':
                self.doctor_manager.search_doctor_by_name()
            elif choice == '4':
                self.doctor_manager.add_new_doctor()
            elif choice == '5':
                self.doctor_manager.edit_doctor_info()
            elif choice == '6':
                self.display_menu()
            else: 
                print("Invalid choice. Please try again.")