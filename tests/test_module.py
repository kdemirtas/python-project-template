import os
import unittest

import numpy as np

from project_template import module


class ProjectTemplate(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_module_print_module(self):
        module.print_module()


if __name__ == "__main__":
    unittest.main()