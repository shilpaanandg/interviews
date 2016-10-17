import sys
from optparse import OptionParser
import requests

restaurants_api= r'http://server_name:80/restaurants'

def get_restaurants_by_postcode(post_code):
    try:
        payload={'q':post_code}
        headers={'Accept-Tenant':'uk',
                 'Accept-Language':'en-GB',
                 'Authorization':'Basic VGVjaFRlc3RBUEk6dXNlcjI=',
                 'Host': 'public.je-apis.com',
                 'Accept-Version':'1'}
        r=requests.get(restaurants_api,headers=headers,params=payload)
        if r.status_code==200:
            result=r.json()
            if len(result['Restaurants'])==0:
                print "No restaurant found. Postcode may be wrong."
            for restaurant in result['Restaurants']:
                print '\nName: ',restaurant['Name']
                print 'Rating: ',restaurant['RatingAverage']
                print 'Type of food: '
                for cuisine in restaurant['CuisineTypes']:
                    print '\t',cuisine['SeoName']

        else:
            print "Oops!!Something went wrong."

    except exception,ee:
        print ee



if __name__=='__main__':
    
    parser = OptionParser()
    parser.add_option("-p", "--postcode", dest="post_code",
                      help="Postcode to search restaurants", metavar="POSTCODE")

    (options, args) = parser.parse_args()
    if options.post_code:
        get_restaurants_by_postcode(options.post_code)
    else:
        print '''Please run this script as following. Postcode option is required:
        python get_restaurants.py --postcode=bs32'''
    