from django.shortcuts import render
from django.http import HttpResponse

def get_name(request, name):
    return HttpResponse(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>   
<div> <h1 style="color:red;font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;font-style: initial;background-color: brown;color: wheat;">Hello world name</h1> </div>
</body>
</html>                       
                        
                     
                    """)
def get_surname(request, surname):
    return HttpResponse(f"<h1 style=color:red>{surname}</h1>")

def get_age(request, age):
    return HttpResponse(f"<h3 style=color:yellow>Hello {age}</h3>")
def get_phone(request, phone):
    return HttpResponse(f"<h1 style=color:red>Hello {phone}</h1>")


def get_grade(request, grade):
    return HttpResponse(f"""<p style="color:red; FONT">Hello {grade}</p>""")

def get_password(request, password):
    return HttpResponse(f"<p style=color:red>Hello {password}</p>")
def get_email(request, email):
    return HttpResponse(f"<p style=color:red>Hello {email}</p>")