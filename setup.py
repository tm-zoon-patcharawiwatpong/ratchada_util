from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='ratchada_util',
    version='0.1.0',
    author='tm-zoon',
    author_email='zoon_p@thinkingmachin.es',
    description='A Python lib/util for Ratchada Whisper model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/tm-zoon-patcharawiwatpong/ratchada_util',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10, <3.12',
    install_requires=install_requires,
    include_package_data=True,
)
