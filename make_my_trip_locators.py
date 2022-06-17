from selenium.webdriver.common.by import By


class MakeMyTripLocators:

    Hand_picked_collections_Titles = [By.XPATH, '//div[@class="hpClcn__slider--itemDesc"]//p[@class="latoBold font16 lineHeight22 whiteText"]']
    Relaxation_destination = [By.XPATH, '//a[@data-test="tripIdeaWrapper_list_9"]']
    scroll_down_to_element = [By.XPATH, '//div[@class="appDnldCnt appendBottom20 "]']
    scroll_down = [By.XPATH, '//p[@class="tpDest__heading"]']
    slide_to_last = [By.XPATH, '(//button[@class="slick-arrow slick-next"])[3]']
    select_city = [By.XPATH, '//div[@class="fromTextWraper"]']
    main_city_name = [By.XPATH, '(//ul[@class="PopularCitiesstyles__CityList-d8r2qv-1 fwGpxo"]//a)[1]']
    city_name = [By.XPATH, '//h1']
    activities = [By.XPATH, '//div[@class="SearchByCardStyle__MiddleTab-sc-102ccav-2 hZjoUk"]/a[4]']
    activity_price = [By.XPATH, '//span[@class="ActivitiesCard__NewPrice-vy7c9s-6 hBnscK"]']
    close_span = [By.XPATH, '//span[@class="langCardClose"]']
    highlights = [By.XPATH, '//a[@data-href="#highlights"]']
    highlights_text = [By.XPATH, '//div[@class="whyShouldIDoList"]']
    activity_title = [By.XPATH, '//p[@class="product-title"]']

    @staticmethod
    def destination_cities(item):
        return By.XPATH, '(//div[@class="DestinationCard__Card-sc-1czmno9-0 oivJt"])['+ str(item) +']'

    @staticmethod
    def activity_header_name(item):
        return By.XPATH, '(//span[@class="ActivitiesCard__NewPrice-vy7c9s-6 hBnscK"])[' + str(item) + ']'
