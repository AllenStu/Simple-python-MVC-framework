# fix imports for appengine environments
import fix_imports
(fix_imports)

from tg import AppConfig
from main import MainController

config = AppConfig(minimal=True, root_controller=MainController())
app = config.make_wsgi_app()