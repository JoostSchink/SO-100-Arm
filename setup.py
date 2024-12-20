from setuptools import setup, find_packages

setup(
    name="SO-100-Arm",
    version="3.13",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here, e.g.,
        # 'numpy>=1.21.0',
    ],
    extras_require={
        "dynamixel": ["dynamixel_sdk"]  # Optional dependencies
    },
    author="JoostSchink",
    author_email="j.j.schinkelshoek@student.tudelft.nl",
    description="A sample Python project",
)
