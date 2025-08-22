from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    return HttpResponse("""
        <html>
        <head>
            <style>
                body {
                    background-color: #f5f5f5;
                    font-family: Arial, Helvetica, sans-serif;
                    margin: 0;
                    padding: 0;
                }
                .container {
                    max-width: 400px;
                    margin: 60px auto;
                    background: #fff;
                    padding: 32px;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    text-align: center;
                }
                h1 {
                    color: #333366;
                }
                label {
                    font-size: 1.1em;
                    color: #222;
                }
                input[type='text'] {
                    padding: 8px;
                    margin: 12px 0;
                    border: 1px solid #ccc;
                    border-radius: 4px;
                    width: 80%;
                }
                button {
                    background-color: #333366;
                    color: #fff;
                    border: none;
                    padding: 10px 18px;
                    border-radius: 4px;
                    cursor: pointer;
                    font-size: 1em;
                }
                button:hover {
                    background-color: #555599;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Welcome to Home page</h1>
                <form method='post' action='/greet/'>
                    <label>Enter your name:</label><br>
                    <input type='text' name='name'><br>
                    <button type='submit'>Submit</button>
                </form>
            </div>
        </body>
        </html>
    """)

@csrf_exempt
def greet(request):
    name = request.POST.get("name")
    return HttpResponse(f"""
        <html>
        <head>
            <style>
                body {{
                    background-color: #f5f5f5;
                    font-family: Arial, Helvetica, sans-serif;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 400px;
                    margin: 60px auto;
                    background: #fff;
                    padding: 32px;
                    border-radius: 8px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    text-align: center;
                }}
                h2 {{
                    color: #333366;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h2>Hello, {name}! Nice to meet you.</h2>
            </div>
        </body>
        </html>
    """)