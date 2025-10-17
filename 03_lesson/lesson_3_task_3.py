from address import Address
from mailing import Mailing

Address1 = Address(101000, "Moscow", "Frunze", 45, 15)
Address2 = Address(142003, "Tambov", "Krasnaya", 12, 3)
Mailing1 = Mailing(Address1, Address2, 1200, "RB458743678CN")
print(Mailing1)
