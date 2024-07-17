from setuptools import setup, find_packages

setup(
    name='ratchada_util',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A description of your package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ratchadapipeline',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10, <3.12',
    install_requires=[
        regex==2023.10.3 ; python_version >= "3.10" and python_version < "3.12"
    ],
    include_package_data=True,
)
