	Instructions:

- Run create_new_repo once.
- On linux:
	crontab -e
	add the following to the last line:
	*/180 * * * * /usr/bin/env python3 /path/to/upload_files.py

-on windows:
	just automate execution of upload_files.py to once every 3 hours.	