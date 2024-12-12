from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy as np


extensions = [
    Extension(
        "dual_autodiff_x.dual", 
        ["dual_autodiff_x/dual.pyx"], 
    ),
]


setup(
    name="dual_autodiff_x",
    version="0.1.0",
    author="Lily Rausser",
    author_email="lsr34@cam.ac.uk",
    description="Cythonized implementation of automatic differentiation using dual numbers",
    ext_modules=cythonize(extensions, language_level="3"),
    # packages=find_packages(where='src'),
    packages=["dual_autodiff_x"],
    # package_dir={"": "src"},
    # packages=["dual_autodiff_x"],
    # Include only .so/.pyd files (compiled extensions), exclude source files
    install_requires=[
        "numpy",
    ],
    setup_requires=[
        "Cython",
    ],
    package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
    exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
    # Ensure that wheels can be built
    zip_safe=False,
)
