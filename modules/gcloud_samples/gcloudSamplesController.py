from tg import TGController, expose


class GCloudSamplesController(TGController):

    @expose()
    def index(self):
        return "gcloud samples"


    @expose()
    def cloud_storage(self):
        pass
