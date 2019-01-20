from django.shortcuts import render

# Create your views here.
#보여줄 화면을 만들었으니 이제 연결
def home(request):
    return render(request, 'wordcount/home.html')
#render(request, 'wordcount/home.html') 
# 여기서 request 뒤에 적는 내용은 home.html이라는 
# template이 위치하는 경로입니다.

#앞서 템플릿을 templates/wordcount/home.html 경로에 만들었기 때문에 
# wordcount/home.html로 적어줍니다.

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dictionary = {}

    for word in word_list:
        if word in word_dictionary:
            # Increase
            word_dictionary[word] += 1
        else:
            # add to the dictionary
            word_dictionary[word] = 1

    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list), 'dictionary': word_dictionary.items()})