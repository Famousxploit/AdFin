# AdFin
[![Python 2.6|2.7](https://img.shields.io/badge/python-2.6|2.7-yellow.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://raw.githubusercontent.com/p4kl0nc4t/AdFin/master/LICENSE)

AdFin is a tool used to look for website's (admin) login page by using a wordlist. AdFin is running under Python 2.7 and Python 2.6.
## Usage
```
usage: AdFin [-h] [--verbose] [--code CODE] [--filter FILTER]
             [--timeout TIMEOUT] [--noexit]
             wordlist url

AdFin is a tool used to check (admin) login page on a website based on given
wordlist file.

positional arguments:
  wordlist           path of file contining wordlist. Expected wordlist format
                     is one path per line (example:
                     'admin[newline]adminpage[newline]...)
  url                the url for login page check. Please not that you must
                     include the 'http://' or 'https://' and not including any
                     slashes at the end. (example: 'http://vb800.com')

optional arguments:
  -h, --help         show this help message and exit
  --verbose          this will increase the output verbosity by including
                     false (not found) results
  --code CODE        the expected HTTP response code (default: 200)
  --filter FILTER    the server usually return 200 OK response instead of 404
                     Not Found response, this option will also filter the page
                     content based on the given keyword (example: 'Username')
  --timeout TIMEOUT  sets the request timeout (default: no timeout)
  --noexit           do not exit AdFin when admin login page founded. This is
                     useful to find multiple admin page
```
## Dependency
AdFin requires Python 2.x to be able to run. AdFin also requires "requests" library, you can get it by issuing ```pip install requests``` or ```apt-get install python-requests``` for debian systems.
