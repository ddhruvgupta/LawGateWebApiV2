## New Setup ##

Create Env

```
> mkdir myproject
> cd myproject
> py -3 -m venv C:\Users\Dhruv-PC\Downloads\virtual-envs\LawGateWebApiV2

py -3 -m venv .venv (orginally used)
```

Activate env

```C:\Users\Dhruv-PC\Downloads\virtual-envs\LawGateWebApiV2\Scripts\activate```

Install Flask

```pip install Flask```

```pip freeze > requirements.txt
pip install -r requirements.txt
```

## Restart App ##

=> just choose the python interpreter in VSCode, set it up to use the venv that was setup above.

1. create virtual env in the downloads directory
2. activate env
3. install dependencies from `requirequirements.txt`

TODO: Can we rename the virtual environment to something other than venv ?

`flask --app helloWorld.py run`
`flask --app app.py --env-file .env.dev run`

docker compose --env-file .env.dev up --build

## Troubleshooting database container ##

1. Login to container:
`docker exec -it <container_id_or_name> bash`
or use sh instead of bash

2. Login to mysql
`mysql -u root -p`

password is in the .env file.

3.Test DB connection
SHOW DATABASES;

4.Check permissions for DB_USER:

USE mysql;
SELECT User, Host, authentication_string FROM user;
