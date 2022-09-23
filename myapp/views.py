from django.shortcuts import render , redirect
import logging
from .forms import PdfForm
from .filehundler import handle_uploaded_file, pdfReader, text_to_audio
from .models import Pdf, PdfToAudio, Langue
from django.contrib.auth.models import User


log = logging.getLogger('log')

def index(request):
    log.error("Message for error")
    pdf_obj = Pdf.objects.filter(owner=request.user.id)
    
    if request.method=="POST": 
        form = PdfForm(request.POST, request.FILES)
        if form.is_valid:
            name, ex = str(request.FILES['pdf']).split('.')
            lang_id = request.POST.get('langue')
            user_id = request.POST.get('owner')
            lang = Langue.objects.get(pk=lang_id)
           
            file_handler = handle_uploaded_file(request.FILES['pdf'], name, ex)
            doc = Pdf()
            doc.pdf = file_handler
            doc.langue = Langue.objects.get(pk=lang_id)
            doc.owner = User.objects.get(pk=user_id)
            doc.save()  
                      
            return redirect(f'/pdf/{doc.id}')
    else:
        form = PdfForm()
    context = {'form':form, 'last_audio':pdf_obj}
    return render(request, 'myapp/index.html', context)



def audio(request, id):
    pdf_obj = Pdf.objects.get(pk=id, owner=request.user)
    audios = PdfToAudio.objects.filter(owner=request.user).order_by('-id')
    file_name_with_extension = pdf_obj.pdf.name.split('/')[1]
    file_name = file_name_with_extension.split('.')[0]
    
    if request.method=='POST':
        lang_code = pdf_obj.langue.code
       
        text = pdfReader(f"media/pdf/{file_name_with_extension}")
        mp = text_to_audio(text, f"media/audio/{file_name}.mp3", lang_code)
        
        audio = PdfToAudio()
        audio.pdf = pdf_obj
        audio.audio = mp
        audio.owner = User.objects.get(id=request.user.id)
        audio.save()
        pdf_obj.status = True
        pdf_obj.save()
        return redirect(f'/pdf/{pdf_obj.id}')
    context = {'file_name': file_name_with_extension, 'pdf_obj':pdf_obj, 'audio':file_name, 'audios':audios}
    return render(request, 'myapp/audio.html', context)


def delete(request, id):
    obj = PdfToAudio.objects.get(id=id)
    obj.delete()
    return redirect('/')