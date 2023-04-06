import argparse
import asyncio
import pymongo
import socket
import os

RESET = '\033[0m'
BOLD = '\033[1m'
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
CYAN = '\033[96m'
WHITE = '\033[97m'

def write_to_file(filename, content):
    if not os.path.exists("output"):
        os.makedirs("output")
    with open(f"output/{filename}", "a") as f:
        f.write(content + "\n")

def write_success(url):
    write_to_file("success.txt", url)

def write_error(url):
    write_to_file("error.txt", url)

async def test_url(url, verbose):
	try:
		client = pymongo.MongoClient(url.strip(), serverSelectionTimeoutMS = 2000)
		db_list = client.list_database_names()
		if verbose:
			print(f"{BOLD}{WHITE}[{GREEN}+{WHITE}]{YELLOW}: {CYAN}{url.strip()}")
			write_success(url.strip())
		return url.strip(), True
	except pymongo.errors.ConfigurationError:
		if verbose:
			print(f"{BOLD}{WHITE}[{RED}+{WHITE}]{YELLOW}: {CYAN}{url.strip()}")
			write_error(url.strip())
		return url.strip(), False
	except socket.timeout:
		if verbose:
			print(f"{BOLD}{WHITE}[{RED}+{WHITE}]{YELLOW}: {CYAN}{url.strip()}")
			write_error(url.strip())
		return url.strip(), False
	except Exception as e:
		if verbose:
			print(f"{BOLD}{WHITE}[{RED}+{WHITE}]{YELLOW}: {CYAN}{url.strip()}")
			write_error(url.strip())
		return url.strip(), False

async def main(filename, verbose):
	with open(filename) as f:
		urls = f.readlines()
	tasks = [asyncio.create_task(test_url(url, verbose)) for url in urls]
	results = await asyncio.gather(*tasks)
	return results

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-l", "--list", help="display connection status for each URL in the list", action="store_true")
	parser.add_argument("filename", help="name of the file containing the list of URLs")
	args = parser.parse_args()

	if args.list:
		results = asyncio.run(main(args.filename, True))
	else:
		results = asyncio.run(main(args.filename, False))