from django.shortcuts import render
import joblib

def home(request):
    return render(request, 'home.html')

def result(request):
    # Load models
    scaler = joblib.load("scaler_model.pkl")
    model = joblib.load("glass_model.pkl")

    # Collect input features
    elements = {
        "RI":float(request.GET.get('RI')),
        "Na":float(request.GET.get('Na')),
        "Mg":float(request.GET.get('Mg')),
        "Al":float(request.GET.get('Al')),
        "Si":float(request.GET.get('Si')),
        "K":float(request.GET.get('K')),
        "Ca":float(request.GET.get('Ca')),
        "Ba":float(request.GET.get('Ba')),
        "Fe":float(request.GET.get('Fe')),
    }

    elements_list = list(elements.values())

    # Scale data
    scaled_data = scaler.transform([elements_list])

    # Predict
    prediction = model.predict(scaled_data)

    # Send result to template
    return render(request, 'result.html', {
        "ans": prediction[0],
        "elements": elements
    })
