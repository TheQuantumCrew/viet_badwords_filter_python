from setuptools import setup, find_packages

setup(
    name='viet_badwords_filter',
    version='1.0.1',
    description='A library to filter Vietnamese bad words',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Dinh Truong Quang',
    author_email='quangdinhvh2@example.com',
    url='https://github.com/TheQuantumCrew/viet_badwords_filter_python',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
