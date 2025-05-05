from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField("Nome", max_length=50)
    last_name = models.CharField("Sobrenome", max_length=50)
    email = models.EmailField("Email", unique=True)
    password = models.CharField("Senha", max_length=128)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Patient(models.Model):
    patient_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField("Data de Nascimento")
    gender = models.CharField("Gênero", max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro')])

    def __str__(self):
        return f"Paciente #{self.patient_id} (Usuário: {self.user})"

class Professional(models.Model):
    professional_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField("Especialidade", max_length=100)
    crm = models.CharField("CRM", max_length=20, unique=True)

    def __str__(self):
        return f"{self.specialty} #{self.professional_id} (Usuário: {self.user})"

class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='appointments')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    appointment_date = models.DateTimeField("Data e Hora da Consulta")
    notes = models.TextField("Anotações", blank=True, null=True)

    def __str__(self):
        return f"Consulta #{self.appointment_id} - Paciente: {self.patient} - Profissional: {self.professional}"

class Availability(models.Model):
    availability_id = models.AutoField(primary_key=True)
    professional = models.OneToOneField(Professional, on_delete=models.CASCADE, related_name='availability')
    day_of_week = models.IntegerField("Dia da Semana", choices=[(0, 'Domingo'), (1, 'Segunda'), (2, 'Terça'), (3, 'Quarta'), (4, 'Quinta'), (5, 'Sexta'), (6, 'Sábado')])
    start_time = models.TimeField("Hora de Início")
    end_time = models.TimeField("Hora de Fim")

    def __str__(self):
        return f"Disponibilidade #{self.availability_id} - Profissional: {self.professional} - {self.get_day_of_week_display()} ({self.start_time} - {self.end_time})"

class Clinic(models.Model):
    clinic_id = models.AutoField(primary_key=True)
    name = models.CharField("Nome", max_length=200)
    address = models.CharField("Endereço", max_length=255)
    phone_number = models.CharField("Telefone", max_length=20)
    professionals = models.ManyToManyField(Professional, related_name='clinics')

    def __str__(self):
        return self.name