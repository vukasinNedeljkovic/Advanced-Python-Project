# Project for NIT Advanced Python programming course


### Create and set up a virtual environment

In Advanced-Python-Project root run following commands:

```
python.exe -m venv myenv
.\myenv\Scripts\activate
python.exe -m pip install -U -r .\requirements.txt
```


### Build and install library

```
cd .\project_solution\
python.exe setup.py bdist_wheel
pip install .\dist\user_management_lib-0.0.1-cp312-cp312-win_amd64.whl
```


### Run tests for testing library code

```
python.exe .\tests\test.py
```


### Manually test library functionality

Run main script from the Advanced-Python-Project root.

```
python.exe main.py
```

This script will print a menu where the user can select the options they want:

```
Welcome to User management
1. Register   
2. Login      
3. Add contact
4. Remove contact
5. Print contact
6. Logout
7. Exit
Enter your choice:
```