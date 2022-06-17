from django.db import models

class IdentificationTypeOptions(models.TextChoices):
    """ Identification Type Options 
    
        CONSTANT = DB_VALUE, USER_DISPLAY_VALUE
    """

    BIRTH_CERTIFICATE = 'BIRTH_CERTIFICATE', 'Birth Certificate'
    NATIONAL_ID = 'NID', 'NID'

class ClassOptions(models.TextChoices):
    ''' Class Options For Train '''	
    SHOVAN = 'SHOVAN', 'Shovan'
    S_CHAIR = 'S_CHAIR', 'Shovan Chair'
    SNIGDHA = 'SNIGDHA', 'Snigdha'
    AC_BERTH = 'AC_BERTH', 'AC BERTH'
    AC_SEAT = 'AC_SEAT', 'AC Seat'
    F_CHAIR = 'F_CHAIR', 'First Class Chair'
    F_BERTH = 'F_BERTH', 'First Class Berth'
    F_SEAT = 'F_SEAT', 'First Class Seat'
    
