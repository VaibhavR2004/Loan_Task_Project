import unittest


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.discover("tests")

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


if __name__ == "__main__":
    print("Running Engineer 3 Tests...\n")
    run_tests()