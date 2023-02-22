import setuptools

version = None

version = ""
file_version = convert_path("tacky/version.py")
with open(file_version) as f:
    main_ns = {}
    exec(f.read(), main_ns)
    version = main_ns['__version__']

setuptools.setup(
    name             = "tacky",
    version          = version,
    author           = "Sasha F",
    author_email     = "carley.f253fa96@icantbelieveitsnotgmail.com",
    description      = """copy and paste specific UTI's from the macOS Pasteboard""",
    url              = "https://github.com/friedenberg/tacky",
    package_data={'': ['VERSION']},
    include_package_data=True,
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
