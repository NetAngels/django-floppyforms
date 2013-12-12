# -*- coding: utf-8 -*-
from django.conf import settings

USE_REQUIRE_ATTR = getattr(settings, "FLOPPYFORMS_USE_REQUIRE_ATTR", True)
USE_HTML5_TYPES = getattr(settings, "FLOPPYFORMS_USE_HTML5_TYPES", True)
