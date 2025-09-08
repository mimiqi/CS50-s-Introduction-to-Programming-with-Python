import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-n",type = int,required = True, help = "Number of times to print 'Hello, World!'")
parser.add_argument("-v", "--verbose", action = "store_true", help = "Verbose mode")
args = parser.parse_args()
if(args.verbose == True):
    print("Verbose mode is enabled")

for _ in range(args.n):
    print("Hello, World!")