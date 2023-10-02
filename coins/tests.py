# from django.test import TestCase
# from django.contrib.auth.models import User
# from coins.models import (
#     CoinBaseModel,
#     SelectOneMint,
#     CoinFamily,
#     Denominations,
#     CoinTypeName,
#     GradingServices,
#     CoinGrades,
#     Strike,
# )
# from images.models import Images


# class CoinBaseModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # Set up non-modified objects used by all test methods
#         mint = SelectOneMint.objects.create(name="Mint A")
#         family = CoinFamily.objects.create(name="Family A")
#         denomination = Denominations.objects.create(name="Denomination A")
#         coin_type = CoinTypeName.objects.create(name="Coin Type A")
#         grading_service = GradingServices.objects.create(name="Grading Service A")
#         coin_grade = CoinGrades.objects.create(name="Coin Grade A")
#         strike = Strike.objects.create(name="Strike A")

#         cls.user = User.objects.create_user(username="testuser", password="testpass")
#         cls.image = Images.objects.create(name="Test Image")

#         cls.coin = CoinBaseModel.objects.create(
#             pcgs_number=123,
#             title="Test Coin",
#             year=2022,
#             year2=2023,
#             family_of_coin=family,
#             denomination_of_coin=denomination,
#             coin_type=coin_type,
#             cost=9.99,
#             quantity=10,
#             sale_price=19.99,
#             strike=strike,
#         )
#         cls.coin.mint.add(mint)
#         cls.coin.grading.add(grading_service)
#         cls.coin.grade = coin_grade
#         cls.coin.images.add(cls.image)

#     def test_model_str(self):
#         coin = CoinBaseModel.objects.get(pk=self.coin.pk)
#         expected_str = (
#             f"{coin.year}-{coin.mint.first()} {coin.coin_type} {coin.grading.first()} {coin.strike} {coin.grade}"
#         )
#         self.assertEqual(str(coin), expected_str)

#     def test_model_fields(self):
#         coin = CoinBaseModel.objects.get(pk=self.coin.pk)
#         self.assertEqual(coin.pcgs_number, 123)
#         self.assertEqual(coin.title, "Test Coin")
#         self.assertEqual(coin.year, 2022)
#         self.assertEqual(coin.year2, 2023)
#         self.assertEqual(coin.family_of_coin, CoinFamily.objects.get(name="Family A"))
#         self.assertEqual(coin.denomination_of_coin, Denominations.objects.get(name="Denomination A"))
#         self.assertEqual(coin.coin_type, CoinTypeName.objects.get(name="Coin Type A"))
#         self.assertEqual(coin.cost, 9.99)
#         self.assertEqual(coin.quantity, 10)
#         self.assertEqual(coin.sale_price, 19.99)
#         self.assertEqual(coin.strike, Strike.objects.get(name="Strike A"))

#     def test_model_related_fields(self):
#         coin = CoinBaseModel.objects.get(pk=self.coin.pk)
#         self.assertEqual(coin.mint.count(), 1)
#         self.assertEqual(coin.mint.first(), SelectOneMint.objects.get(name="Mint A"))
#         self.assertEqual(coin.grading.count(), 1)
#         self.assertEqual(coin.grading.first(), GradingServices.objects.get(name="Grading Service A"))
#         self.assertEqual(coin.grade, CoinGrades.objects.get(name="Coin Grade A"))
#         self.assertEqual(coin.images.count(), 1)
#         self.assertEqual(coin.images.first(), self.image)
