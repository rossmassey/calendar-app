from app.providers.test_provider import TestProvider
from app.providers.zenoti_provider import ZenotiProvider
from app.providers.base import BaseProvider
from app.config import settings


def get_provider() -> BaseProvider:
    """Dependency to get the appropriate provider based on config"""
    if settings.PROVIDER == "test":
        return TestProvider()
    elif settings.PROVIDER == "zenoti":
        return ZenotiProvider()
    # Future: elif settings.PROVIDER == "gcal": return GCalProvider()
    # Future: elif settings.PROVIDER == "boulevard": return BoulevardProvider()
    else:
        raise ValueError(f"Unknown provider: {settings.PROVIDER}") 