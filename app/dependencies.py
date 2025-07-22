from app.providers.test_provider import TestProvider
from app.providers.base import BaseProvider
from app.config import settings

# Global provider instances to persist state
_test_provider_instance = None


def get_provider() -> BaseProvider:
    """Get the appropriate provider based on config"""
    global _test_provider_instance
    
    if settings.PROVIDER == "test":
        if _test_provider_instance is None:
            _test_provider_instance = TestProvider()
        return _test_provider_instance
    # elif settings.PROVIDER == "zenoti":
    #     return ZenotiProvider()
    else:
        raise ValueError(f"Unknown provider: {settings.PROVIDER}") 