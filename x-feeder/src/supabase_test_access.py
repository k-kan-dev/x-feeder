import os
import configparser
from supabase import create_client, Client
from dotenv import load_dotenv, find_dotenv

parser = configparser.ConfigParser()
parser.read("./x-feeder/config/cfg.ini")

# `.env` ファイルを明示的に探してロード
env_path = find_dotenv("./x-feeder/config/.env")
if env_path == "":
    raise FileNotFoundError(".env ファイルが見つかりません。ルートディレクトリに作成してください。")
load_dotenv(env_path)

# 環境変数の取得
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")  # 管理用キー
SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")  # クライアント用キー（未使用なら削除可）

# 環境変数のチェック
if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    raise ValueError("環境変数が正しく設定されていません。")

# Supabaseクライアントを作成
supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# データを挿入
data = {"id": "1", "Contents": "xxx"}
response = supabase.table(parser["DEFAULT"]["SUPABASE_DATABASE_NAME"]).insert(data).execute()
print(response)
