from address import Address
from mailing import Mailing

to_address = Address("64700","Норильск","Мира","28","43")
from_address = Address("653000","Краснодар","Красная","39","53")
mailing = Mailing(to_address,from_address,"1000","945367290")
print(mailing)