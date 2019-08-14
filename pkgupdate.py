"""Update all the pypi packages listed in your requirements.txt"""

req = open('requirements.txt')
packages = []
for line in req.readlines():
    pkg = line.split("==")
    packages.append(pkg[0])
    
from subprocess import call
call("pip install --upgrade " + ' '.join(packages), shell = True)
