import argparse
import sys

def banner():
	banner = r'''
	   Vigenere bruteforce tool by [ch4rm]
	'''
	print(banner)

def decrypt(ciphertext, key):
    key_length = len(key)
    key_as_int = [ord(i) for i in key]
    ciphertext_int = [ord(i) for i in ciphertext]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % 26
        plaintext += chr(value + 65)
    return plaintext

if __name__ == "__main__":
	banner()
	parser = argparse.ArgumentParser()

	parser.add_argument("-w", "--wordlist", dest = "wordlist",help="Wordlist")
	parser.add_argument("-n", dest = "unciphered", help="Known word")
	parser.add_argument("-c", dest = "ciphered", help="ciphered word")
	parser.add_argument("-v", dest = "verbose", help="Verbose", action='store_true')

	args = parser.parse_args()
	
	args = parser.parse_args(args=None if sys.argv[3:] else ['--help'])
	with open(args.wordlist, 'r', encoding="utf-8") as f:
		if not args.verbose:
			for line in f:
				if args.unciphered in decrypt(args.ciphered, line):
					print("Key found =  {}".format(line))
					break;
		else:
			for line in f:
				print("{}".format(line))
				if args.unciphered in decrypt(args.ciphered, line):
					print("Key found =  {}".format(line))
					break;
