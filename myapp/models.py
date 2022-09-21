from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# langue
class Langue(models.Model):
    langue = models.CharField(max_length=300)
    code = models.CharField(max_length=300, default='fr')
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.langue)

class LangueAdmin(admin.ModelAdmin):
    list_display = ("langue",)

# PDF
class Pdf(models.Model):
    langue = models.ForeignKey(Langue, on_delete=models.DO_NOTHING)
    pdf = models.FileField(upload_to="pdf")
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.pdf)

class PdfAdmin(admin.ModelAdmin):
    list_display = ('langue', "pdf", 'status', 'owner')
    
# Audio
class PdfToAudio(models.Model):
    pdf = models.ForeignKey(Pdf, on_delete=models.DO_NOTHING)
    audio = models.FileField(upload_to="audio")
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)
    status = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now=True)

class PdfToAudioAdmin(admin.ModelAdmin):
    list_display = ('pdf', "audio", 'status', 'owner', 'create_at')