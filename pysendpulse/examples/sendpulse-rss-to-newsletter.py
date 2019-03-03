# RSS to Newsletter
# This script checks your website RSS feed everyday and sends today's post (if any) to your mailing list.
# If you run it on a server, you might need to use "screen" or "tmux" to keep the script running after closing your Terminal.
# Change the values of the following variables: feed, REST_API_ID, REST_API_SECRET, from_email, from_name, addressbook_id

from pysendpulse.pysendpulse import PySendPulse
import feedparser
import datetime
import schedule
import time


# Schedule function

def job():
    
    # Find the last post in the RSS feed

    feed = feedparser.parse('https://yourwebsite.com/feed/')    # Change to your RSS feed link
    feed_date = feed.entries[0]['updated'][0:16]    # Latest post publish date (without time)
    feed_title = feed.entries[0]['title']    # Post title
    feed_description = feed.entries[0]['description']    # Post description
    feed_link = feed.entries[0]['link']    # Post link


    # Extract the post description only without links (we will have our own format later)

    description_start = feed_description.find("<p>") + 3
    description_end = feed_description.find("</p>")
    feed_description = feed_description[description_start:description_end]


    # Find today's date

    now = datetime.datetime.now()
    today = now.strftime("%a, %d %b %Y")     # Format to: "Thu, 03 Jan 2019"


    # Check if the post was published today; if True, send the campaign

    if feed_date == today:

        if __name__ == "__main__":
            REST_API_ID = 'your_api_id_here'    # Find it at your SendPulse's Account Settings > API
            REST_API_SECRET = 'your_api_secret_here'    # Find it at your SendPulse's Account Settings > API
            TOKEN_STORAGE = 'memcached'
            SPApiProxy = PySendPulse(REST_API_ID, REST_API_SECRET, TOKEN_STORAGE)


            # Create a new email campaign and send it
            task_body = "<h2>"+feed_title+"</h2><p>"+feed_description+"</p><p><b>Read the complete post at: "+feed_link+"</b></p><br><br><br><p>---<br>You receive this email because you have subscribed to our tutorial notifications.</p>"
            SPApiProxy.add_campaign(from_email='email@yourwebsite.com',
                                    from_name='your_company_name',
                                    subject="[New] " + feed_title,     # Subject line = post line from the RSS feed; add any string you want
                                    body=task_body.encode('utf-8'),     # Without UFT-8 encoding, you might get an error
                                    addressbook_id= 11111,     # Change to your mailing list ID, found in its URL
                                    campaign_name=feed_title)   # Campaign name = post line from the RSS feed;



# Schedule the job to run every day at a specific time

schedule.every().day.at("11:30").do(job)
#schedule.every(1).minutes.do(job)    # Can be used for testing purposes

while True:
    schedule.run_pending()
    time.sleep(1)
