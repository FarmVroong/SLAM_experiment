# ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    scripts=['src/gps_test.py'],
    # scripts=['src/gps_listener.py'],
    # scripts=['src/initialize.py'],
    packages=['gps_test'],
    package_dir={'': 'src'},
)


setup(**setup_args)

# setup(
#     # version='0.0.0',

#     scripts=['src/gps_test.py'],

#     packages=['gps_test'],

#     package_dir={'':'src'}
# )