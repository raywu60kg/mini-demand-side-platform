from app.logger import get_logger

log = get_logger(logger_name="get_ads")


class GetAds():
    def get_eligible_ads(self):
        raise NotImplementedError


class GetAdsFromPostgres(GetAds):

    def get_eligible_ads(self, postgres_client):
        try:
            conn = postgres_client

            # Open a cursor to perform database operations
            cur = conn.cursor()

            # Execute a query
            cur.execute("SELECT * FROM ad WHERE status='True';")
            column_names = [desc[0] for desc in cur.description]
            # Retrieve query results
            eligible_ads = cur.fetchall()
            formated_eligible_ads = []
            for ads_info in eligible_ads:
                eligible_ad = {}
                for key, value in zip(column_names, ads_info):
                    eligible_ad[key] = value
                formated_eligible_ads.append(eligible_ad)
            return formated_eligible_ads
        except Exception as e:
            log.error("Get eligible ads error: {}".format(e))
            return None
