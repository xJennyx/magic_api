

def test_create_short_url(url_creator_endp):
    #site_url='https://www.wbd.com/news/warner-bros-discovery-names-ryan-gould-and-bobby-voltaggio-heads-us-advertising-sales'
    url_creator_endp.create_short_url_for_long_url(long_url='https://www.wbd.com/news/warner-bros-discovery-names-ryan-gould-and-bobby-voltaggio-heads-us-advertising-sales')
    url_creator_endp.check_response_status_is_ok()
    url_creator_endp.check_long_url_same_as_sent()
    url_creator_endp.check_code_is_not_empty()


def test_custom_short_url(url_creator_endp, random_string):
    site_url = 'https://www.wbd.com/news/warner-bros-discovery-names-ryan-gould-and-bobby-voltaggio-heads-us-advertising-sales'
    code = random_string
    url_creator_endp.create_short_url_for_long_url(site_url, code)
    url_creator_endp.check_response_status_is_ok()
    url_creator_endp.check_long_url_same_as_sent()
    url_creator_endp.check_short_code_same_as_sent()