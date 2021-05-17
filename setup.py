from setuptools import setup

install_requires = [
    'requests'
]

setup(name='csgo_market_api',
      version='0.1.2',
      description='A simple python module for interacting with various parts of market.csgo.com',
      packages=['csgo_market_api'],
      author_email='letsfunbox@gmail.com',
      install_requires=install_requires,
      zip_safe=False)
