import os
import configparser
from fastapi import FastAPI
from fastapi.responses import FileResponse
from supabase import create_client
from dotenv import load_dotenv

from .lib.x import X

parser = configparser.ConfigParser()
parser.read("./x-feeder/config/cfg.ini")
# .envの読み込み
load_dotenv("./x-feeder/config/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # クライアント用キー（未使用なら削除可）

# Supabaseクライアントの作成
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

app = FastAPI()
FAVICON_PATH = os.path.join(
    os.path.dirname(__file__),
    "static",
    "favicon.ico"
)

x = X()

@app.get("/")
def home():
    return {"message": "Hello, Vercel + FastAPI!"}

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return FileResponse(FAVICON_PATH)

@app.get("/get_tweets")
def get_users():
    user_id = x.get_user_id(
        username = parser["DEFAULT"]["X_TOF_ACCOUNT_NAME"]
    )
    tweets = x.get_tweets(
        user_id = user_id,
        max_results = 5
    )

    # response = supabase.table(parser["DEFAULT"]["SUPABASE_DATABASE_NAME"]).select("*").execute()
    return tweets
