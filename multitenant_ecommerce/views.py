from django.http import HttpResponse
from django.shortcuts import render


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


def Home(request):

    """
        1) Single Object
        2) List of Object
    """

    ctx = {
        "sr_no": 1,
        "name": "Santoshi",
        "class": "MCA",
        "marks": {"DSA": "90%", "JAVA": "60%", "SE": "75%", "Maths": "100%"}
    }

    return render(request=request, template_name='index.html', context=ctx)


def About(request):

    ctx = {
        "lst": list_object
    }
    return render(request=request, template_name='about.html', context=ctx)


def getSingleAbout(request, santoshi):
    ctx = {}
    for ele in list_object:
        if int(santoshi) == ele["sr_no"]:
            ctx = ele

    return render(request=request, template_name='privacy.html', context=ctx)


def Privacy(request):
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
    """
    context = {
        "template_variable": data
    }
    """
    context = {
        "sr_no": 6,
        "name": "Saurabh",
        "class": "Electronics Engg",
        "marks": "98%",
        "santoshi": list_object
    }

    return render(request=request, template_name='privacy.html', context=context)


def Career(request):
    return render(request=request, template_name='career.html', context=None)
