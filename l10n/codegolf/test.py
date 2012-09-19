import unittest
import subprocess

class BaseTest(unittest.TestCase):
    def test_value_1(self): self.call(1, "1")
    def test_value_12(self): self.call(12, "12")
    def test_value_123(self): self.call(123, "123")
    def test_value_1234(self): self.call(1234, "1.234")
    def test_value_12345(self): self.call(12345, "12.345")
    def test_value_123456(self): self.call(123456, "123.456")
    def test_value_1234567(self): self.call(1234567, "1.234.567")
    def test_value_123456789(self): self.call(123456789, "123.456.789")
    def test_value_1_1(self): self.call(1.1, "1,1")
    def test_value_12_12(self): self.call(12.12, "12,12")
    def test_value_123_123(self): self.call(123.123, "123,123")
    def test_value_1234_1234(self): self.call(1234.1234, "1.234,1234")
    def test_value_1999995_99(self): self.call(1999995.99, "1.999.995,99")
    def test_value_minus_1(self): self.call(-1, "-1")
    def test_value_minus_10(self): self.call(-10, "-10")
    def test_value_minus_100(self): self.call(-100, "-100")
    def test_value_minus_1000(self): self.call(-1000, "-1.000")
    def test_value_minus_100000(self): self.call(-100000, "-100.000")
    def test_value_minus_1000000(self): self.call(-1000000, "-1.000.000")
    def test_value_minus_1_1(self): self.call(-1.1, "-1,1")
    def test_value_minus_12_12(self): self.call(-12.12, "-12,12")
    def test_value_minus_123_123(self): self.call(-123.123, "-123,123")
    def test_value_minus_1234_1234(self): self.call(-1234.1234, "-1.234,1234")

    def test_decimal_1(self): self.call('decimal.Decimal(\'1\')', "1")
    def test_decimal_12(self): self.call('decimal.Decimal(\'12\')', "12")
    def test_decimal_123(self): self.call('decimal.Decimal(\'123\')', "123")
    def test_decimal_1234(self): self.call('decimal.Decimal(\'1234\')', "1.234")
    def test_decimal_12345(self): self.call('decimal.Decimal(\'12345\')', "12.345")
    def test_decimal_123456(self): self.call('decimal.Decimal(\'123456\')', "123.456")
    def test_decimal_1234567(self): self.call('decimal.Decimal(\'1234567\')', "1.234.567")
    def test_decimal_123456789(self): self.call('decimal.Decimal(\'123456789\')', "123.456.789")
    def test_decimal_1_1(self): self.call('decimal.Decimal(\'1.1\')', "1,1")
    def test_decimal_12_12(self): self.call('decimal.Decimal(\'12.12\')', "12,12")
    def test_decimal_123_123(self): self.call('decimal.Decimal(\'123.123\')', "123,123")
    def test_decimal_1234_1234(self): self.call('decimal.Decimal(\'1234.1234\')', "1.234,1234")
    def test_decimal_1999995_99(self): self.call('decimal.Decimal(\'1999995.99\')', "1.999.995,99")
    def test_decimal_minus_1(self): self.call('decimal.Decimal(\'-1\')', "-1")
    def test_decimal_minus_10(self): self.call('decimal.Decimal(\'-10\')', "-10")
    def test_decimal_minus_100(self): self.call('decimal.Decimal(\'-100\')', "-100")
    def test_decimal_minus_1000(self): self.call('decimal.Decimal(\'-1000\')', "-1.000")
    def test_decimal_minus_100000(self): self.call('decimal.Decimal(\'-100000\')', "-100.000")
    def test_decimal_minus_1000000(self): self.call('decimal.Decimal(\'-1000000\')', "-1.000.000")
    def test_decimal_minus_1_1(self): self.call('decimal.Decimal(\'-1.1\')', "-1,1")
    def test_decimal_minus_12_12(self): self.call('decimal.Decimal(\'-12.12\')', "-12,12")
    def test_decimal_minus_123_123(self): self.call('decimal.Decimal(\'-123.123\')', "-123,123")
    def test_decimal_minus_1234_1234(self): self.call('decimal.Decimal(\'-1234.1234\')', "-1.234,1234")

    def test_string_1(self): self.call("'1'", "1")
    def test_string_12(self): self.call("'12'", "12")
    def test_string_123(self): self.call("'123'", "123")
    def test_string_1234(self): self.call("'1234'", "1.234")
    def test_string_12345(self): self.call("'12345'", "12.345")
    def test_string_123456(self): self.call("'123456'", "123.456")
    def test_string_1234567(self): self.call("'1234567'", "1.234.567")
    def test_string_123456789(self): self.call("'123456789'", "123.456.789")
    def test_string_1_1(self): self.call("'1.1'", "1,1")
    def test_string_12_12(self): self.call("'12.12'", "12,12")
    def test_string_123_123(self): self.call("'123.123'", "123,123")
    def test_string_1234_1234(self): self.call("'1234.1234'", "1.234,1234")
    def test_string_1999995_99(self): self.call("'1999995.99'", "1.999.995,99")
    def test_string_minus_1(self): self.call("'-1'", "-1")
    def test_string_minus_10(self): self.call("'-10'", "-10")
    def test_string_minus_100(self): self.call("'-100'", "-100")
    def test_string_minus_1000(self): self.call("'-1000'", "-1.000")
    def test_string_minus_100000(self): self.call("'-100000'", "-100.000")
    def test_string_minus_1000000(self): self.call("'-1000000'", "-1.000.000")
    def test_string_minus_1_1(self): self.call("'-1.1'", "-1,1")
    def test_string_minus_12_12(self): self.call("'-12.12'", "-12,12")
    def test_string_minus_123_123(self): self.call("'-123.123'", "-123,123")
    def test_string_minus_1234_1234(self): self.call("'-1234.1234'", "-1.234,1234")

    def call(self, arg, value):
        result = subprocess.check_output([self.pyversion, "-c", 
                """import decimal,%s;print(%s.f(%s))""" % (self.lib, self.lib,
                    arg)])
        result = result.strip("\n")
        self.assertEqual(result, "%s" % value, 
            "%r resulted in %r, should be %r" % (arg, result, value))

class Codegolf3Test(BaseTest):
    pyversion="python3"
    lib="codegolf3"

class Codegolf2Test(BaseTest):
    pyversion="python2"
    lib="codegolf2"

class Codegolf2_2PY2Test(BaseTest):
    pyversion="python2"
    lib="codegolf2_2"

class Codegolf2_2PY3Test(BaseTest):
    pyversion="python3"
    lib="codegolf2_2"

test_classes = (Codegolf2Test, Codegolf3Test, Codegolf2_2PY2Test, Codegolf2_2PY3Test)

def load_tests():
    suite = unittest.TestSuite()
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(load_tests())
