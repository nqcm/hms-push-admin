import requests


def post(url, req_body, headers=None, verify_peer=False):
    """post http request to slb service
    :param url: url path
    :param req_body: http request body
    :param headers: http headers
    :param verify_peer:  (optional) Either a boolean, in which case it controls whether we verify
        the server's TLS certificate, or a string, in which case it must be a path
        to a CA bundle to use. Defaults to ``True``.
    :return:
        success return response
        fali return None
    """
    try:
        response = requests.post(
            url, data=req_body, headers=headers, timeout=10, verify=verify_peer
        )
        return response

    except Exception as e:
        raise ValueError("caught exception when post {0}. {1}".format(url, e))


def _format_http_text(method, url, headers, body):
    """
    print http head and body for request or response

    For examples: _format_http_text('', title, response.headers, response.text)
    """
    result = method + " " + url + "\n"

    if headers is not None:
        for key, value in headers.items():
            result = result + key + ": " + value + "\n"

    result = result + body
    return result
