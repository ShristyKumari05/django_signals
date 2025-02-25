import threading
from django.test import TestCase
from django_signals.signals import my_signal, my_handler

class SignalTests(TestCase):
    def test_signal_execution(self):
        print("Before sending signal")
        my_signal.send(sender=None)
        print("After sending signal")

    def test_signal_thread(self):
        print(f"Caller thread: {threading.current_thread().name}")
        my_signal.send(sender=None)