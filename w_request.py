#/usr/bin/python3

import requests


def getPdf(myUrl):
	r = requests.get(myUrl)
	return r.content

t_url = "https://sfc-va3-ds1-2-customer-stage.s3.us-east-1.amazonaws.com/q3h00000-s/stages/8cfe13e0-ca16-40fb-8234-93e7334112c8/pdfFour.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIATA3OVJKND4IUW7WW%2F20220810%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220810T023705Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=538a345ca56454b8218461a6fd80b3b472968faec9ae20a76dce49b114d904df"

with open('thedoc.pdf', 'wb') as mydoc:
	mydoc.write(getPdf(t_url))
