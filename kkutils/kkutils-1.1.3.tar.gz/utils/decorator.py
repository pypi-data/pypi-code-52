#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Author: zhangkai
Last modified: 2019-11-12 16:04:04
'''
import functools
import logging
import time


def synchronize(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        return self.loop.create_task(func(self, *args, **kwargs))
    return wrapper


def smart_decorator(decorator):
    def wrapper(func=None, **kwargs):
        if func is not None:
            return decorator(func=func, **kwargs)

        @functools.wraps(func)
        def wrapper(func):
            return decorator(func=func, **kwargs)
        return wrapper
    return wrapper


def timeit(func):
    logger = logging.getLogger()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        logger.info(f'{func.__name__} cost time: {time.time() - start_time:.5f}')
        return result
    return wrapper


@smart_decorator
def retry(func, count=2, raise_error=False):
    logger = logging.getLogger()

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(count):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                logger.exception(f'running exception: {e}, retry: {i + 1}')
                if raise_error and i == count - 1:
                    raise
    return wrapper


@smart_decorator
def aioretry(func, count=2, raise_error=False):
    logger = logging.getLogger()

    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        for i in range(count):
            try:
                return await func(*args, **kwargs)
            except Exception as e:
                logger.exception(f'running exception: {e}, retry: {i + 1}')
                if raise_error and i == count - 1:
                    raise
    return wrapper
