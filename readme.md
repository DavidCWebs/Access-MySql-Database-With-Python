Access MySql Database With Python
=================================
Use Python to build CSV files from a WordPress database.

Quick & dirty script.

Usage
-----
1. Clone this repo
2. `cd` into the project directory
3. Make a virtual environment: `virtualenv -p python3 venv`
4. `source` the virtual environment activation script - e.g. `source venv/bin/activate`
5. Run `pip install -r requirements.txt`
6. Add a `config.py` file in project root with database connection credentials in a `mysql` list
7. `cp sample-config.py config.py` and amend values

References
----------
* [Basic tutorial for pymysql][1]

[1]: https://hackersandslackers.com/using-pymysql/
