feed_obj = Feed(feed_type='item', feed_scope='ALL_ACTIVE', category_id='220',
			       marketplace_id='EBAY_US', token=<TOKEN>, environment='SANDBOX')
result_code, api_status_code, file_path = feed_obj.get()
