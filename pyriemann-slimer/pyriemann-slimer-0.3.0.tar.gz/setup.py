from setuptools import setup, find_packages

setup(name='pyriemann-slimer',
      version='0.3.0',
      description='Riemannian Geometry for python',
      url='',
      author='Alexandre Barachant',
      author_email='alexandre.barachant@gmail.com',
      license='BSD (3-clause)',
      packages=find_packages(),
      install_requires=['numpy', 'scipy', 'scikit-learn',  'joblib'],
      zip_safe=False)
