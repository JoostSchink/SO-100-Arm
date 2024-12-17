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
    author="Your Name",
    author_email="youremail@example.com",
    description="A sample Python project",
)
