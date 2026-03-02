# Defines which iCal files are read into which spreadsheets.
# Ensure each one has a source, destination and files field, the source should be ./icals/Tutor or ./icals/master (this is the folder in which the cal.ical is in).
# Destination is the google calendar id, found under Integrate Calendar in settings, and files should be set to True.
ICAL_FEEDS = [
    {
        "source": "./icals/master",
        "destination": "0a8253f0cad4cfbc4a03483314c1ecb3ee0f55e913abd8f147fefda658e36cc7@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Rhys",
        "destination": "8bfa932a04dac5b6117627c75fca58206a0318d4128523c87aeecf379ab3516b@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Alex",
        "destination": "12bab8bca27461a513e0362ec8e67b8f7e19c963dc47b936ba78702ee3ac836b@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Charles",
        "destination": "88d2a629b19858ca1ad11cbbf6728d12d540e86af27ea58a723838f3b06a9956@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Ennel",
        "destination": "db18484a3990513571610acdbd8f0ca7330244933269232b6dcce8563fb85163@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Giselle",
        "destination": "c9c5fd8603f44e0133043da0414d90dc0d0e32309b2d4b84e186a85fe7f75c1e@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Harry",
        "destination": "5817311b537139af2dac987b2beaa0e0efe025947cb71703cd170b7fbd705f65@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Lauren",
        "destination": "ce06765ff8b5570c9393e4fd7f0b47753e7026aaf211e1dafa21039012f89b48@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Megan",
        "destination": "f4de689d214dd6e266e26fb8d7d2a9d92b69ad3cc30d257903e13d19ea70ce52@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Oscar",
        "destination": "6b951ad31eb98c3dbc3e61c98d60e85ce38e1883647b61d8fb6fc3e186278324@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Owen",
        "destination": "ee24b7052d9c6d69debd374f07892f8c30ffbf1649abf158971ac00ba836c87f@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Simon",
        "destination": "44fa4b2b5a994420f7ce50030b1e1af80b346fd41e9a27a6f8538cb777a59867@group.calendar.google.com",
        "files": True,
    },
    {
        "source": "./icals/Tina",
        "destination": "56e467601bdcef2522a52657a68ec6c961a7d090549b53490c2013517d9964d4@group.calendar.google.com",
        "files": True,
    }
]

SPREADSHEET_ID = "1CyLZRSk1SFdRVYnkbzy2fmLWEUF2P9S2utjD52YkW2Q"

WORKSHEET_NAMES = ["Rhys", "Alex", "Charles", "Ennel", "Giselle", "Harry", "Lauren", "Megan", "Oscar", "Owen", "Simon", "Tina"]

# These are the table headers chosen for the spreadsheet. They must match exactly to what is in the spreadsheet.
DATE_HEADER = "Date (Do Not Touch)"
START_TIME_HEADER = "Start Time"
END_TIME_HEADER = "End Time"
LOCATION_HEADER = "Location"
TYPE_HEADER = "Type" # This refers to the type of tutoring event, for example Tutor Hours or Seminar
NAME_HEADER = "Name (For Seminars)" # This is for the names of seminars and other important events

# Application name for the Google Calendar API
APPLICATION_NAME = "tutor-hours-scheduling-1234"

# File to use for logging output
LOGFILE = "tutor_calendar.log"

############## SHOULD NOT HAVE TO TOUCH ANYTHING BELOW #################

# API secret stored in this file
CLIENT_SECRET_FILE = "account_info.json"

# Location to store API credentials
CREDENTIAL_PATH = "credentials.json"

# Authentication information for the ical feeds.
# The same credentials are used for all feeds where 'files' is False
# If the feed does not require authentication or if FILES is true, it should be left to None
ICAL_FEED_USER = None
ICAL_FEED_PASS = None

# If the iCalendar server is using a self signed ssl certificate, certificate checking must be disabled.
# This option applies to all feeds where 'files' is False
# If unsure left it to True
ICAL_FEED_VERIFY_SSL_CERT = True

# Must use the OAuth scope that allows write access
SCOPES = ["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/spreadsheets"]


# Time to pause between successive API calls that may trigger rate-limiting protection
API_SLEEP_TIME = 0.10

# Integer value >= 0
# Controls the timespan within which events from ICAL_FEED will be processed
# by the script.
#
# For example, setting a value of 14 would sync all events from the current
# date+time up to a point 14 days in the future.
#
# If you want to sync all events available from the feed this is also possible
# by setting the value to 0, *BUT* be aware that due to an API limitation in the
# icalevents module which prevents an open-ended timespan being used, this will
# actually be equivalent to "all events up to a year from now" (to sync events
# further into the future than that, set a sufficiently high number of days).
ICAL_DAYS_TO_SYNC = 0

# Integer value >= 0
# Controls how many days in the past to query/update from Google and the ical source.
# If you want to only worry about today's events and future events, set to 0,
# otherwise set to a positive number (e.g. 30) to include that many days in the past.
# Any events outside of that time-range will be untouched in the Google Calendar.
# If the ical source doesn't include historical events, then this will mean deleting
# a rolling number of days historical calendar entries from Google Calendar as the script
# runs
PAST_DAYS_TO_SYNC = 30

# Restore deleted events
# If this is set to True, then events that have been deleted from the Google Calendar
# will be restored by this script - otherwise they will be left deleted, but will
# be updated - just Google won't show them
RESTORE_DELETED_EVENTS = True

# function to modify events coming from the ical source before they get compared
# to the Google Calendar entries and inserted/deleted
#
# this function should modify the events in-place and return either True (keep) or
# False (delete/skip) the event from the Calendar. If this returns False on an event
# that is already in the Google Calendar, the event will be deleted from the Google
# Calendar
from icalevents import icalparser

def EVENT_PREPROCESSOR(ev: icalparser.Event) -> bool:
    # include all entries by default
    # see README.md for examples of rules that make changes/skip
    return True


# Sometimes you can encounter an annoying situation where events have been fully deleted
# (by manually emptying the "Bin" for the calendar), but attempting to add new events with
# the same UIDs will continue to fail. Inserts will produce a 409 "already exists" error,
# and updtes will produce a 403 "Forbidden" error. Probably because the events are still
# stored somewhere even though they are no longer visible to the API or through the web
# interface.
#
# If you run into this situation and don't want to create a fresh calendar, you can try
# setting this value to something other than an empty string. It will be used as a prefix
# for new event UIDs, so changing it from the default will prevent the same IDs from being
# reused and allow them to be inserted as normal.
#
# NOTE: Characters allowed in the ID are those used in base32hex encoding, i.e. lowercase
# letters a-v and digits 0-9, see section 3.1.2 in RFC2938
EVENT_ID_PREFIX = ""