"""Setup and Install Script."""


from setuptools import setup


def get_readme():
    """Load README.rst for display on PyPI."""
    with open('README.md') as fhandle:
        return fhandle.read()


setup(
    name="PTMKinase",
    version="0.0.1b1",
    description="PTMKinase Package",
    long_description=get_readme(),
    long_description_content_type='text/markdown',
    # license="GNU (Version 3)",
    # package_dir={"PTMKinase": "features"},
    package_dir={"PTMKinase": ["DL", "RF"]},
    packages=["PTMKinase"],
    install_requires=["numpy>=1.18.5", "scipy>=1.5.0", "pytest>=5.4.3", "sphinx>=2.3.0"],
)
