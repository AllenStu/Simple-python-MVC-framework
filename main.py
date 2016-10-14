from modules.account.AccountController import AccountController
from modules.gcloud_samples.gcloud_samples_controller import GCloudSamplesController
from modules.home.homeController import HomeController
from tg import TGController
from tg import expose


class MainController(TGController):

    home = HomeController()
    account = AccountController()
    gcloud_samples = GCloudSamplesController()

    @expose()
    def index(self):
        # go to http://localhost:8080, you should see this message
        return "it works!"