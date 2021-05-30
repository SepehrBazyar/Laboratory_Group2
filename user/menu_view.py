from time import sleep
from hashlib import sha256
from getpass import getpass
import user.models as models
from Lab.models import CV19


def register():
    # user_type =
    first_name = input("enter your first name:")
    last_name = input("enter your last name:")
    phone = input("enter your phone number:")
    email = input("enter your email(optional):") or None
    password = sha256(getpass("enter your password:").encode()).hexdigest()
    # password = "1234"  # it is just for test

    return first_name, last_name, phone, email, password

    # todo : we should get an id to the user or using phone as username. we need this for login
    # todo: we need to add some char to username for distinguishing type of user: fro example p0911111 for patient


def patient_register():
    first_name, last_name, phone, email, password = register()
    gender = input("enter your gender(male or female):")
    age = int(input("enter your  age:"))
    blood_type = input("enter your blood type(A,B,AB or O) :")
    models.Patient(first_name, last_name, phone, password, gender, age, blood_type, email)
    print("Congrats. Your Account Is Created")


def doctor_register():
    first_name, last_name, phone, email, password = register()
    expertise = input("enter your expertise:")
    models.Doctor(first_name, last_name, phone, email, expertise)
    print("Congrats. Your Account Is Created")


def operator_register():
    first_name, last_name, phone, email, password = register()
    licence = input("enter your licence:")
    models.Operator(first_name, last_name, phone, email, licence)
    print("Congrats. Your Account Is Created")


def manager_register():
    first_name, last_name, phone, email, password = register()
    educational_degree = input("enter your educational degree:")
    models.Doctor(first_name, last_name, phone, email, educational_degree)
    print("Congrats. Your Account Is Created")


def repr_all_users():
    patients = models.Patient.patients
    for i in range(len(patients)):
        print(f"""
{i + 1}-
<first name:{patients[i]["first_name"]}, 
 last  name:{patients[i]["last_name"]}>
""")


Patient_list = []
Tests = []


def cv19_view():
    print("Enter your profile : ")
    first_name = input("First Name : ")
    last_name = input("Last Name : ")
    phone = input("Phone : ")
    email = input("Email(Optional) : ")

    patient = models.Patient(first_name, last_name, phone, email)
    Patient_list.append(patient)

    print("Your profile saved !")
    print("Testing patient ", end="")

    [sleep(1) or print(".", end="") for i in range(3)]

    cv19 = CV19(patient)

    print("Done ! ")

    Tests.append(cv19)
    print("Estimated result time : ", cv19.estimate_time)
