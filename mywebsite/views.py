from django.http import HttpResponse
from django.shortcuts import render
import operator

# Create your views here.
def homepage(request):
	return render(request,'home.html' )

def count(request):
	
	data = request.GET["fulltextarea"]
	word_list = data.split()
	len_wordlist = len(word_list)

	wordset = {}
	for word in word_list:
		if word in wordset:
			wordset[word]+=1
		else:
			wordset[word]=1

	sort_list = sorted(wordset.items(), key= operator.itemgetter(1))
	return render(request, 'count.html', {'name': data , 'count': len_wordlist, 'wordset': wordset.items() })

def aboutus(request):
	return render(request,'aboutus.html')


