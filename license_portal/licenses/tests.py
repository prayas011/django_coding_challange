from django.test import TestCase
from django.core.mail import outbox

# outbox[0] is the latest email in the outbox
print(outbox[0].subject)   # Should print "Subject Here" if everything's working correctly.
