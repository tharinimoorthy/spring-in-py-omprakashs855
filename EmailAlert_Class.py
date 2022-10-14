class EmailAlert:
    
    def __init__(self):
        self.email_check = False

    # @property
    def emailSent(self, val, max_th):
        if val > max_th:
            self.email_check = True
            print("Value above Threshold, Email Sent !!!")
        return self.email_check

