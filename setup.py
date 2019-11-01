from distutils.core import setup
setup(
  name = 'cazoo-cloudwatch-events',
  packages = ['cazoo-cloudwatch-events'],
  version = '0.1',
  license='MIT',
  description = 'Library for Cloudwatch Events common functions',
  author = 'Raul Herranz',
  author_email = 'raul.herranz@cazoo.co.uk',
  url = 'https://gitlab.com/raulherranz/cazoo-cloudwatch-events/',
#   download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
  keywords = ['Cazoo', 'Cloudwatch', 'events', 'put_events'],
  install_requires=[
          'boto3',
          'typing',
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
