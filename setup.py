import setuptools

version = None

with open('VERSION', 'r') as f:
    version = f.read()

setuptools.setup(
    name             = "tacky",
    version          = version,
    author           = "Sasha Friedenberg",
    author_email     = "carley.f253fa96@icantbelieveitsnotgmail.com",
    description      = """copy and paste specific UTI's from the macOS Pasteboard""",
    url              = "https://github.com/friedenberg/tacky",
    packages         = ['tacky'],
    package_dir      = {'tacky': 'src'},
    install_requires = [
        'pyobjc-core',
        'pyobjc-framework-Cocoa',
        ],
    classifiers      = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Environment :: MacOS X :: Cocoa",
    ],
    python_requires  = '>=3.6.8',
    entry_points     = {
        'console_scripts': ['tacky = tacky.__main__:main'],
    }
)
