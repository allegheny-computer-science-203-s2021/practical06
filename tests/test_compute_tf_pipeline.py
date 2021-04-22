"""Using Hypothesis, check the correctness of the pipeline-based implementation."""

import pytest

from hypothesis import given
from hypothesis import settings
from hypothesis import Verbosity
from hypothesis.strategies import text

from termfrequency import compute_tf_pipeline

# TODO: Make sure that you understand the three types of tests in this suite
# --> Simple test with a single input
# --> Parameterized test with multiple inputs
# --> Property test with multiple automatically generated inputs

# TODO: Try to transform all of the tests that you wrote for the previously
# practical assignment into new tests that leverage strategies from Hypothesis!


def test_scan_splits_string_correctly():
    """Check that scan function finds the correct number of words in the String."""
    input_string = "Mr. Bingley and Jane remained at Netherfield only a twelvemonth."
    expected_count = 10
    assert len(compute_tf_pipeline.scan(input_string)) == expected_count


@pytest.mark.parametrize(
    "input_string,expected_count",
    [("hello world", 2), ("hello world again", 3), ("", 0), (" ", 0), (" ", 0)],
)
def test_scan_splits_string_correctly_parameterized(input_string, expected_count):
    """Check iteratively that scan function finds the correct number of words in the String."""
    assert len(compute_tf_pipeline.scan(input_string)) == expected_count


@given(input_string=text(min_size=1, max_size=100))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_scan_splits_string_correctly_automated_bounded(input_string):
    """Check that scan function finds words in bounded automatically created strings."""
    number_of_characters = len(input_string)
    scanned_string_list = compute_tf_pipeline.scan(input_string)
    print(f"scanned {input_string} to make scanned_string: {scanned_string_list}")
    assert isinstance(scanned_string_list, list)
    assert len(scanned_string_list) <= number_of_characters


@given(input_string=text())
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_scan_splits_string_correctly_automated_unbounded(input_string):
    """Check that scan function finds words in unbounded automatically created strings."""
    number_of_characters = len(input_string)
    scanned_string_list = compute_tf_pipeline.scan(input_string)
    print(f"scanned {input_string} to make scanned_string: {scanned_string_list}")
    assert isinstance(scanned_string_list, list)
    assert len(scanned_string_list) <= number_of_characters


def test_filter_normalize_correctly_example():
    """Check that filter-normalize function strips non-alpha-numeric symbols."""
    input_string = "Mr. Bingley and Jane remained at Netherfield only a twelvemonth."
    filtered_normalized_string = compute_tf_pipeline.filter_chars_and_normalize(
        input_string
    )
    print(
        f"filtered-normalized {input_string} to make the string: {filtered_normalized_string}"
    )
    assert isinstance(filtered_normalized_string, str)
    assert len(input_string) >= len(filtered_normalized_string)
    assert isinstance(compute_tf_pipeline.scan(filtered_normalized_string), list)
    for word in compute_tf_pipeline.scan(filtered_normalized_string):
        assert word.isalnum()
        assert not word.isspace()


@pytest.mark.parametrize(
    "input_string",
    [
        ("hello world"),
        ("hello world again"),
        (""),
        (" "),
        (" "),
        ("!"),
        ("."),
        ("%"),
        ("\n"),
        ("\\"),
    ],
)
def test_filter_normalize_correctly_parameterized(input_string):
    """Check iteratively that filter-normalize function strips non-alpha-numeric symbols."""
    filtered_normalized_string = compute_tf_pipeline.filter_chars_and_normalize(
        input_string
    )
    print(
        f"filtered-normalized {input_string} to make the string: {filtered_normalized_string}"
    )
    assert isinstance(filtered_normalized_string, str)
    assert len(input_string) >= len(filtered_normalized_string)
    assert isinstance(compute_tf_pipeline.scan(filtered_normalized_string), list)
    for word in compute_tf_pipeline.scan(filtered_normalized_string):
        assert word.isalnum()
        assert not word.isspace()


@given(input_string=text(min_size=1, max_size=100))
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_filter_normalize_correctly_automated_bounded(input_string):
    """Check that filter-normalize function strips non-alnum in bounded auto-created strings."""
    filtered_normalized_string = compute_tf_pipeline.filter_chars_and_normalize(
        input_string
    )
    print(
        f"filtered-normalized {input_string} to make the string: {filtered_normalized_string}"
    )
    assert isinstance(filtered_normalized_string, str)
    assert len(input_string) >= len(filtered_normalized_string)
    assert isinstance(compute_tf_pipeline.scan(filtered_normalized_string), list)
    for word in compute_tf_pipeline.scan(filtered_normalized_string):
        assert word.isalnum()
        assert not word.isspace()


@given(input_string=text())
@settings(verbosity=Verbosity.verbose, deadline=None)
@pytest.mark.hypothesisworks
def test_filter_normalize_correctly_automated_unbounded(input_string):
    """Check that filter-normalize function strips non-alnum in bounded auto-created strings."""
    filtered_normalized_string = compute_tf_pipeline.filter_chars_and_normalize(
        input_string
    )
    print(
        f"filtered-normalized {input_string} to make the string: {filtered_normalized_string}"
    )
    assert isinstance(filtered_normalized_string, str)
    assert len(input_string) >= len(filtered_normalized_string)
    assert isinstance(compute_tf_pipeline.scan(filtered_normalized_string), list)
    for word in compute_tf_pipeline.scan(filtered_normalized_string):
        assert word.isalnum()
        assert not word.isspace()
