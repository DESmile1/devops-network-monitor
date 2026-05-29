import unittest
import monitor


class TestNetworkMonitor(unittest.TestCase):

    def test_servers_list_not_empty(self):
        # ??At least one item in the list of servers
        self.assertTrue(len(monitor.servers) > 0)


if __name__ == "__main__":
    unittest.main()