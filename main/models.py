from django.db import models

class Talaba(models.Model):
    ism=models.CharField(max_length=355)
    guruh=models.CharField()
    kurs=models.CharField(choices=(('1', '1'), ('2', '2'),('3','3'),('4','4')))
    kitob_soni=models.IntegerField()

    def __str__(self):
        return self.ism


class Muallif(models.Model):
    ism=models.CharField(max_length=30)
    jins=models.CharField(choices=(('ayol','Ayol'),('erkak','Erkak')))
    tugilgan_sana=models.CharField(default=30)
    kitob_soni=models.PositiveSmallIntegerField()
    tirik=models.BooleanField(default=False)

    def __str__(self):
        return self.ism

class Kitob(models.Model):
    nom=models.CharField()
    janr=models.CharField()
    sahifa=models.PositiveSmallIntegerField()
    muallif=models.ForeignKey(Muallif, on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.nom

class Kutubxonachi(models.Model):
    ism=models.CharField()
    ish_vaqti=models.CharField(choices=(('8:00/13:30','8:00/13:30'),('13:30/19:00','13:30/19:00')))

    def __str__(self):
        return self.ism

class Record(models.Model):
    talaba=models.ForeignKey(Talaba,on_delete=models.SET_NULL,null=True)
    kitob=models.ForeignKey(Kitob,on_delete=models.SET_NULL,null=True)
    Admin=models.ForeignKey(Kutubxonachi,on_delete=models.SET_NULL,null=True)
    olingan_sana=models.DateField(auto_now_add=True)
    qaytarish_sana=models.DateField()

    def __str__(self):
        return str(self.talaba)












