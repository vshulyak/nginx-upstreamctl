from setuptools import setup, find_packages
 
setup(
    name='nginx-upstreamctl',
    version='0.1.0',
    description="""Nginx upstream config dynamic generation via python script.
        A common use case is to execute this script on every Serf cluster config change""",
    author='Vladimir Shulyak',
    author_email='vladimir@shulyak.net',
    url='http://shulyak.net/',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts = [
        'upstreamctl/nginx-upstreamctl'
    ],
    install_requires=['pynginxconfig>=0.3.3']
)