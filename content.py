#layout
meta = {
        'author': 'drew verlee',
        'description' : 'Online Art Gallery',
        'keywords' : 'Art, Gallery, Flowers, Abstract, Stick',
        'viewport' : 'width=device-width, initial-scale=1.0, minimum-scale=1.0'
        }

internal_urls = ['home', 'gallery', 'about','purchase', 'tour', 'reviews']
copy_right = "NY, New York City 88516, Rich ave P0 234. &copy; 2014 "
logo = "DREW'S ART"


#global
images = 'static/images/'
alt = 'art piece'

#cover
cover_art = ['Abstract_4.jpg', 'Flowers_2.jpg', 'Stick_1.jpg']
cover_art = [images + a for a in cover_art]
external_links = {
        'Michael Whelan' : 'www.michaelwhelan.com/',
        'pablo picasso'  : 'http://en.wikipedia.org/wiki/Pablo_Picasso',
        'Lenonardo da vinci' : 'http://en.wikipedia.org/wiki/Leonardo_da_Vinci',
        'Vincent van Gogh' : 'http://en.wikipedia.org/wiki/Vincent_van_Gogh',
        'Andy Warhol' : 'http://en.wikipedia.org/wiki/Andy_Warhol'
        }

email_hyper_link= 'drew.Verlee@gmail.com'

#about
picture_of_drew = images + 'drew.jpg'
about_art = images + 'Stick_3.jpg'
about_drew='''Artistic mastermind drew Verlee was born in Michigan. Raised and
taught by wolves. His style has been hailed as revolutionary. A renowned time traveler
drew had the ability to study under many famous artists'''

drew_facts = [
    'The flue gets drew shots',
    'Drew is the reason why Waldo is hiding',
    'Death once had a near-drew experience',
    'Drew makes onions cry'
    ]

# purchase
purchase_art = images + 'Flowers_1.jpg'
purchase_table = {'small': '150', 'large': '200'}
purchase_info="Prices vary by something something something..."
email_form_heading="Send me an email with your order!"

# tour page
tour_art = images + 'Flowers_4.jpg'
tour_info="Here are some dates and locations where you can come see how amazing I am"
tour_table = {'Detroit': '4/7/2015', 'Croatia': '4/25/2015', 'Iceland': '5/20/2015'}

#reviews page
review_art = images + 'Abstract_4.jpg'
review = "review" * 50
text_reviews = [review] * 3


#TODO better way, read file
stick_art = [images + 'Stick_' + str(x) + '.jpg' for x in range(1,5)]
flowers_art = [images + 'Flowers_' + str(x) + '.jpg' for x in range(1,5)]
abstract_art = [images + 'Abstract_' + str(x) + '.jpg' for x in range(1,5)]
animated_art = ['abstract', 'ball', 'boom', 'heart', 'line']
animated_art = [images + x + '.gif' for x in animated_art]


gallery_art = {
        'stick': stick_art,
        'abstract': abstract_art,
        'flower': flowers_art,
        'animated': animated_art,
        }
