import setuptools
from os import path

# Get the long description from README.md
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="TagGenerator",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A reusable Django app for QR Code generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DadaNanjesha/TagGenerator",
    packages=["QrCode"],  # Explicitly list your reusable app package
    include_package_data=True,  # Include files specified in MANIFEST.in
    install_requires=[
        "Django>=4.0",   
        "qrcode",
        "Pillow",  # If using an external QR code generation library
    ],
    classifiers=[
        "Framework :: Django",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
