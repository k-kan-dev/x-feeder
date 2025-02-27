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

## supabase
1. see `API settings > Data API` @ supabase
1. write down env-variables into `config/.env`
```PowerShell
PS cat config/.env
SUPABASE_URL = https://xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SUPABASE_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SUPABASE_SERVICE_KEY = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
