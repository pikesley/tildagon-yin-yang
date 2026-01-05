# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps//"

if "github_user_tildagon_yin_yang" in apps:
    ASSET_PATH = "/apps/github_user_tildagon_yin_yang/"

if "yin_yang" in apps:
    ASSET_PATH = "apps/yin_yang/"
