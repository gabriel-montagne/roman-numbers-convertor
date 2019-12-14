# Google cloud function for converting numbers to roman numerals

### Scope

This project aims to provide a simple cloud service to compute a roman numeral 
from a given integer in the range of [1 ... 3999]

        
### Testing
#### Prerequisites

 - Python3 environment

To run the tests:

    > make test
    
You can test the cloud function using Postman or just a simple curl command:

    > curl -X POST 'https://us-central1-roman-numeral-2019.cloudfunctions.net/handler'  -H 'Content-Type: application/json' -d '{"digits_string": "849"}'

To run in local environment:
    
    1. Start the server:
        > make local
    2. Run curl command:
        > curl -X POST 'localhost:5000/handler'  -H 'Content-Type: application/json' -d '{"digits_string": "849"}'

###Run in Docker:
####Prerequisites: 
- Docker (https://docs.docker.com/v17.09/engine/installation/)

        1. Start container:
            > docker-compose up
        2. Run curl command:
            > curl -X POST 'localhost:5000/handler'  -H 'Content-Type: application/json' -d '{"digits_string": "849"}'
        
        
### Deployment
#### Prerequisites

 - Python3 environment
 - Google Cloud SDK (https://cloud.google.com/sdk/install)

1. Clone this project on your computer and go to the created directory:

        > git clone https://github.com/gabriel-montagne/roman-numbers-convertor.git
        
        > cd roman-numbers-convertor
        
2. Create a new python3 virtual environment for this project
3. Install dependencies:
        
        > pip install -r requirements.txt
        
4. Login to gcloud:

        > gcloud auth login
        
5. A browser window will appear. Select your user and login into your account.
6. A confirmation page will appear asking you to allow Google Cloud SDK to access your account.
Click Allow button.
7. In the up-right corner of the page you will find Console button. Click it to navigate to the console.
8. Open the projects window by clicking the dropdown arrow situated at the right side of title (Google Cloud Platform)
9. Create a new project and select it.
10. Click the upper left menu and the navigation window will appear on the right side of the page. Search for Cloud function and click on it.
11. Go back to your terminal in the project directory and run:

        > export PROJECT_NAME=name-of-your-project
        
12. Deploy the function to your project:
        
        > make deploy
        