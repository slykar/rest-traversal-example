from pyramid import view, httpexceptions, security


@view.forbidden_view_config()
def basic_challenge(request):
    response = httpexceptions.HTTPUnauthorized()
    response.headers.update(security.forget(request))
    return response
