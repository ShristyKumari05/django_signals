from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Create a receiver function
@receiver(my_signal)
def my_handler(sender, **kwargs):
    print("Signal handler executed")