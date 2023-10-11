from django.test import TestCase
from django.core.mail import outbox

print(outbox[0].subject)   # Should print "Subject Here" if everything's working correctly.
