from django.shortcuts import render
from collections import Counter
from pathlib import Path
from string import punctuation

from .models import Document
from config.settings import MEDIA_ROOT



def wordCount(request):
    file = None
    c = {}
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
            for line in file:
                for word in line.lower().split():
                    key = word.rstrip(punctuation)
                    c[key] = c.get(key, 0) + 1
                    context = {'words' : c}
    

    return render(request=request, template_name = 'app.html', context = context)


def countDelete(request):
    records = Document.objects.all()
    records.delete()
