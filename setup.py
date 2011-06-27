# encoding: utf-8

try:
    import setuptools
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
from setuptools import setup, find_packages

version = '0.1.0'
readme = open('README.rst').read()

setup(name='should_web',
      version=version,
      description='Should-DSL matchers for web application tests using Splinter.',
      long_description=readme,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Software Development :: Documentation',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Testing',
      ],
      keywords='should dsl assertion bdd python expectation web applications splinter',
      author='Rodrigo Manhães',
      author_email='rmanhaes@gmail.com',
      url='https://github.com/rodrigomanhaes/should-web',
      license='MIT License',
      packages=find_packages(),
      test_suite='run_all_examples.test_suite',
      install_requires=['should-dsl', 'splinter'],
      tests_require=['flask']
      )

