from subimage import cli


def test_parse_args(self):
    parser = cli.parse_args(["-l", "-m"])
    self.assertTrue(parser.long)
