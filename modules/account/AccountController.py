from tg import TGController, expose

from modules.home.homeService import HomeService
from packages.tg.controllers.util import redirect

class AccountController(TGController):

    @expose()
    def index(self):
        return "account controller"
