import pytest_asyncio
from sqlalchemy.orm import sessionmaker


@pytest_asyncio.fixture(scope='function')
async def async_session(async_db_engine):
    async with sessionmaker() as session:
        try:
            yield session
        except:
            await session.rollback()
            raise
        finally:
            await session.close()