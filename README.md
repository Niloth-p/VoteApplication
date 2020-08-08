### Setup Instructions: Running the Project Locally

Install the requirements:  
`pip install -r requirements.txt`  
Setup the local configurations:  
`cp .env.example .env`  
Create the database:  
`python manage.py migrate` 
Finally, run the development server:  
`python manage.py runserver`  
The project will be available at 127.0.0.1:8000/voteapp/

### Usage:

* Go to 127.0.0.1:8000/voteapp/  
* Click on any of the candidates' names to view their profile page  
* Go back to the voting page
* Choose a candidate from the radio buttons, and click submit  
* This will take you to the results page
* To clear your IP and re-vote, run the command:
`python manage.py shell < ClearIP.py`

### Features:

* Voting - once per IP 
* Viewing candidates' profiles
* Viewing results
* Admin actions
    - Add a new candidate
    - Delete an existing candidate
* Candidate actions
    - Edit details

#### Detailed features

* A clear_IP script for back-end testers to delete their IP from the database quickly to test re-voting.
* Back button of browser will redirect the voting page to the results page, after voting.
* Trying to get the details of a non-existent candidate returns 404.
* All the voters' IPs are stored in the database.
* The admins are given an authorization code, which needs to be present in the POST request, else access will be denied.
* The candidates are given a different authorization code to only edit the details.

### Settings variables

* Admin authorization code
* Candidate Authorization code
