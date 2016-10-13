# fix imports for appengine environments
import fix_imports
(fix_imports)

from tg import AppConfig, TGController, expose
from modules.home.homeController import HomeController
from modules.account.AccountController import AccountController

# =======================
# here's where we define all included modules for our application
# =======================
class RootController(TGController):
    home = HomeController()
    account = AccountController()
    # user = UserController()
    # sample = SampleController()

    @expose()
    def index(self):
        # go to http://localhost:8080, you should see this message
        return "it works!"

config = AppConfig(minimal=True, root_controller=RootController())
main = config.make_wsgi_app()