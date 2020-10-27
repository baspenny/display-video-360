import os
from display_video_360.display_video import DisplayVideo

if __name__ == '__main__':
    from pathlib import Path

    BASE_PATH = Path().resolve()
    service_account_file = os.path.join(BASE_PATH, 'secrets', 'service_account.json')
    display_video = DisplayVideo(service_account_file)
    line_items = display_video.get_lineitems_for_advertiser('2355552')
    advertisers = display_video.get_advertisers_for_partner('2104250')

    pass