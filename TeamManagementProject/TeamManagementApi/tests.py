# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse
from django.test import TestCase
from .models import Teamlist

# Create your tests here.
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
        teamlist = Teamlist.objects.get()
        change_teamlist = {'first_name': 'Different name'}
        res = self.client.patch(
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

