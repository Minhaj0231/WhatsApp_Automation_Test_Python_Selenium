

from unittest import TestLoader, TestSuite, TextTestRunner

from tests.TC001_search_test import SearchTest
from tests.TC002_send_message import SendMessageTest
from tests.TC003_successfully_msg_sent import SuccessFullyMsgSent
from tests.TC004_msg_seen import MsgSeen
from tests.TC005_log_out import LogOutTest


if __name__ == "__main__" :

    
    test_loader = TestLoader()
    test_suite = TestSuite((

        test_loader.loadTestsFromTestCase(SearchTest),
        # test_loader.loadTestsFromTestCase(SendMessageTest),
        # test_loader.loadTestsFromTestCase(SuccessFullyMsgSent),
        # test_loader.loadTestsFromTestCase(MsgSeen),
        # test_loader.loadTestsFromTestCase(LogOutTest)

        

    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

