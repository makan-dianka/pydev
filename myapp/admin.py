from django.contrib import admin

# Register your models here.
from .models import (
    PdfToAudio, PdfToAudioAdmin, 
    Pdf , PdfAdmin, 
    Langue, LangueAdmin
    )
    
admin.site.register(PdfToAudio, PdfToAudioAdmin)
admin.site.register(Pdf, PdfAdmin)
admin.site.register(Langue, LangueAdmin)