from typing import List
from display_video_360.google_api import GoogleAPI


class DisplayVideo(GoogleAPI):

    def get_lineitems_for_advertiser(self, advertiser_id: str) -> List[dict]:
        """Gets line items and sets as a prop

        Args:
            advertiser_id (str): The advertiser id

        Returns:
            [list]: A list of all lineitems
        """
        res = self.service.advertisers().lineItems().list(advertiserId=advertiser_id).execute()

        return res.get("lineItems")

    def get_advertisers_for_partner(self, partner_id) -> List[dict]:
        """Gets all advertisers and sets on advertisers props"""
        res = self.service.advertisers().list(partnerId=partner_id).execute()
        self.advertisers = res.get("advertisers")
        return self.advertisers
