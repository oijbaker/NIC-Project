class Portfolio:
    
    
    def __init__(self, df):
        self.cash = 10000
        self.stocks = [[i, 0] for i in range(10)]
        self.df = df
        self.day = 0
        self.logbook = []
        self.do_log = True
        
    
    def log(self, string):
        self.logbook.append(string)   
        
    def buy(self, stock_index, number):
        """ Buy a stock

        Args:
            stock_index (int): This needs to be 
            number (_type_): _description_
        """
        volume_field = "vol"+str(stock_index)
        close__field = "close_"+str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        if number < 0.4*volume and number*close_ < self.cash*0.999:
            self.stocks[stock_index-1][1] += number
            
        self.cash -= number*close_*0.999
        if self.do_log:
            total_value = self.evaluate()+self.cash
            self.log("Bought "+str(number)+" of "+str(stock_index)+" at "+str(close_)+". New value="+str(total_value))
     
            
    def sell(self, stock_index, number):
        volume_field = "vol"+str(stock_index)
        close__field = "close_"+str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        if number <= self.stocks[stock_index-1][1]*0.999 and number < 0.4*volume:
            self.stocks[stock_index-1][1] -= number
            
        self.cash += number*close_*0.999
        if self.do_log:
            total_value = self.evaluate()+self.cash
            self.log("Sold "+str(number)+" of "+str(stock_index)+" at "+str(close_)+". New value="+str(total_value))
        
        
    def evaluate(self):
        value = 0
        for stock in self.stocks:
            stock_index = self.stocks.index(stock)
            close_field = "close_"+str(stock_index+1)
            close = self.df[close_field][self.day]
            
            value += stock[1]*close
            
        return value+self.cash
