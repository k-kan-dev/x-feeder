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
    PS poetry install
    ```
# deployment

## local-env

1. see `API settings > Data API` @ supabase
1. create `.\x-feeder\config\.env`
    ```txt
    SUPABASE_URL = https://xxxxxxx.supabase.co
    SUPABASE_KEY = exxxxxxxxx
    SUPABASE_SERVICE_KEY = xxxxxxxxxxxx
    ```

1.  
    ```PowerShell
    PS poetry run uvicorn x-feeder.src.main:app --reload
    ```
## test-env

1. `vercel --local-config .\x-feeder\config\vercel.json`
    - ex.
    ```PowerShell
    PS vercel --local-config .\x-feeder\config\vercel.json
    Vercel CLI 41.2.2
    🔍  Inspect: https://vercel.com/PROJECT_NAME/x-feeder/6Vz216U4N1ySvH4Z9kyMUvZamR2f [2s]
    ✅  Preview: https://x-feeder-ks9r0jxyx-PROJECT-NAME.vercel.app [2s]
    📝  To deploy to production (x-feeder.vercel.app), run `vercel --prod`
    ❗️  Due to `builds` existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply. Learn More: https://vercel.link/unused-build-settings
    ```

## prod-env 

1. `vercel --local-config .\x-feeder\config\vercel.json --prod`
    - ex.
    ```PowerShell
    PS vercel --local-config .\x-feeder\config\vercel.json --prod
    Vercel CLI 41.2.2
    🔍  Inspect: https://vercel.com/PROJECT-NAME/x-feeder/Gjr2bu1mnjXhtfcYsHGYYT4M4wKd [956ms]
    ✅  Production: https://x-feeder-q3oizcgam-PROJECT-NAME.vercel.app [956ms]
    ❗️  Due to `builds` existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply. Learn More: https://vercel.link/unused-build-settings
    ```

