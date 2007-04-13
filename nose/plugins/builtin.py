"""
Lists builtin plugins
"""

from nose.plugins.attrib import AttributeSelector
from nose.plugins.capture import Capture
from nose.plugins.cover import Coverage
from nose.plugins.debug import Pdb
from nose.plugins.deprecated import Deprecated
from nose.plugins.doctests import Doctest
## from nose.plugins.isolation import 
from nose.plugins.prof import Profile
from nose.plugins.skip import Skip

plugins = [
    AttributeSelector,
    Capture,
    Coverage,
    Deprecated,
    Doctest,
    Pdb,
    Profile,
    Skip]