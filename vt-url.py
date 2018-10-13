import requests
import argparse
import os
import time

def checkkey(kee):
	try:
		if len(kee) == 64:
			return kee
		else:
			print "There is something wrong with your key. Not 64 Alpha Numeric characters."
			exit()
	except Exception, e:
			print e
			
#def checkhash(hsh):
#	try:
#		if len(hsh) == 32:
#			return hsh
#		elif len() == 40:
#			return hsh
#		elif len(hsh) == 64:
#			return hsh
#		else:
#			print "The Hash input does not appear valid."
#			exit()
#	except Exception, e:
#			print e
			
def fileexists(filepath):
	try:
		if os.path.isfile(filepath):
			return filepath
		else:
			print "There is no file at:" + filepath
			exit()
	except Exception, e:
			print e

def main():
	parser = argparse.ArgumentParser(description="Query URL(s) against Virus Total.")
	parser.add_argument('-i', '--input', type=fileexists, required=False, help='Input File Location EX: /Desktop/Somewhere/input.txt')
	parser.add_argument('-o', '--output', required=True, help='Output File Location EX: /Desktop/Somewhere/output.txt ')
	parser.add_argument('-U', '--URL', required=True, help='Single URL EX: www.google.com')
	parser.add_argument('-k', '--key', type=checkkey, required=True, help='VT API Key EX: ASDFADSFDSFASDFADSFDSFADSF')
	args = parser.parse_args()

	#Run for a single url + key
	
	if args.url and args.key:
		file = open(args.output,'w+')
		file.write('Below is the identified URL.\n\n')
		file.close()
		VT_Request(args.key, args.url, args.output)
    
	#Run for an input file + key
	#elif args.input and args.key:
	#	file = open(args.output,'w+')
	#	file.write('Below are the identified malicious files.\n\n')
	#	file.close()
	#	with open(args.input) as o:
	#		for line in o.readlines():
	#			VT_Request(args.key, line.rstrip(), args.output)
	#			if args.unlimited == 1:
	#				time.sleep(1)
	#			else:
	#				time.sleep(26)
	
def VT_Request(key, url, output):
	params = {'apikey': key, 'url': url}
	url = requests.get('https://www.virustotal.com/vtapi/v2/url/scan', params=params)
	json_response = url.json()
	print json_response
	response = int(json_response.get('response_code'))
	if response == 0:
		print url + ' is not in Virus Total'
		file = open(output,'a')
		file.write(url + ' is not in Virus Total')
		file.write('\n')
		file.close()
	elif response == 1:
		positives = int(json_response.get('positives'))
		if positives == 0:
			print url + ' is not malicious'
			file = open(output,'a')
			file.write(url + ' is not malicious')
			file.write('\n')
			file.close()
		else:
			print url + ' is malicious'
			file = open(output,'a')
			file.write(url + ' is malicious. Hit Count:' + str(positives))
			file.write('\n')
			file.close()
	else:
		print url + ' could not be searched. Please try again later.'
# execute the program
if __name__ == '__main__':
if __name__ 
	main()
