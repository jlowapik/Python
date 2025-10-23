from models import Antibiotic, Vitamin, Vaccine

def midicines(meds):
    for med in meds:
        print(med.info())
    

meds = [
    Antibiotic('Нурофен', 10, 15.3),
    Vitamin('Аскорбінка', 120, 135.3),
    Vaccine('СОнце', 10, 10.0)
]
midicines(meds)