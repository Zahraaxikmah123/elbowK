from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='elbowK',
    version='1.0',
    description='Automatically find the optimal number of clusters (k) for KMeans using the Elbow Method and visualize the result.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Mohamed Adan, Sara Iidle, Nasteha Nor',
    author_email='zaaraxikmahiidle388@gmail.com',
    url='https://github.com/Zahraaxikmah123/elbowK',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'matplotlib',
        'pandas',
        'kneed'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)