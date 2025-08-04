from setuptools import find_packages, setup

package_name = 'imu_covariance_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='neurolab',
    maintainer_email='mehmetmrt199@gmail.com',
    description='ROS2 node that adds covariance matrices to raw IMU messages.',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'imu_covariance_node = imu_covariance_pkg.imu_covariance_node:main',
            'imu_combiner_node = imu_covariance_pkg.imu_combiner_node:main',
        ],
    },
)

