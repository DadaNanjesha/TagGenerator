from django.db import models

class QRCode(models.Model):
    data = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.data[:50]
