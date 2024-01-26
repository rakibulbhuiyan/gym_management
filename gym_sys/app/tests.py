from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from .models import (Banners,Service,Pages,Faq,Enquiry)
# Create your tests here.
class BannersModelTest(TestCase):
    def setUp(self):
        # Create a sample banner for testing
        self.banner = Banners.objects.create(
            img=SimpleUploadedFile("test_image.jpg", content=b"file_content", content_type="image/jpg"),
            alt_text="Test Alt Text"
        )
    def test_image_tag(self):
        # Call the image_tag method and check if the HTML is generated correctly   
        expected_html = '<img src="%s" width="80" />' % (self.banner.img.url)
        self.assertEqual(self.banner.image_tag(), expected_html)
class ServiceModelTest(TestCase):
    def setUp(self):
        self.service=Service.objects.create(
            title="Test_title",
            detail="test detail",
            img=SimpleUploadedFile("test_image.jpg", content=b"file_content", content_type="image/jpg")
        )
    def test_image_tag(self):
        html_return=self.service.image_tag()
        expected_html='<img src="%s" width="80" />' %(self.service.img.url)
        self.assertEqual(html_return, expected_html)
class PagesModelTest(TestCase):
    def setUp(self):
        self.page=Pages.objects.create(
            title="Test title",
            detail="test detail",
        )
    def test_str_method(self):
        expected_str='Test title'
        self.assertEqual(str(self.page),expected_str)
class FaqModelTest(TestCase):
    def setUp(self):
        self.faq=Faq.objects.create(
            ques="Test Question",
            ans="Test Answer",
        )
    def test_str_method(self):
        expected_str='Test Question'
        self.assertEqual(str(self.faq),expected_str)
    def test_faq_creation(self):
        self.assertIsInstance(self.faq,Faq)
        self.assertEqual(self.faq.ques,"Test Question")
        self.assertEqual(self.faq.ans,"Test Answer")
class EnquiryModelTest(TestCase):
    def setUp(self):
        self.enquiry=Enquiry.objects.create(
            full_name="Test title",
            email="Test email",
            detail="Test detail",
        )
    def test_str_method(self):
        expected_str='Test title'
        self.assertEqual(str(self.enquiry),expected_str)
    def test_enquiry_creation(self):
        self.assertIsInstance(self.enquiry,Enquiry)
        self.assertEqual(self.enquiry.full_name,"Test title")
        self.assertEqual(self.enquiry.email,"Test email")
        self.assertEqual(self.enquiry.detail,"Test detail")
        self.assertIsNotNone(self.enquiry.send_time)
        self.assertTrue(timezone.now()-self.enquiry.send_time<timezone.timedelta(seconds=1))
