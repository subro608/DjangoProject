from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def homepage_view(*args, **kwargs):
    html = '''
    <html lang="en" className="scroll-smooth">
    <head>
        <style>
            body {
                background-color: #e6e6e6;
                font-family: Arial, sans-serif;
            }
            .title {
                font-size: 3em;
                text-align: center;
                animation: fadein 2s;
                color: #2ecc71;
            }
            .subtitle {
                font-size: 1.5em;
                text-align: center;
                animation: fadein 2s;
                animation-delay: 1s;
                color: #8bc34a;
            }
            .jumbotron {
                background-color: #ecf0f1;
                padding: 20px;
                text-align: center;
                border-radius: 20px;
            }
            .input-group {
                width: 50%;
                margin-left: auto;
                margin-right: auto;
            }
            .form-control {
                border-radius: 20px;
                background-color: #ecf0f1;
                border-color: #8bc34a;
                color: #2ecc71;
            }
            .btn {
                border-radius: 20px;
                background-color: #2ecc71;
                border-color: #2ecc71;
                color: #ecf0f1;
            }
            @keyframes fadein {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
        </style>
    </head>
    <body>
    <div class="container">
        <div class="jumbotron">
            <h1 class="title">Grocery List</h1>
            <p class="subtitle">For students, by students</p>
            <form action="/add_item" method="post">
                <div class="input-group">
                    <input type="text" class="form-control" placeholder="Grocery Item" name="item_name" required>
                    <span class="input-group-btn">
                        <button class="btn btn-primary" type="submit">Add Item</button>
                    </span>
                </div>
            </form>
        </div>
    </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def contact_view(*args, **kwargs):
    html = '''
    <html lang="en" className="scroll-smooth">
    <head>
        <style>
            body {
                background-color: #e6e6e6;
                font-family: Arial, sans-serif;
            }
            .title {
                font-size: 3em;
                text-align: center;
                animation: fadein 2s;
                color: #2ecc71;
            }
            .subtitle {
                font-size: 1.5em;
                text-align: center;
                animation: fadein 2s;
                animation-delay: 1s;
                color: #8bc34a;
            }
            .jumbotron {
                background-color: #ecf0f1;
                padding: 20px;
                text-align: center;
                border-radius: 20px;
            }
            .contact {
                text-align: center;
                padding: 20px;
            }
            .contact a {
                text-decoration: none;
                color: #2ecc71;
            }
            .contact a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
    <div class="container">
        <div class="jumbotron">
            <h1 class="title">Contact Us</h1>
            <p class="subtitle">Subhrajit Dey, Founder</p>
            <div class="contact">
                <p>Phone Number: <a href="tel:9296695456">929-669-5456</a></p>
                <p>Email: <a href="mailto:sd5963@nyu.edu">sd5963@nyu.edu</a></p>
                <p>Can be contacted anytime</p>
            </div>
        </div>
    </div>
    </body>
    </html>
    '''
    return HttpResponse(html)

def home_view(request, *args, **kwargs):
    my_context = {
        "title": "Home",
        "my_number": 123,
        "my_text": "This is the home page. Welcome",
        "my_list": [12,33,43,5,67,7,87]
    }
    return render(request, "home.html", my_context)
