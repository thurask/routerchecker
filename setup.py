#!/usr/bin/env python3
from setuptools import setup, find_packages
from routerchecker import __version__ as version


def readme():
    """
    Read ReST readme file, use as long description.
    """
    with open('README.rst') as file:
        return file.read()


if __name__ == "__main__":
    setup(name='routerchecker',
          version=version,
          description='Router firmware update scanner',
          long_description=readme(),
          url='https://github.com/thurask/routerchecker',
          keywords='router firmware',
          author='Thurask',
          author_email='thuraski@hotmail.com',
          license='WTFPL v2',
          classifiers=[
              "Development Status :: 5 - Production/Stable",
              "Environment :: Console",
              "Environment :: MacOS X",
              "Environment :: Win32 (MS Windows)",
              "Environment :: X11 Applications",
              "Intended Audience :: End Users/Desktop",
              "License :: Freely Distributable",
              "Operating System :: MacOS",
              "Operating System :: MacOS :: MacOS X",
              "Operating System :: Microsoft",
              "Operating System :: Microsoft :: Windows",
              "Operating System :: OS Independent",
              "Operating System :: POSIX",
              "Operating System :: POSIX :: BSD :: FreeBSD",
              "Operating System :: POSIX :: BSD :: NetBSD",
              "Operating System :: POSIX :: BSD :: OpenBSD",
              "Operating System :: POSIX :: Linux",
              "Operating System :: Unix",
              "Programming Language :: Python :: 3.2",
              "Programming Language :: Python :: 3.3",
              "Programming Language :: Python :: 3.4",
              "Programming Language :: Python :: 3.5",
              "Programming Language :: Python :: 3",
              "Programming Language :: Python :: 3 :: Only",
              "Topic :: Utilities"
          ],
          packages=find_packages(),
          zip_safe=False,
          include_package_data=True,
          install_requires=[
              'requests',
              'beautifulsoup4'
          ],
          entry_points={'console_scripts': ['routerchecker=routerchecker:parse_args']})
