import time
from Make_my_trip_Locators import MakeMyTripLocators
from basePage import BasePage
import pandas as pd
from pprint import pprint

data = pd.read_csv("data.csv")


class MakeMyTripPageFunctions(BasePage):

    '''___________Constructor___________'''

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(data['url'][0])   # launching make my trip browser can also be fetched by config.ini

        '''___________Page Actions____________'''

    def GetTitles(self):
        time.sleep(5)
        try:
            self.do_click(MakeMyTripLocators.close_span)
        except:
            time.sleep(1)

        # collecting hand picked collections titles
        self.scrollele(MakeMyTripLocators.scroll_down_to_element)
        time.sleep(5)
        titles = self.get_elements_text(MakeMyTripLocators.Hand_picked_collections_Titles)
        for x in titles:
            time.sleep(1)
            print(x.text)
            try:
                self.do_click(MakeMyTripLocators.slide_to_last)
            except:
                time.sleep(1)

        # selecting relaxation destination
        self.do_click(MakeMyTripLocators.Relaxation_destination)
        time.sleep(2)

    def SelectCity(self):
        global act_title, element, city_name
        time.sleep(5)

        # selecting city name
        self.do_click(MakeMyTripLocators.select_city)
        time.sleep(3)
        self.do_click(MakeMyTripLocators.main_city_name)
        time.sleep(3)

        # selecting destination cities
        for i in range(1, 6):
            self.do_click(MakeMyTripLocators.destination_cities(i))
            time.sleep(3)
            # fetching city name
            city_name = self.get_element_text(MakeMyTripLocators.city_name)
            time.sleep(3)

            # selecting activities
            self.scrollele(MakeMyTripLocators.activities)
            self.do_click(MakeMyTripLocators.activities)
            time.sleep(3)

            # fetching activity prices
            prices = self.get_elements_text(MakeMyTripLocators.activity_price)
            for k in prices:
                value = k.text
                value = value.strip('\u20B9')  # u20B9 stands for rupee symbol
                value = value.replace(",", "")
                val = int(value)

                if 2000 <= val <= 6000:
                    k.click()
                    self.switch_the_tab(1)

                    # fetching activity title
                    act_title = self.get_element_text(MakeMyTripLocators.activity_title)

                    time.sleep(5)
                    try:
                        # click on highlights
                        self.scrollele(MakeMyTripLocators.highlights)
                        time.sleep(2)
                        self.do_click(MakeMyTripLocators.highlights)

                        # fetch the highlights texts
                        element = self.get_element_text(MakeMyTripLocators.highlights_text)

                    except:
                        time.sleep(1)

                    lis = [{"city": city_name, "activities": [{'title': act_title, " price": val, " highlights": [element]}]}]
                    pprint(lis)
                    time.sleep(3)
                    self.close_current_tab()
                    self.switch_the_tab(0)
                    time.sleep(5)

                else:
                    pass
            self.page_back()

        time.sleep(3)




