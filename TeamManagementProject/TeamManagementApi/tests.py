# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Teamlist

# Create your tests here.
class ModelTestCase(TestCase):
    def setup(self):
        self.first_name = 'Gaurav'
        self.last_name = 'Kumar'
        self.phone = '123456789'
        self.email = 'aavrug@gmail.com'
        self.role = 0
        self.teamlist = Teamlist(
        	first_name = self.first_name,
            last_name = self.last_name,
            phone = self.phone,
            email = self.email,
            role = self.role
        )

    def test_model_can_create_a_teamlist(self):
    	old_count = Teamlist.objects.count()
        self.teamlist.save()
        new_count = Teamlist.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.teamlist_data = {
            'first_name': 'Harry',
            'last_name': 'Potter',
            'phone': '9999999999',
            'email': 'xyz@xyz.com',
            'role': 1
        }
        self.response = self.client.post(
            reverse('create'),
            self.teamlist_data,
            format="json")

    def test_api_can_create_a_teamlist(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_api_can_get_a_teamlist(self):
        teamlist = Teamlist.objects.get()
        response = self.client.get(
            reverse('details',
            kwargs={'pk': teamlist.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, teamlist)

    def test_api_can_update_teamlist(self):
        change_teamlist = {'first_name': 'Different name'}
        res = self.client.put(
            reverse('details', kwargs={'pk': teamlist.id}),
            change_teamlist, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_teamlist(self):
        teamlist = Teamlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': teamlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)

