class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bedNumber = 0

class Hospital(object):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.patient_list = []

    def admit(self, patient):
        if len(self.patient_list) >= self.capacity:
            print "Hospital is full"
        else:
            self.patient_list.append(patient)
            print "Admission is complete"
            print "Patient count is " + str(len(self.patient_list))
            patient.bedNumber = patient.id
            print "Patient bed number: " + str(patient.bedNumber)
        return self
    def display(self):
        print "Number of patients: " + str(len(self.patient_list))
        print "Patients: "
        for i in range(0, len(self.patient_list)):
            print "ID: ", str(self.patient_list[i].id)
            print "Name: ", str(self.patient_list[i].name)
            print "Allergies: ", str(self.patient_list[i].allergies)
            print "Bed #: ", str(self.patient_list[i].bedNumber)
        return self
    def discharge(self, id):
        for i in range(0, len(self.patient_list)-1):
            if(self.patient_list[i].id == id):
                print "Patient " + str(self.patient_list[i].name) + " has been discharged"
                self.patient_list[i].bedNumber = 0
                print "Patient bed number is now " + str(self.patient_list[i].bedNumber)
                self.patient_list.remove(self.patient_list[i])
        return self

mmc = Hospital('Manati', 300)
mmc.display()

patient1 = Patient("1", "Melissa", "Eggs")
patient2 = Patient("2", "Sky", "None")

mmc.admit(patient1)
mmc.admit(patient2)

mmc.display()
mmc.discharge("1")
mmc.display()
