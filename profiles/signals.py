# yeni bir user oluşturulduğu anda bu user ile ilişkili olarak bir profil nesnesi oluşturacağız.

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model # projemizdeki aktif user modelini döndürür, bunun varsayılanını da settings.py içerisinden değiştirdiğimiz için aslında bizim oluşturduğumuz CustomUser modeli gelecektir.

from profiles.models import Profile

user = get_user_model()

@receiver(post_save, sender=user)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)