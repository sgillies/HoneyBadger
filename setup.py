from setuptools import setup, find_packages
import sys, os

version = '1.0'

setup(name='honeybadger',
      version=version,
      description="Hungry, fearless, gross",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='hungry fearless gross',
      author='Sean Gillies',
      author_email='sean.gillies@gmail.com',
      url='',
      license='WTFPL 2.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
