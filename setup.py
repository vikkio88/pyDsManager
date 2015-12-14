from distutils.core import setup

setup(
        name='pyDsManager',
        version='0.0.1beta',
        packages=['lib.models', 'lib.generator'],
        url='https://github.com/vikkio88/pyDsManager',
        license='MIT',
        author='vikkio88',
        author_email='vincenzo.ciaccio@gmail.com',
        description='',
        install_requires=[
                "faker==0.5"
        ],
        dependency_links=[
            "git+ssh://git@github.com/joke2k/faker.git@0.5#egg=faker-0.5"
        ]
)
