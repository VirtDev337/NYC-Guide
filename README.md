
# <div align="center">New York City Guide</div>
## <div align="center">JTC App Project 2</div>
***
New York City Guide is a travel website built within Django, a Python web framework, that displays static content from the five NYC burroughs and various tourist activities and venues people can see and/or do if they visit the Big Apple.
***

### Table of Contents
- Developers
- Installation/Technology Requirements
    - Python ver. 3.9.7 or later
    - Django
- Usage
    - Create and Run Virtual Environment
    - Install Django and Create 'requirements.txt' file
    - Run the New York City Guide website in the virtual environment
- Bonus Features
    - Implementation of cards to link activty and venue
- License
- Links
***
### Developers
- Lee Harvey
 Git Hub: https://github.com/VirtDev337
- Rakesh Perani 
  Git Hub: https://github.com/RakeshPerani

***
## Installation/Technology Requirements
New York City Guide requires [Python](https://www.python.org/) v3.9+  and [Django](https://www.djangoproject.com/) to run.
***

### Usage
- To run New York City Guide, you will have to create a directory where you will run a virtual environment. The files for running the virtual environment will be saved in this directory:
```
mkdir <name-of-your-directory>
cd <name-of-your-directory>
```

Inside `<name-of-your-directory>` run the following:
```
python -m venv <name-of-your-virtual-environment>
```

Now, run the virtual environment:

##### On Windows:
Windows Powershell users:

```
<name-of-your-directory>/Scripts/activate.bat  or  <name-of-your-directory>/Scripts/activate.ps1
```
##### On Bash, Unix, Linux or MacOS:
```
source <name-of-your-directory>/Scripts/activate
```

- Install Django:
```
pip install django
```

- Start your virtual environment and run the New York City Guide from the directory with manage.py in it:
```
python manage.py runserver (and follow/click on the link: http://127.0.0.1:8000/)
```
***
### Bonus Features
#### Bootstrap Cards:
The Bootstrap toolkit, a free and open-source CSS framework, was utilized for front-end development of cards to display a picture of each activity and venue.

***
### Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. 
All changes will be considered but may not be integrated.

Please make sure to update tests as appropriate.
***
### License
[MIT](https://choosealicense.com/licenses/mit/)
***
Copyright (c) 10/13/2021 Rakesh Perani & Lee Harvey



