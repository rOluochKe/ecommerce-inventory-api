import pytest
from django.core.exceptions import ValidationError

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    def test_str_output(self, category_factory):
        obj = category_factory(name="test_cat")
        assert obj.__str__() == "test_cat"


class TestBrandModel:
    def test_str_output(self, brand_factory):
        obj = brand_factory(name="test_brand")
        assert obj.__str__() == "test_brand"


class TestProductModel:
    def test_str_output(self, product_factory):
        obj = product_factory(name="test_product")
        assert obj.__str__() == "test_product"


class TestProductLineModel:
    def test_str_output(self, product_line_factory):
        obj = product_line_factory(sku="12345")
        assert obj.__str__() == "12345"

    def clean_duplicate_order_values(self, product_line_factory, product_factory):
        obj = product_factory()
        product_line_factory(order=1, product=obj)
        with pytest.raises(ValidationError):
            product_line_factory(order=1, product=obj).clean()


class TestProductImageModel:
    def test_str_method(self, product_image_factory, product_line_factory):
        obj1 = product_line_factory(sku="12345")
        obj2 = product_image_factory(order=1, product_line=obj1)
        assert obj2.__str__() == "12345_img"

    def test_alternative_text_field_length(self, product_image_factory):
        alternative_text = "x" * 101
        with pytest.raises(ValidationError):
            product_image_factory(alternative_text=alternative_text)

    def test_duplicate_order_values(self, product_image_factory, product_line_factory):
        obj = product_line_factory()
        product_image_factory(order=1, product_line=obj)
        with pytest.raises(ValidationError):
            product_image_factory(order=1, product_line=obj).clean()
