# fastapi-aiogram3-template

Personal template for FastApi & Aiogram3

Feel free to use :)

Requirements:
<ul>
    <li>python = "^3.12"</li>
    <li>aiogram = "^3.3.0"</li>
    <li>fastapi = "^0.109.0"</li>
    <li>uvicorn = "^0.27.0.post1"</li>
    <li>environs = "^10.3.0"</li>
    <li>sqlalchemy = "^2.0.28"</li>
    <li>alembic = "^1.13.1"</li>
    <li>asyncpg = "^0.29.0"</li>
</ul>

## How to make migrations?
1) Import module with models to `migrations/base.py`.

2) Execute a command to make migration file
    ```
    alembic revision --autogenerate -m 'Model name or migration title'
    ```
3) Check the created migration file. WARNING!!! Alembic can't do model renaming automatically.

4) Make migration (make changes in db)
    ```
    alembic upgrade head
    ```