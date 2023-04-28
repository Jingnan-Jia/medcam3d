import setuptools

with open('README.md', mode='r', encoding='utf-8') as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setuptools.setup(
    name='medcam3d',
    version='0.0.3',
    author='Jingnan Jia',
    author_email='jiajingnan2222@gmail.com',
    description='CAM for 3D medical image networks',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Jingnan-Jia/medcam3d',
    project_urls={
        'Bug Tracker': 'https://github.com/Jingnan-Jia/medcam3d/issues',
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(
        exclude=["*tutorials*"]),
    python_requires='>=3.6',
    install_requires=requirements)