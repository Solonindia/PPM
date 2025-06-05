from django.shortcuts import render
import math

def dew_point_to_ppm(dew_point_celsius, pressure_pa=101325):
    numerator = 23.036 * dew_point_celsius - 333.7
    denominator = dew_point_celsius + 279.82
    vapor_pressure = 611.15 * math.exp(numerator / denominator)
    ppmv = (vapor_pressure / pressure_pa) * 1e6
    return ppmv

def index(request):
    result = []
    input_values = ""
    
    if request.method == 'POST':
        input_values = request.POST.get('dewpoints', '')
        try:
            dew_points = [float(dp.strip()) for dp in input_values.split(',')]
            for dp in dew_points:
                ppm = dew_point_to_ppm(dp)
                result.append((dp, round(ppm, 2)))
        except ValueError:
            result = "Invalid input. Please enter numbers separated by commas."

    return render(request, 'index.html', {
        'results': result,
        'input_values': input_values
    })

