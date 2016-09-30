import os


# host
API_HOST = os.getenv("API_HOST", "http://cmss.updev.cn")
THEME_TOKEN = os.getenv("THEME_TOKEN", "2156f4a9-19db-462e-bda2-90304315ad21")

TEST = os.getenv("TEST", False)