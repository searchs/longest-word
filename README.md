# WordApp - Get Longest and Shortest words with length

This application returns the longest word(s) in a sentence along with the length of such a word(s).
It can also return the shortest word(s) with the length.

Since the several words can have the same length and can be the longest, the application returns a
list of words along with the length.

The application was built using the following technologies:
1. Python
2. FastAPI 
3. Docker
4. PyTest/PyCov
   
The list of libraries and dependencies can be found in the requirements.txt in the src directory.

To build and run the application, simply clone the repository, change into the project directory and run the command:
```docker-compose up -d --build```

If Docker is not your thing, then follow these steps: 
1.  Clone the repository
2.  Change into source directory
3.  Run the command to install dependencies: ```pip install -r src/requirements.txt```
4.  Inside the app directory, run the command:```uvicorn app.wordapp:app --reload```
5.  Go to http://localhost:docs to test the app.


To run the tests, follow these steps:
1.  If using via docker: ```docker-compose exec web pytest --cov-report term-missing -v . --cov ```
2.  If you are running the app without Docker and with code coverage: `pytest --cov-report term-missing -v . --cov`
3.  To test via a user interface(UI), go to the Swagger docs: `http://localhost:8000/docs`

There is the assumption that the application does not require manual user input at the moment, hence the sample API
included in the code.
I also assumed that numbers/digits are not counted as words.
Another assumption is that there is no need to store the results hence no persistence layer in the application. 