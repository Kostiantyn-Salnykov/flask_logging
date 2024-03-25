import itertools

import pytest

import logging

from pytest import LogCaptureFixture

from app import function_with_logs, function_to_log_message


def test_capture_logging__default_level(caplog: LogCaptureFixture) -> None:
    assert caplog.text == ""
    assert caplog.messages == []

    function_with_logs()

    assert caplog.messages == ["WARNING", "ERROR", "CRITICAL", "WARNING Flask", "ERROR Flask", "CRITICAL Flask"]


def test_capture_logging__debug_level(caplog: LogCaptureFixture) -> None:
    caplog.set_level(logging.DEBUG)
    assert caplog.text == ""
    assert caplog.messages == []

    function_with_logs()

    assert caplog.messages == [
        "DEBUG",
        "INFO",
        "WARNING",
        "ERROR",
        "CRITICAL",
        "DEBUG Flask",
        "INFO Flask",
        "WARNING Flask",
        "ERROR Flask",
        "CRITICAL Flask",
    ]


@pytest.mark.parametrize(
    argnames="func_name, message",
    argvalues=itertools.product(("debug", "info", "warning", "error", "critical"), ("TEST MESSAGE!",)),
)
def test_function_to_log_message__debug_level(caplog: LogCaptureFixture, func_name: str, message: str) -> None:
    caplog.set_level(logging.DEBUG)

    function_to_log_message(func_name=func_name, message=message)

    assert caplog.messages == ["TEST MESSAGE!"]
