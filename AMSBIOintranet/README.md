﻿## Running Local Server

1.	Go to the path where project is saved, there should be a file named “manage.py”. The path in this case is: “G:\Vaibhav\new_intranet\AMS-Intranet\AMSBIOintranet”.
2.	Here, open command prompt by typing “cmd” in the address bar.
3.	In the command prompt, enter: “C:\ProgramData\Anaconda3\Scripts\activate test_env” to activate the python environment.
4.	Once activated enter the command, “python manage.py runserver” to run the tests.
5.	The local server will start and could be visited at https://127.0.0.1:8000.
6.  On closing the command prompt the server will stop.


## Testing Procedures

1.	Go to the path where project is saved, there should be a folder named “functional_tests”. The path in this case is: “G:\Vaibhav\new_intranet\AMS-Intranet\AMSBIOintranet”.
2.	Here, open command prompt by typing “cmd” in the address bar.
3.	In the command prompt, enter: “C:\ProgramData\Anaconda3\Scripts\activate intranetenv” to activate the python environment.
4.	Once activated enter the command, “python manage.py test -n functional_tests” to run the tests.
5.	The testing should take about 30-35 seconds to finish.