from setuptools import setup
setup(
    name = 'pomodoroCLI',
    version = '0.1.0',
    packages = ['pomodoroCLI'],
    entry_points = {
        'console_scripts': [
            'pomodoro = pomodoroCLI.__main__:main'
        ]
    },
    install_requires=["numpy", "pandas"]
    )