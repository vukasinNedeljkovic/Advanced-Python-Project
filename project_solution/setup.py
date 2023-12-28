import setuptools
 
 
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
 
setuptools.setup(
    name='user_management_lib',
    packages=setuptools.find_packages(),
    version='0.0.1',
    long_description=long_description,
    description='User management lib',
    author='Group 2',
    license="MIT",
    install_requires=[],
    test_suite='tests',
    python_requires=">=3.6",
    ext_modules=[
        setuptools.Extension(
            name='hash',
            sources=['user_management_lib/hash.c']
        )
    ]
)