from doctores.models import Specialty
Specialty.objects.all().delete()
speciality1 = Specialty(name='Cardiologia')
speciality1.save()

from doctores.models import Doctor
Doctor.objects.all().delete()
Doctor.objects.create(identification=1234567833339, photo='', name='Juan', last_name='Perez', email='Juan@perez.com', specialty=speciality1)

