from setuptools import setup, find_packages


requirements = "./requirements.txt"
def dependencies():
    req_list=[]
    with open(requirements,"r") as f:
        dep_line = f.readlines()
        for i in dep_line:
            if i == "-e .":
                pass
            else:
                req_list.append(i.replace("\n",""))
        return req_list




setup(
    name="Gem Price Prediction",
    version="0.0.1",
    description="End-to-End Machine Learning Project",
    author="Aaron",
    author_email="aaronnb17@gmail.com",
    packages=find_packages(),
    install_requires=dependencies(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

