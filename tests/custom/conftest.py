from dotenv import load_dotenv
import os
import pytest

from fluidstack.client import FluidStack

load_dotenv()


@pytest.fixture
def fluidstack_settings():
    return os.getenv("FLUIDSTACK_API_KEY"), os.getenv("FLUIDSTACK_API_URL")


@pytest.fixture
def fluidstack_client(fluidstack_settings):
    return FluidStack(api_key=fluidstack_settings[0], base_url=fluidstack_settings[1])
