from django.db import models



class data(models.Model):
	    city = models.CharField(max_length=255L)
	    location = models.CharField(max_length=255L)
	    q1_2010 = models.IntegerField()
	    q2_2010 = models.IntegerField()
	    q3_2010 = models.IntegerField()
	    q4_2010 = models.IntegerField()
	    q1_2011 = models.IntegerField()
	    q2_2011 = models.IntegerField()
	    q3_2011 = models.IntegerField()
	    q4_2011 = models.IntegerField()
	    q1_2012 = models.IntegerField()
	    q2_2012 = models.IntegerField()
	    q3_2012 = models.IntegerField()
	    q4_2012 = models.IntegerField()
	    class Meta:
	        db_table = 'Data'

# Create your models here.
