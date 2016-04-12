from pyramid import view, httpexceptions, security
from spree import rest


@view.view_defaults(context=rest.APIEndpoint)
class MyView(rest.TraversalRESTView):
    pass


@view.forbidden_view_config()
def basic_challenge(request):
    response = httpexceptions.HTTPUnauthorized()
    response.headers.update(security.forget(request))
    return response
