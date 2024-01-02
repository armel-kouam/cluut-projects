import boto3
import pandas as pd
from boto3.dynamodb.conditions import Key




dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Orders')
# get_productorders_timerange: Input <productName>, Output <DataFrame>

def get_productorders_timerange(productName):
  
   response = table.query(
       KeyConditionExpression=Key('product').eq(productName), 
       IndexName = 'Products',
       ProjectionExpression = "orderID, quantity")
   dataf = pd.DataFrame(response["Items"])
   dataf["orderID"] = pd.to_datetime(dataf["orderID"])
   return(dataf)
   
# if __name__ == "__main__":
#     print(get_productorders_timerange('plant'))
    

# get_total_orders: Input <productName>, Output <Int>
def get_total_orders(productName):
   
   response_quantity = table.query(
       KeyConditionExpression=Key('product').eq(productName), 
       IndexName = 'Products',
       ProjectionExpression = "quantity")
   dataf = pd.DataFrame(response_quantity["Items"])
#   pd.to_numeric(dataf["quantity"]).sum()
   summe = int(pd.to_numeric(dataf["quantity"]).sum())
   return (summe)
   
   
   
if __name__ == "__main__":
    print(get_productorders_timerange('plant'))
    # print(get_total_orders('book'))
    

    
