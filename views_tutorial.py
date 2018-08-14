from django.shortcuts import render
from django.urls import reverse_lazy
# from django.http import HttpResponse
# from django.template import loader
from .forms import TutorialUploadForm, LevelSelectionForm
from django.http import HttpResponseRedirect
from django.core.files import File
# from django.core.files.base import ContentFile
# from django.core.files.storage import default_storage
from . import models
# import os
# import unicodedata
import zipfile
from . views import base_function


def thanks(request):
    context = base_function(request)
    context.update({
        'tutorial_name': "tutorial.pdf",
        'tutorial_screenshot': "screenshot.png",
        'tutorial_resources': "resources.zip"
    })
    return render(request, "coderdojomobile/thanks_tutorial.html", context)


def handle_uploaded_file(uploaded, description):
    files = {}
    with zipfile.ZipFile(uploaded, 'r') as z:
        # we need to extract:
        # The tutorial file.
        # The screenshot file
        # The resources file
        # Save all of them to media folder (not the original zip file!)
        # Save data on the DB
        # TODO handle malformed zip
        resource_entity = None
        tutorial_entity = None
        project_name = None
        for f in z.namelist():
            info = z.getinfo(f)
            if info.is_dir():
                project_name = f.split('/')[0]
            if f.endswith('pdf'):
                with z.open(f) as pdfFileInZip:
                    pdfFile = File(pdfFileInZip)
                    tutorial_entity = models.GenericUserFile(
                        title=f,
                        file=pdfFile
                    )
                    # now g.file is a FieldFile object https://bit.ly/2LGt9QE
                    # We need to set the base folder as generic files have
                    # no base folder
                    tutorial_entity.file.field.upload_to = "tutorial/"
                    tutorial_entity.save()  # automatically saves the file
            if f.endswith('png'):
                with z.open(f) as pdfFileInZip:
                    pngFile = File(pdfFileInZip)
                    screenshot_entity = models.GenericUserFile(
                        title=f,
                        file=pngFile
                    )
                    screenshot_entity.file.field.upload_to = "tutorial/"
                    screenshot_entity.save()
            if f.endswith('zip'):
                with z.open(f) as pdfFileInZip:
                    resourceFile = File(pdfFileInZip)
                    resource_entity = models.GenericUserFile(
                        title=f,
                        file=resourceFile
                    )
                    resource_entity.file.field.upload_to = "tutorial/"
                    resource_entity.save()
        # Now save the tutorial
        learningMaterial = models.LearningMaterial()
        learningMaterial.title = project_name
        learningMaterial.description = description
        learningMaterial.tutorial = tutorial_entity
        learningMaterial.screenshot = screenshot_entity
        learningMaterial.save()
        learningMaterial.resources.add(resource_entity)
        learningMaterial.save()
        # For now just save the file to GenericUserFiles
        # g = GenericUserFile(title="tutorial.pdf", file = pdfFile)
        # g.save()

    return files


def tutorials(request, topic_id, material_level=None):
    context = base_function(request)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TutorialUploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            files = handle_uploaded_file(
                request.FILES['tutorial_file'],
                request.POST['tutorial_description']
            )
            if not files:
                raise Exception("No uploaded files!")
            return HttpResponseRedirect(reverse_lazy('coderdojomobile:thanks'))
    # if a GET (or any other method) we'll create a blank form
    else:
        # but still we have to filter checking whether a specific level was
        # requested by url or by form
        try:
            # read from form get
            requested_material_level = request.GET['level']
        except KeyError:
            requested_material_level = None
        if (
                (requested_material_level is None) or
                (requested_material_level == LevelSelectionForm.LEVEL_ALL)
        ):
            projects = models.LearningMaterial.objects.all().filter(
                topic_id=topic_id,
                is_active=True
            ).order_by('level', 'title')
        else:
            projects = models.LearningMaterial.objects.all().filter(
                topic_id=topic_id,
                is_active=True,
                level=requested_material_level
            ).order_by('level', 'title')
        form = TutorialUploadForm()
        search_form = LevelSelectionForm()
        context.update({'projects': projects,
                        'form': form,
                        'topic_id': topic_id,
                        'search_form': search_form})
        return render(request, 'coderdojomobile/tutorials.html', context)


def tutorial(request, tutorial_id):
    context = base_function(request)
    tutorial = models.LearningMaterial.objects.get(id=tutorial_id)
    context.update({'project': tutorial,
                    'project_resources': tutorial.resources.all()})
    return render(request, "coderdojomobile/tutorial.html", context)
