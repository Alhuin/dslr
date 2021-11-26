from setuptools import setup

setup(
    name="dslr",
    version="1.0.0",
    description="42 AI : Logistic Regression Project",
    author="jjanin-r",
    author_email="jjanin-r@student.42lyon.fr",
    packages=["dslr"],
    extras_require={"dev": ["pytest", "flake8", "pytest-cov", "pandas", "pre-commit"]},
    install_requires=["wheel", "matplotlib", "numpy"],
)
