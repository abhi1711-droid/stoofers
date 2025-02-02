from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pincode(models.Model):
    pincode = models.CharField(max_length=6)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)


class University(models.Model):
    name = models.CharField(max_length=255, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class College(models.Model):
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True)
    university = models.ForeignKey(University, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name
