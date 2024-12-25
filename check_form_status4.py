import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime

# The URL of the page to monitor
# url = "https://hopeyhdistys.fi/tarvitsen-apua/?flocation=pori"
url = "https://hopeyhdistys.fi/tarvitsen-apua/?flocation=paakaupunkiseutu"


def check_form_activation():
    try:
        # Get the current date and time
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Make a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Parse the page content with BeautifulSoup
        soup = BeautifulSoup(response.text, "html.parser")

        # Check for the presence of the form
        form = soup.find("form")
        
        if form:
            status_message = f"The HOPE form is activated! Checked at {current_time}"
            print(status_message)
            # Display a macOS notification
            os.system(f'osascript -e \'display notification "{status_message}" with title "Form Status"\'')
        else:
            status_message = f"The HOPE form is not activated. Checked at {current_time}"
            print(status_message)
            # Display a macOS notification
            # os.system(f'osascript -e \'display notification "{status_message}" with title "Form Status"\'')
            
    except requests.RequestException as e:
        error_message = f"Error checking the form: {e} at {current_time}"
        print(error_message)
        # Display a macOS notification
        os.system(f'osascript -e \'display notification "{error_message}" with title "Form Status Error"\'')

# Run the function and show the notification
check_form_activation()
