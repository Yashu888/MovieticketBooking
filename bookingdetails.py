class Bookings:
    def __init__(self,bid, custname, selected_slot, movname,aseattype,tickets_booked,time,date):
        self.bid=bid
        self.custname=custname
        self.slot=selected_slot
        self.movname=movname
        self.aseattype=aseattype
        self.booked=tickets_booked
        self.time=time
        self.date=date
    
    def __str__(self):
        return str(self.bid)+"      |   "+self.custname+"  |    "+str(self.slot)+"  |   "+str(self.movname)+"   |   "+(self.aseattype)+"    |   "+str(self.booked)+"    |   "+str(self.time)+"  |   "+str(self.date)+"  |   ""\n--------------------------------------------------------------------------------------------------------------------\n"

