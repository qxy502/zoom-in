import json
from pathlib import Path

from flask import Flask, render_template


app = Flask(__name__)


# ============================================================
# 项目目录
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


# ============================================================
# JSON 文件
# ============================================================

TOPIC_FILE = (
    BASE_DIR / "yuanmingyuan_topic.json"
)

DAILY_CHALLENGE_FILE = (
    BASE_DIR / "yuanmingyuan_daily_challenge.json"
)


# ============================================================
# 读取 JSON
# ============================================================

def load_json(path):

    with path.open(
        "r",
        encoding="utf-8",
    ) as file:

        return json.load(file)


# ============================================================
# 首页
# ============================================================

@app.route("/")
def home():

    daily_challenge = load_json(
        DAILY_CHALLENGE_FILE
    )

    return render_template(
        "index.html",
        daily_challenge=daily_challenge,
    )


# ============================================================
# 每日挑战
# ============================================================

@app.route("/challenge")
def challenge():

    daily_challenge = load_json(
        DAILY_CHALLENGE_FILE
    )

    return render_template(
        "challenge.html",
        daily_challenge=daily_challenge,
    )


# ============================================================
# 圆明园详情页
# ============================================================

@app.route("/topic/yuanmingyuan")
def yuanmingyuan():

    topic = load_json(
        TOPIC_FILE
    )

    return render_template(
        "yuanmingyuan.html",
        topic=topic,
    )


# ============================================================
# 用户中心
# ============================================================

@app.route("/profile")
def profile():

    return render_template(
        "profile.html"
    )


# ============================================================
# 积分商城
# ============================================================

@app.route("/shop")
def shop():

    return render_template(
        "shop.html"
    )


# ============================================================
# 启动网站
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )