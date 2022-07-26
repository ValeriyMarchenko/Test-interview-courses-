from django.shortcuts import render
from pathlib import Path
from .models import Document
from config.settings import MEDIA_ROOT
from . import models
import os


def wordCount(request):
    file = None
    context = {}
    if request.method == 'POST':
        file = request.FILES.get('file', False)
        doc = Document(
            file = file
        )
        doc.save()

    file_path = MEDIA_ROOT + f'/files/{file}'

    if Path(file_path).is_file():
        with open(file = file_path, mode = 'rt') as file:
            data = file.read()
            words = data.split()
            context = {'words' : len(words)}
    

    return render(request=request, template_name = 'app.html', context = context)


def countDelete(request):
    records = Document.objects.all()
    records.delete()
