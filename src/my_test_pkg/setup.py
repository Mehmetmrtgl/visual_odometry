from setuptools import find_packages, setup

package_name = 'my_test_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
   data_files=[
    ('share/ament_index/resource_index/packages',
     ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ('share/' + package_name + '/launch', ['launch/test_node.launch.py']),
    ('share/' + package_name + '/launch', ['launch/zed2i_launch.py']),
    ('share/' + package_name + '/launch', ['launch/zed_xsens_launch.py']),
        ('share/' + package_name + '/launch', ['launch/start.launch.py']),
    ('share/' + package_name + '/launch', ['launch/zed_xsens_combined.launch.py']),
],

    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='neurolab',
    maintainer_email='mehmetmrt199@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'hr_pub = my_test_pkg.hr_pub:main',],
    },
)
