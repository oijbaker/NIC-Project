class Portfolio:
    # This class is used to simulate the performance of a portfolio of stocks
    
    def __init__(self, df, do_log = False):
        self.cash = 10000
        self.stocks = [[i, 0] for i in range(10)]
        self.df = df
        self.day = 0
        self.logbook = []
        self.do_log = do_log
        
    
    def log(self, string):
        self.logbook.append(string)   
        
        
    def buy_percentage(self, stock_index, percent):
        # Allow the user to buy a certain percentage of a stock's available volume
        volume_field = "vol" + str(stock_index)
        close__field = "close_" + str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        buy_no = int(volume*percent / 100)
        if buy_no * close_ < self.cash * 0.999:
            # Allow the user to buy a specific number of shares of a stock
            self.buy(stock_index, buy_no)
        else:
            self.buy(stock_index, int(self.cash / close_ * 0.999))
            
            
    def sell_percentage(self, stock_index, percent):
        # Allow the user to sell a certain percentage of a stock's available volume
        volume_field = "vol" + str(stock_index)
        close__field = "close_" + str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        buy_no = int(volume*percent / 100)
            
        if buy_no <= self.stocks[stock_index-1][1] * 0.999:
            # Allow the user to sell a specific number of shares of a stock
            self.sell(stock_index, buy_no)
        else:
            self.sell(stock_index, self.stocks[stock_index - 1][1])
        
        
    def buy(self, stock_index, number):
        """ Buy a stock

        Args:
            stock_index (int): This needs to be 
            number (_type_): _description_
        """
        volume_field = "vol" + str(stock_index)
        close__field = "close_" + str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        if number < 0.4 * volume and number * close_ < self.cash * 0.999:
            self.stocks[stock_index - 1][1] += number 
            self.cash -= number * close_ * 1.001
            
        if self.do_log:
            total_value = self.evaluate() + self.cash
            self.log("Bought "+str(number) + " of " + str(stock_index) + " at " + str(close_) + ". New value=" + str(total_value))
     
            
    def sell(self, stock_index, number):
        volume_field = "vol" + str(stock_index)
        close__field = "close_" + str(stock_index)
        
        volume = self.df[volume_field][self.day]
        close_ = self.df[close__field][self.day]
        
        if number <= self.stocks[stock_index - 1][1] and number < 0.4 * volume:
            self.stocks[stock_index - 1][1] -= number
            self.cash += number * close_ * 0.999
            
        if self.do_log:
            total_value = self.evaluate() + self.cash
            self.log("Sold "+str(number) + " of " + str(stock_index) + " at " + str(close_) + ". New value=" + str(total_value))
        
        
    def evaluate(self):
        # Calculates the total value of the portfolio by adding up the value of all stocks in the portfolio and the cash balance
        value = 0
        for stock in self.stocks:
            stock_index = self.stocks.index(stock)
            close_field = "close_" + str(stock_index+1)
            close = self.df[close_field][self.day]
            
            value += stock[1] * close
            
        return value + self.cash
