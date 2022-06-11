from django.db import models

class IdentificationTypeOptions(models.TextChoices):
    """ Identification Type Options 
    
        CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
    """

    BIRTH_CERTIFICATE = 'BIRTH_CERTIFICATE', 'Birth Certificate'
    NATIONAL_ID = 'NID', 'NID'
    