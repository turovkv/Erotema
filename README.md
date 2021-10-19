# python-backend-course-2021

## Quiz online

### Run app

Install all from the requirements.txt  
Run main.py  


There are some example HTTP requests in the test.http   
To use graphQL interface go to "http://localhost:8000/gameGraphQL"

To run unit tests use `pytest test/unit`  
To run integrate tests use `pytest test/integrate`  

### Micro service architecture
[Picture !](https://docs.google.com/drawings/d/1lLF9a6OtFHs5odExkDpHQsIgcV9VS5fVMAp4ajwDGx8/edit?usp=sharing)


### DataBase
Before starting the app (or tests)  
Run `sudo docker-compose up` in `db/`  
To shut down db use `sudo docker-compose down`  
[DB-s comparison](https://docs.google.com/document/d/1mR2bJBGvuYa_xJmuVlW2MEsyAbVhNyqChmuHr4vP02g/edit?usp=sharing)