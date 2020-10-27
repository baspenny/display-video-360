# Google Display & Video 360

This package contains a nice and convienient class to 
interface with the Display & Video 360 API.  

### Authentication
The authentication can be done in two ways.
1. With service account credentials
2. With a credential file obtained via the implicit grant flow

Please use absolute paths at all times to point to the credentials.

## installation

```
pip install display-video-360
```

## Examples
```python
import os
from display_video_360.display_video import DisplayVideo

if __name__ == '__main__':
    from pathlib import Path

    BASE_PATH = Path().resolve()
    service_account_file = os.path.join(BASE_PATH, 'secrets', 'service_account.json')
    
    display_video = DisplayVideo(service_account_file)
    
    line_items = display_video.get_lineitems_for_advertiser('ADVERTISER_ID')
    advertisers = display_video.get_advertisers_for_partner('PARTNER_ID')

```
