from setuptools import setup, find_packages

package_name = 'rqt_publisher'

setup(
    name=package_name,
    version='1.5.0',
    # packages=[package_name],
    packages=find_packages('src'),  # 自动发现src目录下的包，包括rqt_publisher和signal_publisher
    package_dir={'': 'src'},
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name + '/resource',
            ['resource/Publisher.ui']),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, ['plugin.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Dorian Scholz',
    maintainer='Dirk Thomas, Dorian Scholz',
    maintainer_email='dthomas@osrfoundation.org',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description=(
        'A Python GUI plugin publishing ROS messages.'
    ),
    license='BSD',
    entry_points={
        'console_scripts': [
            'rqt_publisher = ' + package_name + '.main:main',
        ],
    },
)
