# nasa_apod

## Get NASA_API_KEY
Get your Api-Key from https://nasa.api.gov

## Create conda environment
Create and activate a conda environment

```
conda create -n nasa_apod_conda_env
conda activate nasa_apod_conda_env
```

## Create environment variable for NASA_API_KEY 
```
conda env config vars set NASA_API_KEY="<add here your api_key>"
```

You need to reactivate the environment
```
conda deactivate
conda activate nasa_apod_conda_env
```

You can check, if the environment variable is set with
```
conda env config vars list
```

## Import required packages 
Import the required packages with requirements.txt via conda
```
conda install --yes --file requirements.txt
```

## Run main.py
```
python main.py
```