# Cazoo Cloudwatch

This repository is meant to be part of to be a helper among all the functions that we use internally at Cazoo.
Right now, it's just a simple CW put_events function. 

# Prereqs

I personally use twine to upload the packages to pypi

`pip install twine`

# Build and upload versions
python setup.py sdist
twine upload dist/* --username <username>
