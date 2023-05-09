"""Huawei Admin SDK for Python."""

import threading
from hms.push_admin import _app

_apps = {}
_apps_lock = threading.RLock()
_DEFAULT_APP_NAME = "DEFAULT"


def initialize_app(
    appid_at,
    appsecret_at,
    appid_push=None,
    token_server="https://oauth-login.cloud.huawei.com/oauth2/v3/token",
    push_open_url="https://push-api.cloud.huawei.com",
):
    """
    Initializes and returns a new App instance.
    :param appid_at: appid parameters obtained by developer alliance applying for Push service
    :param appsecret_at: appsecret parameters obtained by developer alliance applying for Push service
    :param appid_push: the application Id in the URL
    :param token_server: Oauth server URL
    :param push_open_url: push open API URL
    """
    app = _app.App(
        appid_at,
        appsecret_at,
        appid_push,
        token_server=token_server,
        push_open_url=push_open_url,
    )

    with _apps_lock:
        if appid_at not in _apps:
            _apps[appid_at] = app

        """set default app instance"""
        if _apps.get(_DEFAULT_APP_NAME) is None:
            _apps[_DEFAULT_APP_NAME] = app


def get_app(appid=None):
    """
    get app instance
    :param appid: appid parameters obtained by developer alliance applying for Push service
    :return: app instance
    Raise: ValueError
    """
    if appid is None:
        with _apps_lock:
            app = _apps.get(_DEFAULT_APP_NAME)
            if app is None:
                raise ValueError(
                    "The default Huawei app is not exists. "
                    "This means you need to call initialize_app() it."
                )
            return app

    with _apps_lock:
        if appid not in _apps:
            raise ValueError(
                "Huawei app id[{0}] is not exists. "
                "This means you need to call initialize_app() it.".format(appid)
            )

        app = _apps.get(appid)
        if app is None:
            raise ValueError("The app id[{0}] is None.".format(appid))
        return app
