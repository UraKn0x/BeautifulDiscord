from setuptools import setup, find_packages


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open('README.md') as f:
    readme = f.read()


setup(
    name='BeautifulDiscord',
    author='leovoel, Ura Yukimitsu',
    url='https://github.com/UraYukimitsu/BeautifulDiscord',
    version='0.1.0',
    license='MIT',
    description='Adds custom CSS and JS support to Discord.',
    long_description=readme,
    packages=find_packages(),
    install_requires=requirements,
    include_package_data=True,
    entry_points={'console_scripts': ['beautifuldiscord=beautifuldiscord.app:main']}
)
