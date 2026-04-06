# https://tildagon.badge.emfcamp.org/tildagon-apps/reference/ctx/#adding-images
import os

apps = os.listdir("/apps")
path = ""
ASSET_PATH = "apps//"

if "pikesley_tildagon_yin_yang" in apps:
    ASSET_PATH = "/apps/pikesley_tildagon_yin_yang/"

if "yin_yang" in apps:
    ASSET_PATH = "apps/yin_yang/"
