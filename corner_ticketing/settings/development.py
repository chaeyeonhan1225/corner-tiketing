from .base import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

try:
    with open(f"{BASE_DIR}/credentials-dev.json", "r") as f:
        CREDENTIALS = json.load(f)
except FileNotFoundError:
    print("설정 파일이 없습니다!")

TEST_SENDER_EMAIL = "gkscodus11@gmail.com"
TEST_RECEIVER_EMAIL = "gkscodus11@naver.com"
GMAIL_APP_PASSWORD = CREDENTIALS["GMAIL_APP_PASSWORD"]
