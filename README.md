# Table Calendar

Build calendar files (with ics format) based on manually produced tables.
This repository is mainly for educational purpose (TDD training, and show nice stuff about python).
The TDD school represented in this repository is supposed to be in line with the mixed approach Harry J.W Percival portrayed in his book https://www.obeythetestinggoat.com/. 

- outside-in (or double loop TDD)
- nevertheless more inline with classical TDD approach (state verification is preferred, tests doubles are avoided if possible). 
More on the difference between classical and mockist TDD schools here https://martinfowler.com/articles/mocksArentStubs.html

The value of this repository is mainly in the commit history :
https://github.com/brumar/tablecalendar/commits/master

Don't hesitate to use the "Browse" Button to inspect repository state instead of just commit content.

Commit messages are intentionally giving hints on the current step in the TDD methodology. 

Commit content are very short (each step is represented).

I do not advise to do that in real life, committing only at green states should be preferred.
The red outer loop should rather not be played by your CI system, so use `@pytest.mark.skipif` (http://doc.pytest.org/en/latest/skipping.html) to skip this test, then drop this line when the feature test passes.

# Pre-requisites

Linux with python3.8 installed.

# Install your dependencies using a virtual environment

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

Pyannotate can be used. It's invoked in `conftest.py` and writes the file `annotations.json`

Examples to add type automatically :
```
pyannotate --type-info ./annotations.json --py3 tests/test_conversion.py -w
pyannotate --type-info ./annotations.json --py3 icsmaker.py -w
```
