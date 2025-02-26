import os
import configparser
from fastapi import FastAPI
from supabase import create_client
from dotenv import load_dotenv


parser = configparser.ConfigParser()
parser.read("./config/cfg.ini")
# .envの読み込み
load_dotenv("./config/.env")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # クライアント用キー（未使用なら削除可）

# Supabaseクライアントの作成
supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, Vercel + FastAPI!"}

@app.get("/timetable")
def get_users():
    response = supabase.table(parser["DEFAULT"]["SUPABASE_DATABASE_NAME"]).select("*").execute()
    return response.data
