def pytest_runtest_setup(item):
    item.config.option.base_url = item.config.option.base_url.replace('/b', '')
