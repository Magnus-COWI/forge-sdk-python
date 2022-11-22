"""
Clients for communicating with different Autodesk Forge services.
"""

from .auth import AuthenticationClient, Scope, get_authorization_url
from .auth import TokenProviderInterface, SimpleTokenProvider, OAuthTokenProvider
from .datam import OSSClient, DataManagementClient
from .md import ModelDerivativeClient, urnify
from .docm import DocumentManagementClient, Action, Subject
from .accm import AccountManagementClient
from .webhooks import WebhooksClient
