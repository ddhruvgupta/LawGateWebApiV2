## New Setup ##

Create Env

```
> mkdir myproject
> cd myproject
> py -3 -m venv ~/Downloads/virtual-envs/LawGateWebApiV2

py -3 -m venv .venv (orginally used)
```

Activate env

```
.venv\Scripts\activate
```

Install Flask

```
pip install Flask
```

```
pip freeze > requirements.txt
pip install -r requirements.txt
```


## Restart App ## 

=> just choose the python interpreter in VSCode, set it up to use the venv that was setup above. 


1. create virtual env in the downloads directory
2. activate env
3. install dependencies from `requirequirements.txt`

TODO: Can we rename the virtual environment to something other than venv ?