from setuptools import setup, find_packages

with open('falafel/version.py') as f:
    for line in f:
        if line.startswith('__version__'):
            exec(line)

setup(
    author = 'Thomas Hisch',
    author_email = 't.hisch@gmail.com',
    description = ('Library suited for long-running unit/integration tests, '
                   'based on the unittest package'),
    name = "falafel",
    version = __version__,
    packages = find_packages(),
    platforms = 'Any',
    requires = ['python (>=2.7.0)',
                'pygments (>=1.6)',
                'tabulate (>=0.6)']
)
