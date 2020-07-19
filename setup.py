""" ./setup.py """
import setuptools

setuptools.setup(
    name='IHeartMachines',
    version='0.0.1',
    author='Jonathan Craig',
    author_email='blurr@iamtheblurr.com',
    classifiers=[
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Scientific/Engineering :: Mathematics'
    ],
    packages=setuptools.find_packages(),
    url='https://github.com/iamtheblurr/iheartmachines',
    license='None',
    install_requires=[],
    long_description=open('README.md', encoding='utf8').read(),
)
