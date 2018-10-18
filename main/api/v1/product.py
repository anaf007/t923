#coding=utf-8
from flask_restful import Resource
from main.extensions import apiManager
from main.models.products import Product
from sqlalchemy import desc


apiManager.create_api(Product, methods=['GET'])

