#### Instructions
* Prepare environment file (findstr to remove prefix)  
```conda env export | findstr -v "^prefix: " > environment.yml```
* Initialize DB (os env parameters below)  
  - Change APP_DIR in .\\\_\_init_\_.py to 'Path().absolute()'  
  - Run below command from root directory, (OS env parameters below)  
```python initialize.py```
    - DATA_FOLDER=D:\MyDocuments\fitness-files;
    - DB_CONNECTION_STRING=sqlite:///D:\MyDocuments\fitness-files\fitness_files.db;
    - BALL_MACHINE_USAGE_FILE=ball_machine_usage.csv
  - Change APP_DIR in .\\\_\_init_\_.py to 'Path().absolute().parent'  
* Run application  
```uvicorm main:app```