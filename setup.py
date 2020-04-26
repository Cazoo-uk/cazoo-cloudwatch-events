from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'cazoo_cloudwatch_events',
  packages = ['cazoo_cloudwatch_events'],
  version = '0.1.10',
  license='MIT',
  description = 'Cazoo common library for Cloudwatch Events',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'Raul Herranz',
  author_email = 'raul.herranz@cazoo.co.uk',
  url = 'https://gitlab.com/raulherranz/cazoo-cloudwatch-events/',
  keywords = ['Cazoo', 'Cloudwatch', 'events', 'put_events'],
  install_requires=[
          'boto3',
          'cazoo-logger'
      ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
  ],
)
