from django.http import HttpResponse
from django.shortcuts import render


def Home(request):

    # Dynamic Data
    """
    1) Single Object
    2) List of Object
    """
    # Single Object
    ctx = {
        "sr_no": 1,
        "name": "Santoshi",
        "class": "MCA",
        "marks": {"DSA": "90%", "JAVA": "60%", "SE": "75%", "Maths": "100%"}
    }

    return render(request=request, template_name='index.html', context=ctx)


def About(request):
    list_object = [
        {
            "sr_no": 1,
            "name": "Santoshi",
            "class": "MCA",
            "marks": "90%"
        },
        {
            "sr_no": 2,
            "name": "Kanif",
            "class": "BA",
            "marks": "70%"
        },
        {
            "sr_no": 3,
            "name": "Niraj",
            "class": "Engg",
            "marks": "75%"
        },
        {
            "sr_no": 4,
            "name": "Iqbal",
            "class": "BCA",
            "marks": "60%"
        },
        {
            "sr_no": 5,
            "name": "Pratik",
            "class": "Engg",
            "marks": "80%"
        },
    ]

    ctx = {
        "lst": list_object
    }
    print(ctx)
    return render(request=request, template_name='about.html', context=ctx)


def Privacy(request):
    return render(request=request, template_name='privacy.html', context=None)


def Career(request):
    return render(request=request, template_name='career.html', context=None)
