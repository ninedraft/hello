from setuptools import setup
import sys

if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

setup(name='hello',
      version='0.0.1',
      description='Lovely welcome script',
      url='https://github.com/ninedraft/hello',
      author='ninedraft',
      author_email='',
      license='MIT',
      packages=['hello'],
      package_dir={"hello": "hello"},
      package_data={
          "hello": [
              "data/*.txt"
          ]
      },
      install_requires=[
          'requests',
          'appdirs'
      ],
      zip_safe=True)
