from distutils.core import setup, Extension

setup(name='hash', version='1.0',
      ext_modules=[Extension('hash', ['hash.c'])])
