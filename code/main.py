import argparse
import os

parser = argparse.ArgumentParser("simple_example")
parser.add_argument("--random-string", dest='rndstr', help="random string", type=str)
args = parser.parse_args()
if(args.rndstr is not None):
    with open('%s.txt'%(args.rndstr), 'w') as f:
        f.write(args.rndstr)
    os.system('aws s3 cp %s.txt s3://random-string-destination/%s.txt'%(args.rndstr,args.rndstr))
    os.remove('%s.txt'%(args.rndstr))