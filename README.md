# For AWS ELASTIC BEANSTALK DEPLOYMENT
> The configuration is for AWS deployment through Github code pipeline

## END to END ML Project ##

This repository contains an end-to-end machine learning project, showcasing the steps involved in building, training, and deploying a machine learning model.

### Setup ###

1. **Create and Activate a Virtual Environment:**

   It's recommended to work within a virtual environment to manage project dependencies.

   Using conda:

   ```bash
   conda create -n venv python=3.8
   conda activate venv    OR    conda activate path_to_venv
   ```

2. Installing libraries via requirment.txt
    Installing the dependancies. 

    ```bash
    pip install -r requirmement.txt
    ```

3. Build Project package
    Executing setup.py
    ```bash
    python setup.py install
    ```
    Note - This need's to be run after the package folder and files are created. Because in the package source file i.e SOURCE.txt the entries are made for linking those .py files.

4. The src is the folder for application runtime. It contain all the necessary files and API code for your ML model. 

5. 














