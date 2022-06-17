from test_base import BaseTest
from page_methods_make_my_trip import MakeMyTripPageFunctions


class TestMakeMyTrip(BaseTest):

    def test_make_my_trip(self):
        self.fun = MakeMyTripPageFunctions(self.driver)
        self.fun.GetTitles()
        self.fun.SelectCity()

