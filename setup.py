import setuptools

version = None

with open('VERSION', 'r') as f:
    version = f.read()

setuptools.setup(
    name             = "gummy",
    version          = version,
    author           = "Sasha Friedenberg",
    author_email     = "carley.f253fa96@icantbelieveitsnotgmail.com",
    description      = """copy specific UTI's from the macOS Pasteboard""",
    url              = "https://github.com/friedenberg/gummy",
    packages         = ['gummy'],
    package_dir      = {'gummy': 'src'},
    install_requires = [
        'pyobjc-core',
        'pyobjc-framework-Cocoa',
        ],
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: MacOS X :: Cocoa",
    ],
    python_requires  = '>=3.7.6',
    entry_points     = {
        'console_scripts': ['gummy = gummy.__main__:main'],
    }
)
