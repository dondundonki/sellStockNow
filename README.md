# sellStockNow

This function runs on a Lambda on AWS that has a Cloudwatch EventBridge that triggers it every 12 hour. 

It is used to inform me when a Stock is good to sell off based on the pe ratio. (40% and above).

Future Improvements:
Onboard other users.

Plan:
Store other users CHAT_ID with stock_list in a DynamoDB and retrieve and tell other users.

Ask for input on the telegram side.

Check valid ticker option to check for invalid tickers