from setuptools import setup, find_packages
import sys, os

version = '0.2'

setup(name='opencore-fassembler_projects',
      version=version,
      description="Assorted fassembler projects for creating repeatable OpenCore builds",
      long_description=open("CHANGES.txt").read(),
      classifiers=[], 
      keywords='',
      author='Ethan Jucovy',
      author_email='opencore-dev@lists.coactivate.org',
      url='http://coactivate.org/projects/opencore',
      license='GPL',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        "fassembler"
      ],
      dependency_links=[
        "https://svn.openplans.org/svn/fassembler/trunk#egg=fassembler-dev",
        ],
      entry_points="""
      [fassembler.project]
      frontend = fassembler_projects.frontend:FrontendProject
      zine = fassembler_projects.zine:ZineProject
      """,
      )
