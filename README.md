# Table Calendar

Build calendar files (with ics format) based on manually produced tables.
This repository is mainly for educational purpose.

# Pre-requesites

Linux with python3.8 installed.

# Install your depencencies using a virtual environment

```bash
python3.8 -m venv .env --without-pip
source .env/bin/activate
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
rm get-pip.py
pip install -r requirements-dev.txt
pre-commit install
```

To activate your virtual env
```
source .env/bin/activate
```


To deactivate your virtual env
```
deactivate
```
