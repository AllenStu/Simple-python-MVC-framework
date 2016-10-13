from tg import TGController, expose

from modules.home.homeService import HomeService
from tg.controllers.util import redirect

class HomeController(TGController):

    @expose()
    def index(self):
        redirect("home/list")

    @expose()
    def create(self):
        # creation of home entity in datastore service
        data = HomeService().create()
        return data.key.urlsafe()

    @expose()
    def edit(self):
        return "home edit page"

    @expose()
    def delete(self):
        return "home edit page"

    @expose()
    def list(self):
        return "home list page"