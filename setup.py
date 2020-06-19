from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='the-coffee-bar',
    version='0.0.1',
    description='The Coffee Bar - python auto instrumented application',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Sanyaku/tracing-demo-java',
    author='Mateusz "mat" Rumian',
    author_email='mrumian@sumologic.com',
    classifiers=[  # Optional
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='the-coffee-bar opentelemetry auto instrumentation setuptools development',

    packages=find_packages(),
    python_requires='>=3.7, <4',

    install_requires=['argparse==1.4.0',
                      'opentelemetry-instrumentation==0.9b0',
                      'opentelemetry-api==0.9b0',
                      'opentelemetry-sdk==0.9b0',
                      'opentelemetry-ext-requests==0.9b0',
                      'opentelemetry-ext-psycopg2==0.9b0',
                      'opentelemetry-ext-flask==0.9b0',
                      'opentelemetry-ext-jaeger==0.9b0',
                      'psycopg2-binary==2.8.5',
                      'pyjson==1.3.0',
                      'pyyaml==5.3.1',
                      'requests==2.23.0',
                      ],
    data_files=[('config', ['src/config/config.yaml'])],
    entry_points={
        'console_scripts': [
            'the-coffee-bar=src.bin.the_coffee_bar:main',
            'the-coffee-machine=src.bin.the_coffee_machine:main',
            'the-cashdesk=src.bin.the_cashdesk:main',
            'the-coffee-lover=src.bin.the_coffee_lover:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/Sanyaku/tracing-demo-java/issues',
        'Source': 'https://github.com/Sanyaku/tracing-demo-java/',
    },
)
