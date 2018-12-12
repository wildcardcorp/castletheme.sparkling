from setuptools import setup, find_packages

version = '1.0.1'

setup(name='castletheme.sparkling',
      version=version,
      description="Implementation of the WordPress Sparkling theme for CastleCMS",
      long_description=open("README.md").read() + "\n" + open("CHANGELOG.md").read(),
      classifiers=[
        "Framework :: Plone",
        "Framework :: Plone :: 5.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        ],
      keywords='castlecms plone theme',
      author='Wildcard Corp.',
      author_email='corporate@wildcardcorp.com',
      url='https://www.wildcardcorp.com',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['castletheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'plone.app.theming'
      ],
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
