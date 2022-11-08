#!/usr/bin/env python3

from boltons.strutils import slugify
import pyo3_mixed_include_exclude

assert pyo3_mixed_include_exclude.get_42() == 42
assert slugify("First post! Hi!!!!~1    ") == "first_post_hi_1"

print("SUCCESS")
