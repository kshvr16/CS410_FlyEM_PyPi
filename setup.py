from setuptools import setup, find_packages


setup(
    name='CS410_FlyEM_Segmentation_Pipeline',
    version='1.0',
    license='MIT',
    author="Sai Harshavardhan Reddy Kona",
    author_email='s.kona001@umb.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/kshvr16/CS410_FlyEM_PyPi',
    keywords='Testing PyPi deployment',
    install_requires=[
        'numpy',
        'mahotas',
        'matplotlib',
        'scikit-image'
      ],

)
