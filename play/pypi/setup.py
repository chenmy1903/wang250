from setuptools import setup
import setuptools

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_readme():
    with open(os.path.join(BASE_DIR, "README.md"), "r", encoding="utf-8") as f:
        return f.read()

setup(
    name="wang250_mods",
    version="1.4",
    python_requires='>=3.7.0', # python环境
    auther="chenmy1903",
    auther_email="duck_chenmy1903@163.com",
    description="Make a mod in wang250.",
    long_description=get_readme(), # 读取的Readme文档内容
    long_description_content_type="text/markdown",  # 指定包文档格式为markdown
    packages=setuptools.find_packages(),
    install_requires=[
        "pygame",
        "requests",
        "pickleshare",
    ],
    include_package_data=True,
    keywords=['mods', 'wang250', '逃离王建国'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
