from django.db import models

# Create your models here.
class Doctor(models.Model):
	name = models.TextField()
	
	def __str__(self):
		return f'{self.name} 전문의'
  
class Patient(models.Model):
	doctors = models.ManyToManyField(Doctor, through='Reservation',related_name='patients' ) # 환자입장에서는 doctors로 쓰는거 처럼 의사 입장에서도 set_all대신 patients로 접근가능하게 이름변경 
	name = models.TextField()
	
	# doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

	def __str__(self):
		return f'{self.pk}번 환자 {self.name}'

class Reservation(models.Model):
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	symptom = models.TextField()
	reserved_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return f'{self.doctor.pk}번 의사의 {self.patient.pk}번 환자'





# # 관계를 만들어 줌
# class Reservation(models.Model):
# 	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
# 	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return f'{self.doctor_id}번 의사의 {self.patient_id}번 환자'
