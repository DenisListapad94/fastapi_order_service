import pytest_asyncio
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from src.core.config import settings
from src.core.orm import Base

TEST_URL = f'postgresql+asyncpg://{settings.db.user}:{settings.db.password}@{settings.db.host}:{settings.db.port}/{settings.db.test_name}'
test_async_engine = create_async_engine(url=TEST_URL,echo=True,)
async_session_maker = sessionmaker(
    test_async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@pytest_asyncio.fixture(scope='session')
async def async_db_engine():
    async with test_async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.create_all)

    yield test_async_engine

    async with test_async_engine.begin() as connect:
        await connect.run_sync(Base.metadata.drop_all)


