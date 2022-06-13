from datetime import date, timedelta
from time import sleep
from django.core.management.base import BaseCommand
from myapp.models import PeremptionProduit, Notification

class Command(BaseCommand):
    help = "Check si des produits vont périmer et crée une notification si c'est le cas"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'Starting long-running job.'))

        while True:
            listeDate = PeremptionProduit.objects.all()

            for dateP in listeDate:
                refFamily = dateP.refProduit.refStockage.refFamily
                stockageNom = dateP.refProduit.refStockage.nom
                produitNom = dateP.refProduit.nom
                
                if ((dateP.datePeremption - timedelta(days=dateP.notifPeremption)) <= date.today() ):
                    if (len(Notification.objects.filter(refPeremption=dateP)) == 0):
                        Notification.objects.create(
                            message = "Le produit " +produitNom+ " va bientôt périmer dans "+stockageNom,
                            refPeremption = dateP,
                            refFamily = refFamily,
                        )

            sleep(5)
        