# views.py

from django.shortcuts import render
import requests

def warranty(request):
    # Input parameters
    orderId = "LC119339"
    authenticationId = "AD2570"

    # API endpoint
    url = f"https://adesurat.com/API.php?call=get_warranty_details&orderId={orderId}&authenticationId={authenticationId}"

    # Make a GET request to the API
    response = requests.get(url)

    # Check if request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        # Extract data from the "data" object
        warranty_data = data.get("data", {})
        status = data.get("status", False)
        # Pass data to template
        return render(request, 'index.html', {'status': status, 'warranty_data': warranty_data})
    else:
        # If request fails, handle it appropriately
        return render(request, 'error_template.html')
