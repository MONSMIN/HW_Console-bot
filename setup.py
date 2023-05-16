from setuptools import setup, find_namespace_packages

setup(
    name='console-bot',
    version='1',
    description='console-bot',
    url='',
    author='Dmytro Teplinskiy',
    author_email='d.v.teplinskiy@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['console-bot = console_bot.main:main']}
)