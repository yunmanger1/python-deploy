from twisted.application import internet, service
from twisted.web import server
from txrestapi.resource import APIResource
from txrestapi.methods import GET


class MyResource(APIResource):

    @GET('^/')
    def index(self, request):
        return 'Hello World!'

PORT = 8080
api = MyResource()

# initializing web application
application = service.Application('web')
site = server.Site(api)
# Do not display tracebacks if in production
site.displayTracebacks = True
sc = service.IServiceCollection(application)
i = internet.TCPServer(PORT, site, \
    interface='')
i.setServiceParent(sc)
