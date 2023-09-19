from doctores.models import Doctor, Specialty


def run():
    Specialty.objects.create(name='Cardiología')

    Specialty.objects.create(name='Dermatología')

    Specialty.objects.create(name='Endocrinología')

    Specialty.objects.create(name='Gastroenterología')

    Doctor.objects.create(
        identification=123456789,
        name='Juan',
        last_name='Perez',
        email='JuanP@censo.com',
        specialty_id=1
    )

    Doctor.objects.create(
        identification=987654321,
        name='Maria',
        last_name='Gomez',
        email='MarG@censo.com',
        specialty_id=2
    )

    Doctor.objects.create(
        identification=823455789,
        name='Pedro',
        last_name='Garcia',
        email='PedroG@censo.com',
        specialty_id=3
    )

    Doctor.objects.create(
        identification=789455789,
        name='Andres',
        last_name='Durango',
        email='AndresD@censo.com',
        specialty_id=4
    )
