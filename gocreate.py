#!/usr/bin/env python

import os
import sys
import glob
import optparse
import string

USAGE = "%prog [options] (command | package) name"
VERSION = "%prog 0.1"

def create(type, name, options):
	subs = {
		"name": name,
		"capname": name.capitalize(),
		"gitignore": ".gitignore"
	}
	
	if options.capname is not None:
		subs["capname"] = options.capname
	
	files = glob.glob(os.path.join(sys.path[0], type, "*"))
	if options.git == True:
		files.append(os.path.join(sys.path[0], "${gitignore}"))
		
	for filename in files:
		t = string.Template(os.path.basename(filename))
		targetname = t.substitute(subs)
		
		print "%s -> ./%s:" % (filename, targetname),

		if os.path.exists(targetname) and options.force == False:
			print "ERROR: file exists (use --force to override)"
			continue

		with open(filename, "r") as file:
			data = file.read()

		t = string.Template(data)
		data = t.substitute(subs)

		with open(targetname, "w") as file:
			file.write(data)

		print "OK"

def main():
	p = optparse.OptionParser(usage=USAGE, version=VERSION)
	p.add_option('', '--git', action="store_true", dest="git", default=False,
					help="add .gitignore")
	p.add_option('', '--force', action="store_true", dest="force", default=False,
					help="force command")
	p.add_option('', '--capname', action="store", dest="capname", default=None,
					help="override capitalized name")
	(options, args) = p.parse_args()

	if len(args) != 2:
		p.error("wrong number of arguments")

	if args[0] != "command" and args[0] != "package":
		p.error("unknown TYPE: %s" % args[0])

	create(args[0], args[1], options)
	
if __name__ == '__main__':
	main()
