import os
#ok
ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Var
elif os.path.exists("config.py"):
    from config import Development as Var
