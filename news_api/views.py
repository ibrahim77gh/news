from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from firebase_admin import firestore
import os
from .Firebase import Firebase

# Create your views here.
class GeneralView(APIView):
    def get_documents(self, collection_name):
        firebase = Firebase()
        firebase.get_app()
        db = firestore.client()
        collection_name = collection_name

        # Retrieve all documents from the collection
        docs = db.collection(collection_name).get()

        # Convert documents to a list of dictionaries
        documents = [doc.to_dict() for doc in docs]
        # Return the documents as a JSON response
        return Response(documents)

class PoliticsView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='politics_collection')
    
class SportsView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='sports_collection')
        
class BusinessView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='business_collection')
    
class HedgeView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='hedge_collection')
    
class RockWellView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='rockwell_collection')
    
class LocalnewsView(GeneralView):
    def get(self, request):
        return self.get_documents(collection_name='localnews_collection')