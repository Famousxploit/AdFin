#!/usr/bin/python

# - AdFin: Admin login page finder
# | Author: P4kL0nc4t
# | Date: 7/11/2017
# | Disclaimer: Editing the author will not make you the real coder :)

print """\
   ___     _______    
  / _ |___/ / __(_)__   Admin Page Finder
 / __ / _  / _// / _ \\  Author: P4kL0nc4t
/_/ |_\\_,_/_/ /_/_//_/  {ver: 1.0}
"""

import requests
import argparse
import datetime
import time

parser = argparse.ArgumentParser(prog="AdFin", description="AdFin is a tool used to check (admin) login page on a website based on given wordlist file.", epilog="If you had stuck, you can mail me at p4kl0nc4t@obsidiancyberteam.id")
parser.add_argument("wordlist", help="path of file contining wordlist. Expected wordlist format is one path per line (example: 'admin[newline]adminpage[newline]...)")
parser.add_argument("url", help="the url for login page check. Please not that you must include the 'http://' or 'https://' and not including any slashes at the end. (example: 'http://vb800.com')")
parser.add_argument("--verbose", dest="verbose", help="this will increase the output verbosity by including false (not found) results", action="store_true")
parser.add_argument("--code", dest="code", help="the expected HTTP response code (default: 200)", type=int)
parser.add_argument("--filter", dest="filter", help="the server usually return 200 OK response instead of 404 Not Found response, this option will also filter the page content based on the given keyword (example: 'Username')")
parser.add_argument("--timeout", dest="timeout", help="sets the request timeout (default: no timeout)", type=int)
parser.add_argument("--noexit", dest="noexit", help="do not exit AdFin when admin login page founded. This is useful to find multiple admin page", action="store_true")
args = parser.parse_args()

def showstatus(message, type="new"):
	now = datetime.datetime.now().strftime("%H:%M:%S")
	icon = "*"
	if type == "warn":
		icon = "!"
	elif type == "new":
		icon == "*"
	message = "[" + icon + "][" + now + "]" + message
	return message

def wrapsbrace(string, endspace=False):
	if endspace == True:
		return "[" + string + "] "
	else:
		return "[" + string + "]"

def sleep(x):
	try:
		time.sleep(x)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .", "warn")
		exit()

wordlist = open(args.wordlist, 'r')
linecount = sum(1 for line in open(args.wordlist))
print showstatus(wrapsbrace("wordlist", True) + "Counted {} words in {}".format(linecount, args.wordlist))
if args.filter:
	print showstatus(wrapsbrace("filter", True) + "Filtering response content by: '{}'".format(args.filter))
if args.verbose:
	print showstatus(wrapsbrace("warning", True) + "Verbose mode enabled! Including all results!", "warn")
i = 1
for line in wordlist:
	line = line.rstrip()
	word = line
	url = args.url + "/" + word
	try:
		if not args.timeout:
			request = requests.get(url)
		else:
			if args.timeout > 0:
				request = requests.get(url, timeout=args.timeout)
			else:
				request = requests.get(url)
	except KeyboardInterrupt:
		print "\r" + showstatus(wrapsbrace("except", True) + "KeyboardInterrupt thrown! Exiting . . .", "warn")
		exit()
	except requests.exceptions.ConnectionError as e:
		print showstatus(e, "warn")
		print showstatus(wrapsbrace("except", True) + "Exiting . . .")
		exit()
	else:
		expected = 200
		if args.code:
			expected = args.code
		if not args.filter:
			if request.status_code == expected:
				print showstatus(wrapsbrace(str(i)) + ("found") + wrapsbrace("Reason: '{} {}'".format(request.status_code, request.reason), True) + "URL: {}".format(url))
				if not args.noexit:
					exit()
			else:
				if args.verbose:
					print showstatus(wrapsbrace(str(i)) + wrapsbrace("error") + wrapsbrace("Reason: '{} {}'".format(request.status_code, request.reason), True) + "URL: {}".format(url), "warn")
		else:
			if request.status_code == expected and args.filter in request.text:
				print showstatus(wrapsbrace(str(i)) + wrapsbrace("found") + wrapsbrace("Reason: 'FilterMatch', '{} {}'".format(request.status_code, request.reason), True) + "URL: {}".format(url))
				if not args.noexit:
					exit()
			else:
				if args.verbose:
					print showstatus(wrapsbrace(str(i)) + wrapsbrace("error") + wrapsbrace("Reason: 'FilterNotMatch', '{} {}'".format(request.status_code, request.reason), True) + "URL: {}".format(url), "warn")
	i += 1
