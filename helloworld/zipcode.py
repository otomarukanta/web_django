import urllib2
import xml.etree.ElementTree as ET


def get_address(zipcode):
    url = 'http://zip.cgis.biz/xml/zip.php'
    full_url = url + '?zn=' + str(zipcode)
    data = urllib2.urlopen(full_url)
    return data.read()


def get_state(zipcode):
    root = ET.fromstring(get_address(zipcode))
    return root[9][4].get('state')


if __name__ == '__main__':
    print get_state(5140111)
