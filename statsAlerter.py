class StatsAlerter:
    def __init__(self, maxThreshold, class_obj_list):
        self.maxThreshold = maxThreshold
        [self.email_obj, self.led_obj] = class_obj_list

    def checkAndAlert(self, numbers):
        for value in numbers:
            print("\nCurrent Value : {}".format(value))
            print("Threshold Value : {}".format(self.maxThreshold))
            val = value
            max_th = self.maxThreshold
            self.email_obj.emailSent(val , max_th)
            self.led_obj.ledGlows(val , max_th)


