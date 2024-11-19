# Libraries
from datetime import datetime
from atproto import Client
from config import settings

# Error "management"
import warnings
warnings.filterwarnings('ignore')

# Import settings from config.py
bsky_username = settings['user']
bsky_password = settings['password']


def get_user_data(client, handle):
    user_data = client.get_profiles(actors=[handle])
    profiles = user_data.profiles
    return profiles[0]


def add_user_to_list(client, target, my_list):
    try:
        uid = get_user_data(client, target).did
        client.app.bsky.graph.listitem.create(
            repo=client.me.did,
            record={
                "subject": uid,
                "list": my_list,
                "createdAt": datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
            }
        )
        print(f"User {target} added to list")
    except Exception as e:
        print(e)
        return False


def main():
    # Instantiate the ATProto Bluesky API client
    client = Client()
    client.login(bsky_username, bsky_password)

    list_id = "3lugfvm99k1o2i" # List ID - find the ID in the URL of the list

    # The next three lines can be looped through a list of users to be added to the list
    target = "theaccountiwanttoadd.bsky.social" #handle of user to add to list
    my_list = f"at://{client.me.did}/app.bsky.graph.list/{list_id}"
    add_user_to_list(client, target, my_list)

if __name__ == "__main__":
    main()