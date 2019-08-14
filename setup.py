from setuptools import setup

if __name__ == "__main__":
    setup(
        name='iterextras',
        version='0.2.0',
        description='Extra utilities for Python iterables',
        url='http://github.com/scanner-research/iterextras',
        author='Will Crichton',
        author_email='wcrichto@cs.stanford.edu',
        license='Apache 2.0',
        packages=['iterextras'],
        install_requires=['tqdm'],
        setup_requires=['pytest-runner'],
        tests_require=['pytest'],
        zip_safe=False)
