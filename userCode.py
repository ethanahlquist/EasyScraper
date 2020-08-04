import time
import random
from scraper import SeleniumDriver
from scraper import ScrapElement
from data import draw_plot_from_csv
from selenium.webdriver.common.by import By

URL = 'https://www.intemag.com/magnet-pull-calculations-disc-magnet-with-steel-plate'
driver = SeleniumDriver()
driver.get(URL)

'''
I don't know how to do this better, but this is just so we can give all the
funtions access to the webdriver, without adding another param.
'''
def Element(by, token): return ScrapElement(by, token, driver)


e = {
    'diam': Element(By.NAME, 'diameter1'),
    'length': Element(By.NAME, 'length1'),
    'br': Element(By.NAME, 'br1'),
    'gauss': Element(By.XPATH,
                     '//*[@id="bodyContent"]/div[3]/div/form/div/table/tbody/tr[6]/td[2]/p'),
}


def csv_write_elements(e, dictwriter):

    # Maps row to the value field of the objects, not the element themselves
    row = dict(map(lambda pair: (pair[0], pair[1].value), e.items()))
    dictwriter.writerow(row)


def dataLoop(e, dictwriter):

    # Show what we are dealing with.
    print(e.keys())

    for d in range(4, 7):
        e['diam'].value = d + random.uniform(-.7, .7)

        for l in range(4, 7):
            e['length'].value = l + random.uniform(-.7, .7)

            for b in range(8500, 9500, 200):
                e['br'].value = b + random.uniform(-110, 110)

                e['diam'].change_data()
                e['length'].change_data()
                e['br'].change_data().submit()
                # This last .subimt() is hitting <Enter> in the text field

                e['gauss'].value = float(e['gauss'].get_data().text)
                print(e['gauss'].value)

                csv_write_elements(e, dictwriter)
                time.sleep(2.5)


def randomLoop(e, dictwriter):

    for x in range(0, 600):
        e['diam'].value = random.uniform(2, 8)
        e['length'].value = random.uniform(2, 8)
        e['br'].value = random.uniform(5000, 10000)

        e['diam'].change_data()
        e['length'].change_data()
        e['br'].change_data().submit()
        # This last .subimt() is hitting <Enter> in the text field

        e['gauss'].value = float(e['gauss'].get_data().text)
        print(e['gauss'].value)

        csv_write_elements(e, dictwriter)
        time.sleep(2.5)


def afterScrap(csvfile):
    # Not needed since matlab is better
    draw_plot_from_csv('data_csv')
    # MyAnimation()
    pass
