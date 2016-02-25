from app.model.auction import Auction
from app.model.bidding import Bidding
from app.database import db_session

# help(Bidding.query)
# print Bidding.query.all()
# print Bidding.query.first()

a = Auction.query.get(1)

print a.biddings

b = Bidding.query.first()

print b.auction