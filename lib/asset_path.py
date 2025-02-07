# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps//"

if "github_user_tildagon_skellington" in apps:
    ASSET_PATH = "/apps/github_user_tildagon_skellington/"

if "skellington" in apps:
    ASSET_PATH = "apps/skellington/"
