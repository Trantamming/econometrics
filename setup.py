from setuptools import setup, find_packages

setup(
    name='econometrics',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'statsmodels',
        'matplotlib'
    ],
    description='Package for econometric linear regression models and plotting.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Trần Minh Tâm',
    author_email='email@example.com',
    url='https://github.com/yourusername/econometrics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
