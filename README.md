# X-feeder

## dev-env
- Windows11
- python
  - 3.12.9
- pyenv
  - 3.11
- poetry
  - 2.1.1
- ex. (PowerShell)
    ```PowerShell
    PS pyenv install 3.11.9
    PS pyenv local 3.11.9
    PS python --version
    Python 3.11.9
    PS pip install poetry
    ```
# test

1. create `./config/.env`
    ```txt
    SUPABASE_URL = https://xxxxxxx.supabase.co
    SUPABASE_KEY = exxxxxxxxx
    SUPABASE_SERVICE_KEY = xxxxxxxxxxxx
    ```
1.  command ex
    ```PowerShell
    PS poetry run uvicorn src.main:app --reload

    ```
1. vercel --local-config ./config/vercel.json

# deploy 

1. 
    ```PowerShell
    PS vercel --local-config ./config/vercel.json --prod
    ```

## supabase
1. see `API settings > Data API` @ supabase
1. write down env-variables into `config/.env`
```PowerShell
PS cat config/.env
SUPABASE_URL = https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SUPABASE_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SUPABASE_SERVICE_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
