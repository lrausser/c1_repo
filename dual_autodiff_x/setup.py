# from setuptools import setup, Extension, find_packages
# from Cython.Build import cythonize
# import numpy as np


# extensions = [
#     Extension(
#         "dual_autodiff_x.dual", 
#         ["src/dual_autodiff_x/dual.pyx"], 
#         include_dirs=[np.get_include()] 
#     ),
# ]


# setup(
#     name="dual_autodiff_x",
#     version="0.1.0",
#     author="Lily Rausser",
#     author_email="lsr34@cam.ac.uk",
#     description="Cythonized implementation of automatic differentiation using dual numbers",
#     ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
#     packages=find_packages('src'),
#     package_dir={"": "src"},
#     # packages=["dual_autodiff_x"],
#     # Include only .so/.pyd files (compiled extensions), exclude source files
#     package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
#     exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
#     # Ensure that wheels can be built
#     zip_safe=False,
# )


from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy as np

# Define the extensions (Cython modules)
extensions = [
   Extension("dual_autodiff_x.dual", 
             ["src/dual_autodiff_x/dual.pyx"],
             include_dirs=[np.get_include()]  # Add NumPy headers
   ),
]

# Call setup with cythonized extensions
setup(
   ext_modules=cythonize(extensions,
   compiler_directives={'language_level': "3"}),
   package_dir={"": "src"},
   packages=["dual_autodiff_x"],

   # Include only .so/.pyd files (compiled extensions), exclude source files
   package_data={"dual_autodiff_x": ["*.so", "*.pyd"]},
   exclude_package_data={"dual_autodiff_x": ["*.pyx", "*.py"]},
   # Ensure that wheels can be built
   zip_safe=False,
)