from django.shortcuts import render
import joblib
# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    model = joblib.load("regression_model.pkl")
    scaler = joblib.load("scaler_model.pkl")

    details = []
    details.append(request.GET.get("course"))
    details.append(request.GET.get("hours"))

    scaled = scaler.transform([details])
    predicted = model.predict(scaled)[0]

    return render(request, 'result.html', {"result":predicted})