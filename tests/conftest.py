import pytest_asyncio
import asyncio

pytest_plugins = [
    "tests.fixtures.client",
    "tests.fixtures.database",
    "tests.fixtures.async_session",
]

@pytest_asyncio.fixture(scope='session')
def event_loop():
    policy = asyncio.get_event_loop_policy()
    loop = policy.new_event_loop()
    yield loop
    loop.close()